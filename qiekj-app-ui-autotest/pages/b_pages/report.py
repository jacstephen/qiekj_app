# -*- coding: utf-8 -*-
# @Time    : 2020/1/9 16:15
# @Author  : Stephen
# @Email   : jacstephen@163.com
# @File    : report.py
# @Software: PyCharm

from pages.b_pages.basepage import BasePage
from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy as By
import time

class ReportPage(BasePage):
    '''商家端报表页'''
    report_tab_loc = (By.LINK_TEXT,'报表')
    type_change_loc = (By.ID,'com.qekj.merchant:id/tv_change_type')
    list_loc = (By.ID,'com.qekj.merchant:id/tv_liushui')
    order_loc = (By.ID,'com.qekj.merchant:id/tv_order')
    export_loc = (By.ID,'com.qekj.merchant:id/tv_export')
    ex_email = (By.ID,'com.qekj.merchant:id/et_export_email')
    ex_cancel_loc = (By.ID,'com.qekj.merchant:id/ll_cancel')
    ex_confirm_loc = (By.ID,'com.qekj.merchant:id/ll_sure')
    screening_loc = (By.ID,'com.qekj.merchant:id/tv_screening')
    sc_confirm_loc = (By.ID,'com.qekj.merchant:id/ll_sure')
    sc_reset_loc = (By.ID, 'com.qekj.merchant:id/ll_reset')

    def report_tab(self):
        '''底部切换tab'''
        ele=self.get_visible_element(self.report_tab_loc)
        return ele.click()

    def type_change(self):
        '''流水/订单：类型切换'''
        ele = self.get_clickable_element(self.type_change_loc)
        return ele.click()

    def list_type(self):
        '''流水tab'''
        ele = self.get_clickable_element(self.list_loc)
        return ele.click()

    def order_type(self):
        '''订单tab'''
        ele = self.get_clickable_element(self.order_loc)
        return ele.click()

    def export_btn(self):
        '''导出按钮'''
        ele = self.get_clickable_element(self.export_loc)
        return ele.click()

    def export_email(self)->WebElement:
        '''导出目标邮箱地址'''
        ele = self.get_visible_element(self.ex_email)
        return ele

    def email_send(self,email):
        '''传入email'''
        return self.export_email().send_keys(email)

    def ex_cancel(self):
        '''导出--取消按钮'''
        ele = self.get_clickable_element(self.ex_cancel_loc)
        return ele.click()

    def ex_confirm(self):
        '''导出--确认按钮'''
        ele = self.get_clickable_element(self.ex_confirm_loc)
        return ele.click()

    def screening(self)->WebElement:
        '''筛选按钮'''
        ele = self.get_clickable_element(self.screening_loc)
        return ele

    def reset_btn(self):
        '''筛选--重置按钮'''
        ele = self.get_clickable_element(self.sc_reset_loc)
        return ele.click()

    def confirm_btn(self):
        '''筛选--确定按钮'''
        ele = self.get_clickable_element(self.sc_confirm_loc)
        return ele.click()

