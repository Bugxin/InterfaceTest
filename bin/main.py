#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys
import time

# 入口路径
ENTRY_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ENTRY_PATH)


from conf import settings
from common import MailHandle
from common import HTMLTestRunner
from common import FileHandle
import unittest


if __name__ == "__main__":
    # 要测试的文件
    discover = unittest.defaultTestLoader.discover(settings.CASE_PATH,
                                                   pattern='Test*.py')

    # 按照一定的格式获取当前的时间
    now = time.strftime("%Y-%m-%d_%H-%M-%S-")

    # 定义报告存放路径
    filename = settings.REPORT_PATH + '\\' + now + 'result.html'
    fp = open(filename, 'wb')
    # 定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="接口测试报告", description="测试用例执行情况:")

    # 运行测试
    result = runner.run(discover)
    fp.close()  # 关闭报告文件

    # 获取最新测试报告
    report_file = FileHandle.get_newest_report()

    # 发送邮件
    if settings.MAIL_ON:
        MailHandle.SendMail().send_mail(settings.MAIL_SUBJECT,
                                        result.success_count,
                                        result.failure_count,
                                        report_file)
