#!/usr/bin/env python
# -*- coding:utf-8 -*-

from conf import settings


class DataSource(object):
    # 取各个字段在excel中列号
    ID = settings.EXCEL_ARGUMENT.get('interface_id')
    NAME = settings.EXCEL_ARGUMENT.get('name')
    METHOD = settings.EXCEL_ARGUMENT.get('method')
    URL = settings.EXCEL_ARGUMENT.get('url')
    ARGS = settings.EXCEL_ARGUMENT.get('request_arg')
    HEADER = settings.EXCEL_ARGUMENT.get('header')
    BODY = settings.EXCEL_ARGUMENT.get('body')
    DEPEND = settings.EXCEL_ARGUMENT.get('depend')
    CHECK_POINT = settings.EXCEL_ARGUMENT.get('check')
    EXPECT_RES = settings.EXCEL_ARGUMENT.get('expect_res')
    ACTUAL_RES = settings.EXCEL_ARGUMENT.get('actual_res')
    IS_RUN = settings.EXCEL_ARGUMENT.get('is_run')

    # 处理对象是excel表中的一行数据
    def __init__(self, data):
        self.data = data

    def get_id(self, index=ID):
        interface_id = self.data[index]
        if interface_id != '':
            return int(interface_id)
        return None

    def get_name(self, index=NAME):
        name = self.data[index]
        if name != '':
            return name
        return None

    def get_method(self, index=METHOD):
        method = self.data[index]
        if method != '':
            return method
        return None

    def get_url(self, index=URL):
        url = self.data[index]
        if url != '':
            return url
        return None

    def get_arg(self, index=ARGS):
        arg = self.data[index]
        if arg != '':
            return arg
        return None

    def get_header(self, index=HEADER):
        header = self.data[index]
        if header != '':
            return header
        return None

    def get_body(self, index=BODY):
        body = self.data[index]
        if body != '':
            # 返回的是一个字典格式
            return eval(body)
        return None

    def get_depend(self, index=DEPEND):
        depend = self.data[index]
        if depend != '':
            return depend
        return None

    def get_check_point(self, index=CHECK_POINT):
        check_point = self.data[index]
        if check_point != '':
            key, val = check_point.split(':')
            return key, int(val)
        return None

    def get_expect_res(self, index=EXPECT_RES):
        expect_res = self.data[index]
        if expect_res != '':
            return expect_res
        return None

    def get_actual_res(self, index=ACTUAL_RES):
        actual_res = self.data[index]
        if actual_res != '':
            return actual_res
        return None

    def get_is_run(self, index=IS_RUN):
        is_run = self.data[index]
        if is_run != '':
            return is_run
        return None




