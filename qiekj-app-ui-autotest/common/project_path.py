# -*- coding: utf-8 -*-
# @Time    : 2020/1/9 11:36
# @Author  : Stephen
# @Email   : jacstephen@163.com
# @File    : project_path.py
# @Software: PyCharm

import os

#获取当前文件的路径
real_path = os.path.realpath(__file__)
# print(real_path)

#截取项目路径
project_path = os.path.split(os.path.split(real_path)[0])[0]
# print('project:',project_path)

#配置文件路径
conf_path = os.path.join(project_path,"config","test_conf.conf")
# print('conf:',conf_path)

#用例路径 test&online
test_cases = os.path.join(project_path,"test_cases","test")
online_cases = os.path.join(project_path,'test_cases','online')

#测试结果文件
result_path = os.path.join(project_path,"test_results")

#报告文件
report_path = os.path.join(result_path,"test_report","test_result.html")
# print('report:',report_path)

#日志文件
log_path = os.path.join(result_path,"test_log","test_log.log")
# print('log:',log_path)


