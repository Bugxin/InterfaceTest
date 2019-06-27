#!/usr/bin/env python
# -*- coding:utf-8 -*-

import unittest
import ddt
from common import ExcelHandle
from common import RequestHandle
from common import DataCenter
from common import LogHandle
from conf import settings
import re

filename = settings.DATA_FILE
test_data = ExcelHandle.ReadExcel(filename).get_data()
log_obj = LogHandle.MyLogger(filename)


@ddt.ddt
class RunMyTest(unittest.TestCase):
    total_rows = 0  # excel表格已执行行数

    @classmethod
    def setUpClass(cls):
        cls.write_obj = ExcelHandle.WriteExcel(filename)

    @ddt.data(*test_data)
    @ddt.unpack
    def test_api(self, *data):
        RunMyTest.total_rows += 1
        data_obj = DataCenter.DataSource(data)
        is_run = data_obj.get_is_run()
        if is_run.lower() == 'yes':
            log_obj.logger.info("====== 测试开始 ======")
            # 取data中每个字段的值
            case_name = data_obj.get_name()
            checkpoint_key, checkpoint_val = data_obj.get_check_point()
            url = data_obj.get_url()
            method = data_obj.get_method()
            arg = data_obj.get_arg()
            body = data_obj.get_body()
            header = data_obj.get_header()

            # 发送请求
            res = RequestHandle.SendRequest.request_main(method, url, params=arg, data=body, headers=header)

            except_res = checkpoint_key + ':' + str(checkpoint_val)  # 预期结果
            actual_res = re.search('\"%s\":(\d+)' % checkpoint_key, res.text).group(1)  # 实际结果

            # 将结果写入excel
            if int(actual_res) == checkpoint_val:
                write_info = 'pass'
            else:
                write_info = 'fail'
            self.write_obj.write(RunMyTest.total_rows, data_obj.ACTUAL_RES, write_info)

            # 写入日志
            # get post 请求参数放的位置是不一样的
            if arg:
                para = arg
            else:
                para = body
            log_obj.case_info(case_name, url, para, except_res, actual_res)
            log_obj.logger.info("====== 测试结束 ======")
            # 断言
            self.assertEqual(int(actual_res), checkpoint_val, "%s执行失败" % case_name)

    @classmethod
    def tearDownClass(cls):
        cls.write_obj.sava()


if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(RunMyTest('test_api'))
    unittest.TextTestRunner().run(suit)
