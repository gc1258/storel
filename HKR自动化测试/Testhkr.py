from xlutils import copy
import xlrd
from selenium import webdriver
from unittest import TestCase
from ddt import ddt
from ddt import data
from ddt import unpack
from InitPage import LoginData
from LoginOperation import LoginOpera
import time

wd = xlrd.open_workbook(filename="HKR.xls", encoding_override=True)
table = copy.copy(wd)


@ddt
class TestHkr(TestCase):
    success = LoginData(0)
    error = LoginData(1)



    # 在所有用例执行前执行
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8080/HKR")
        self.driver.maximize_window()

    # 在所有用例执行后执行
    def tearDown(self) -> None:
        self.driver.quit()


    @data(*success)
    @unpack
    def testLoginSuccess(self,username,password,expect,i):

        # username = testdata["username"]
        # password = testdata["password"]
        # expect = testdata["expect"]


        login = LoginOpera(self.driver)

        # 执行登陆的三项惭怍
        login.login(username,password)


        # 获取实际结果
        result = login.getLoginSuccessResult()

        time.sleep(3)

        if result == expect:
            table.get_sheet(0).write(i,3,"通过")
            table.save('HKR.xls')
        elif result != expect:
            table.get_sheet(0).write(i,3,"不通过")


        # 断言
        self.assertEqual(expect,result)


    @data(*error)
    @unpack
    def testLoginError(self,username,password,expect,i):

        # username = testdata["username"]
        # password = testdata["password"]
        # expect = testdata["expect"]


        login = LoginOpera(self.driver)

        # 执行登陆的三项惭怍
        login.login(username,password)


        # 获取实际结果
        result = login.getLoginErrorResult()

        time.sleep(3)

        if result == expect:
            table.get_sheet(0).write(i,3,"通过")
            table.save('HKR.xls')
        elif result != expect:
            table.get_sheet(0).write(i,3,"不通过")

        # 断言
        self.assertEqual(expect,result)





















