# -*- coding: utf-8 -*-
# @Time    : 2020/1/9 11:11
# @Author  : Stephen
# @Email   : jacstephen@163.com
# @File    : login.py
# @Software: PyCharm

from pages.b_pages.basepage import BasePage
from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy as By
import time

class LoginPage(BasePage):
    '''登录页面封装'''
    mobile_loc = (By.ID,'com.qekj.merchant:id/et_account')
    pwd_loc = (By.ID,'com.qekj.merchant:id/et_password')
    login_loc = (By.ID,'com.qekj.merchant:id/rl_login')
    reset_pwd_loc = (By.ID,'com.qekj.merchant:id/tv_found_password')
    back_loc = (By.ID,'com.qekj.merchant:id/ll_back')

    def login_opera(self,moblie,pwd):
        '''商家端登录方法'''
        self.moblie_send(moblie)
        self.pwd_send(pwd)
        self.login_btn().click()
        time.sleep(2)

    def mobile(self)->WebElement:
        '''账号输入框'''
        user_ele = self.get_visible_element(self.mobile_loc)
        return user_ele

    def moblie_send(self,mobile):
        '''传入账号'''
        return self.mobile().send_keys(mobile)

    def pwd(self)->WebElement:
        '''密码输入框'''
        user_ele = self.get_visible_element(self.pwd_loc)
        return user_ele

    def pwd_send(self,pwd):
        '''传入密码'''
        return self.pwd().send_keys(pwd)

    def login_btn(self)->WebElement:
        '''登录按钮'''
        user_ele = self.get_clickable_element(self.login_loc)
        return user_ele

    def reset_pwd(self)->WebElement:
        '''找回/重置 密码'''
        user_ele = self.get_visible_element(self.reset_pwd_loc)
        return user_ele

    def back_btn(self)->WebElement:
        '''返回按钮'''
        user_ele = self.get_clickable_element(self.back_loc)
        return user_ele