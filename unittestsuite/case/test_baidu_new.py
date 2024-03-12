import unittest
import ddt
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.excel_read import ParseExcel


excelPath = './../data/test_data.xlsx'
sheetName = 'data_new'
excel = ParseExcel(excelPath, sheetName)

@ddt.ddt
class Test_Baidu_News(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def setUp(self):
        self.driver.get('http://news.baidu.com')
        sleep(2)

    def tearDown(self):
        pass

    @ddt.data(*excel.getDataFromSheetWithOneCol())
    def test_sou(self, data):
        self.driver.find_element(By.ID, 'ww').send_keys(data)
        sleep(2)
        self.driver.find_element(By.ID, 's_btn_wr').click()
        sleep(2)
        self.assertEqual('百度资讯搜索_%s'%data, self.driver.title)

if __name__ == '__main__':
    unittest.main()
