import os
import time
import unittest

import HTMLTestRunner_PY3

from script.test_ihrm import UnittestTest
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
suite=unittest.TestSuite()
suite.addTest(unittest.makeSuite(UnittestTest))
report_path=BASE_DIR+"/report/ihrm-{}.html".format(time.strftime("%Y%m%d%H%M%S"))
with open(report_path,mode="wb")as f:
    runner=HTMLTestRunner_PY3.HTMLTestRunner(f,verbosity=1,title="ihrm系统测试",description="我们的IHRM的接口测试报告")
    runner.run(suite)