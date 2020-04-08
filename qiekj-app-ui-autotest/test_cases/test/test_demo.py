# -*- coding: utf-8 -*-
# @Time    : 2019/11/21 11:18
# @Author  : Stephen
# @Email   : jacstephen@163.com
# @File    : test_demo.py
# @Software: PyCharm
import time

from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.keys import Keys
import unittest


class SearchTest(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['automationName'] = 'Appium'
        desired_caps['deviceName'] = '192.168.243.101:5555'
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['noReset'] = True
        desired_caps["appPackage"] = "com.qekj.merchant"
        desired_caps["appActivity"] = "com.qekj.merchant.ui.module.login.activity.LoginActivity"
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        sleep(5)

    def test_case(self):
        driver = self.driver

        user_name = driver.find_element_by_id("com.qekj.merchant:id/et_account")

        user_name.send_keys('18939651848')
        time.sleep(1)

        pass_word = driver.find_element_by_id("com.qekj.merchant:id/et_password")
        pass_word.send_keys('123456')
        time.sleep(1)

        login_btn = driver.find_element_by_id("com.qekj.merchant:id/rl_login")
        login_btn.click()

        time.sleep(5)



    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()