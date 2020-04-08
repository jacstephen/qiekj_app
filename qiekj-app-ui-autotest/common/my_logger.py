# -*- coding: utf-8 -*-
# @Time    : 2020/1/9 11:13
# @Author  : Stephen
# @Email   : jacstephen@163.com
# @File    : my_logger.py
# @Software: PyCharm

import logging
from common.project_path import log_path,conf_path
from common.read_conf import ReadConf


class MyLogger:
    '''设置日志记录'''
    def __init__(self):
        pass

    def my_logger(self,level,msg):
        '''自定义日志系统'''

        #创建一个日志收集器
        my_logger = logging.getLogger('my_logger')
        my_logger.setLevel('INFO') #设置收集器的setLevel()

        #设置日志的输出格式
        formatter = logging.Formatter('[%(asctime)s]-'
                              '[%(levelname)s]-'
                              '[line:%(lineno)d]-'
                              '[日志信息]:%(message)s')

        #设置输出渠道
        sh = logging.StreamHandler() #创建一个输出到控制台的渠道
        sh.setLevel('INFO') #设置渠道级别
        sh.setFormatter(formatter)

        #输出日志到对应文件
        fh= logging.FileHandler(log_path,encoding='utf-8')
        fh.setLevel('INFO')
        fh.setFormatter(formatter)

        #渠道、日志收集器进行对接
        my_logger.addHandler(sh)
        my_logger.addHandler(fh)

        if level.upper() == "INFO":
            my_logger.info(msg)
        elif level.upper() == 'DEBUG':
            my_logger.debug(msg)
        elif level.upper() == 'WARNING':
            my_logger.warning(msg)
        elif level.upper() == 'ERROR':
            my_logger.error(msg)
        else:
            my_logger.critical(msg)

        my_logger.removeHandler(fh)
        my_logger.removeHandler(sh)

    def debug(self, msg):
        self.my_logger("DEBUG", msg)

    def info(self, msg):
        self.my_logger("INFO", msg)

    def warning(self, msg):
        self.my_logger("WARNING", msg)

    def error(self, msg):
        self.my_logger("ERROR", msg)

    def critical(self, msg):
        self.my_logger("CRITICAL", msg)

if __name__ == '__main__':
    res = MyLogger()
    res.info('abc')


