# -*- coding: utf-8 -*-
# @Time    : 2020/1/9 15:35
# @Author  : Stephen
# @Email   : jacstephen@163.com
# @File    : home.py
# @Software: PyCharm


from pages.b_pages.basepage import BasePage
from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy as By
import time

class HomePage(BasePage):
    '''商家端主页/首页'''

    home_tab_loc = (By.LINK_TEXT,'首页')

    def home_tab(self):
        '''底部切换tab'''
        ele=self.get_visible_element(self.home_tab_loc)
        return ele.click()

