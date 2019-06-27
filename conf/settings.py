#!/usr/bin/env python
# -*- coding:utf-8 -*-


import os

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# 请求超时时间 单位s 秒
REQUEST_EXPIRED_TIME = 5


# 日志相关配置
LOG_PATH = r'%s\log' % BASE_PATH   # 日志保存目录
LOG_WHEN = 'D'    # 日志更新单位 D代表天
LOG_INTERVAL = 1  # 日志更新间隔 与when 搭配 1 D 表示1天
LOG_BACKUP_COUNT = 5  # 最多保留5份日志
LOG_LEVEL = 'info'   # 日志级别

# 邮件相关配置
MAIL_HOST = 'smtp.126.com'  # 网易126邮箱
MAIL_SENDER = 'aaaaaa@126.com'  # 发送者邮箱
MAIL_PWD = 'bbbbbbbb'    # 密码
MAIL_RECIEVERS = ['ccccccc@sina.com', ]   # 接收者

MAIL_SUBJECT = '老黄历接口测试结果'  # 邮件主题
MAIL_ON = False   # 是否开启邮件功能


# 参数配置
# excel字段对应的列号
EXCEL_ARGUMENT = {
    'interface_id': 0,     # 接口id
    'name': 1,         # 接口名
    'method': 2,       # 方法 get post
    'url': 3,
    'request_arg': 4,   # 请求参数
    'header': 5,       # 请求头
    'body': 6,        # 请求体
    'depend': 7,     # 数据依赖
    'check': 8,      # 检查点
    'expect_res': 9,   # 预期结果
    'actual_res': 10,   # 实际结果
    'is_run': 11        # 是否运行
}


# 数据源配置
DATA_PATH = r'%s\data' % BASE_PATH
DATA_FILE = r'%s\template.xls' % DATA_PATH   # 被测文件


# case配置
CASE_PATH = r'%s\testcases' % BASE_PATH

# 报告配置
REPORT_PATH = r'%s\reports' % BASE_PATH

# 数据库相关的配置
#
# if __name__ == '__main__':
#     print(BASE_PATH)
#     print(DATA_PATH)
#     print(LOG_PATH)
#
