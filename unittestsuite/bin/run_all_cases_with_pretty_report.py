import unittest
import datetime
from html_reporter import HTMLTestRunner
from utils.init_folder import init_folder_at_beginning

# output to a file
if __name__ == "__main__":
    my_test_suite = unittest.defaultTestLoader.discover('./../case/', pattern='test_baidu_*.py')

    date_time = datetime.datetime.now()
    date = date_time.strftime('%Y-%m-%d')
    report_time = date_time.strftime('%H%M%S')
    init_folder_at_beginning(date)
    report_path = './../report/html/' + date + '/' + report_time +'_bs4_report.html'
    runner = HTMLTestRunner(
        report_filepath=report_path,
        title="My unit test report",
        description="This demonstrates the report output by HTMLTestRunner.",
        open_in_browser=True
    )
    # run the test
    runner.run(my_test_suite)