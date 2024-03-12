import unittest
import HTMLTestRunner_PY3 as HTMLTestRunner
import datetime

from utils.init_folder import init_folder_at_beginning

suite = unittest.defaultTestLoader.discover('./../case/', pattern='test_baidu_*.py')

if __name__ == '__main__':
    date_time = datetime.datetime.now()
    date = date_time.strftime('%Y-%m-%d')
    report_time = date_time.strftime('%H%M%S')
    init_folder_at_beginning(date)
    fp = open('./../report/html/' + date + '/' + report_time +'_CN_report.html', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title = '测试报告',
        description='text'
    )
    runner.run(suite)
    fp.close()


