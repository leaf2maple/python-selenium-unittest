import unittest
# from HtmlTestRunner import HTMLTestRunner
import os
import time
from BeautifulReport import BeautifulReport as bf


# addTest加载每个test开头的函数
# suite = unittest.TestSuite()
# suite.addTest(BaiduSearch('test_baidu_search'))
# suite.addTest(BaiduSearch('test_baidu_search2'))
# suite.addTest(SportNewsClick('test_sportnews_click'))

path = os.path.dirname(os.path.abspath('.')) + '/test_report/'
now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
report_path = path + now

suite = unittest.TestLoader().discover("testsuites")

if __name__ == '__main__':
    run = bf(suite)
    run.report(filename="wb01", description='盒子管理后台', report_dir=report_path)
    # with open(report_path, 'wb') as f:
    #     runner = HTMLTestRunner(f, report_title=u"WB01测试报告", descriptions=u"测试结果", verbosity=2)
    #     runner.run(suite)

