#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 封装日志操作

import logging
from logging import handlers
from conf import settings
import os


class MyLogger(object):
    def __init__(self, file_name,
                 level=settings.LOG_LEVEL,
                 back_count=settings.LOG_BACKUP_COUNT,
                 when=settings.LOG_WHEN, interval=settings.LOG_INTERVAL):
        """
        :param file_name:   日志文件名
        :param level:   日志级别
        :param back_count:   日志文件保留个数
        :param when:   日志创建间隔单位
        """
        # 创建 logger
        logger = logging.getLogger()
        # 日志级别
        logger.setLevel(self.get_level(level))

        # 日志文件与 file_name同名 但路径不一样
        file_name = os.path.basename(file_name)
        file_name = r'%s\%s.log' % (settings.LOG_PATH, file_name.split('.')[0])

        # 日志输出到文件
        fh = handlers.TimedRotatingFileHandler(filename=file_name,
                                               when=when,
                                               interval=interval,
                                               backupCount=back_count,
                                               encoding='utf-8')

        # 日志格式
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(funcName)s[%(filename)s line:%(lineno)d] '
                                      '- %(message)s')
        fh.setFormatter(formatter)

        # Handler绑定到logger
        logger.addHandler(fh)

        self.logger = logger

    # 返回当前日志的级别
    def get_level(self, level_str):
        level = {
            'debug': logging.DEBUG,
            'info': logging.INFO,
            'warn': logging.WARNING,
            'error': logging.ERROR
        }
        level_str = level_str.lower()
        return level.get(level_str)

    def case_info(self, case_name, url, argument, expect_res, actual_res):
        """
        :param case_name:  case_name
        :param url:   请求url
        :param argument:   请求参数
        :param expect_res:  期望结果
        :param actual_res:  实际结果
        :return:
        """
        self.logger.info("测试用例: %s" % case_name)
        self.logger.info("url：%s" % url)
        self.logger.info("请求参数：%s" % argument)
        self.logger.info("期望结果：%s" % expect_res)
        self.logger.info("实际结果：%s" % actual_res)

# if __name__ == '__main__':
#     import os
#     filename = r'%s\log\test.log' % os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#     print(os.path.dirname(filename))
#     # with open(filename, 'w+') as f:
#     log_obj = MyLogger(filename)
#     log_obj.logger.error('一')
#     log_obj.logger.error('二')
#     log_obj.logger.error('三')
