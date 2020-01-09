# -*- coding: utf-8 -*-
# @Time    : 2019/11/18 11:52
# @Author  : Stephen
# @Email   : jacstephen@163.com
# @File    : basepage.py
# @Software: PyCharm


from appium.webdriver import Remote
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from common.keys import Keycode
from common.my_logger import MyLogger


class BasePage:
    def __init__(self,driver:Remote):
        self.driver = driver

    def get_visible_element(self,locator,equency = 20):
        '''获取可视元素'''
        try:
            return WebDriverWait(self.driver,equency).until(
                ec.visibility_of_element_located(locator))
        except Exception as e:
            self.driver.save_screenshot('elementshot.png')
            MyLogger().error('可视元素获取失败:{}'.format(e))

    def get_presence_element(self, locator, equency=20):
        '''获取存在元素'''
        try:
            return WebDriverWait(self.driver, equency).until(
                ec.presence_of_element_located(locator))
        except Exception as e:
            self.driver.save_screenshot('elementshot.png')
            MyLogger().error('进程树元素获取失败:{}'.format(e))

    def get_clickable_element(self, locator, equency=20):
        '''获取可点击元素'''
        try:
            return WebDriverWait(self.driver, equency).until(
                ec.element_to_be_clickable(locator))
        except Exception as e:
            self.driver.save_screenshot('elementshot.png')
            MyLogger().error('可点击元素获取失败:{}'.format(e))

    @property
    def width(self):
        '''获取屏幕宽度'''
        return self.driver.get_window_size().get('width',0)

    @property
    def height(self):
        '''获取屏幕高度'''
        return self.driver.get_window_size().get('height',0)

    def swipe_to_left(self,offset=0.1):
        '''从右向左滑动'''
        action = self.driver.swipe(self.width*(1-offset),
                                   self.height*0.5,
                                   self.width*offset,
                                   self.height*0.5
                                   )
        return action

    def swipe_to_right(self,offset=0.1):
        '''从左向右滑动'''
        action = self.driver.swipe(self.width*offset,
                                   self.height*0.5,
                                   self.width*(1-offset),
                                   self.height*0.5
                                   )
        return action

    def swipe_to_top(self,offset=0.1):
        '''从下至上移动'''
        action = self.driver.swipe(self.width*0.5,
                                   self.height*offset,
                                   self.width*0.5,
                                   self.height*(1-offset)
                                   )
        return action

    def swipe_to_bottom(self,offset=0.1):
        '''从下至上移动'''
        action = self.driver.swipe(self.width*0.5,
                                   self.height*(1-offset),
                                   self.width*0.5,
                                   self.height*offset
                                   )
        return action

    def click(self,locator):
        '''点击元素'''
        action = WebDriverWait(self.driver,15,poll_frequency=0.1).until(
            ec.element_to_be_clickable(locator))
        return action.click()

    def press_key_power(self):
        '''模拟按下电源键'''
        action = self.driver.press_keycode(Keycode.POWER)
        return action

    def press_key_home(self):
        '''模拟按下home键'''
        action = self.driver.press_keycode(Keycode.HOME)
        return action

    def press_key_back(self):
        '''模拟按下返回键'''
        action = self.driver.press_keycode(Keycode.BACK)
        return action

