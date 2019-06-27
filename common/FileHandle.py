#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
from conf import settings


# 获取最新的测试报告
def get_newest_report(test_report=settings.REPORT_PATH):
    lists = os.listdir(test_report)
    lists.sort(key=lambda fn: os.path.getmtime(test_report + '\\' + fn))   # 以文件修改时间排序
    file_new = os.path.join(test_report, lists[-1])   # 取最新修改的文件
    return file_new
