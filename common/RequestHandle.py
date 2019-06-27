#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests


class SendRequest(object):
    @staticmethod
    def request_main(method, request_url, **kwargs):
        try:
            res = requests.request(method, request_url, **kwargs)
            return res
        except(requests.ConnectionError, requests.HTTPError, requests.URLRequired, requests.Timeout,
                requests.ConnectTimeout) as e:
            print(e)


# if __name__ == '__main__':
#     obj = SendRequest()
#     res = obj.request_main('Get', 'http://www.baidu.com')
#     print(res.status_code)
#     print(res.url)