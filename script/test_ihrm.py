import unittest


import requests
from parameterized import parameterized

from utils import read_data


class UnittestTest(unittest.TestCase):
    def setUp(self):
        self.login_url="http://ihrm-test.itheima.net/api/sys/login"
    def tearDown(self):
        pass
    @parameterized.expand(read_data)
    def test01_login(self,casename,request_body,message):
        data=request_body
        response=requests.post(url=self.login_url,json=data)
        print(response.json())
        self.assertIn(message,response.json().get("message"))
