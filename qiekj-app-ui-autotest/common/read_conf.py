# -*- coding: utf-8 -*-
# @Time    : 2019/7/9 14:49
# @Author  : Stephen
# @Email   : mat_wu@163.com
# @File    : read_conf.py
# @Software: PyCharm

from configparser import ConfigParser

class ReadConf:
    '''读取配置文件中的信息
    以不同目标的类型进行区分：
    str,int,float,bool,data
    返回目标字段的值'''

    def __init__(self,filename):
        '''
        :param filname:目标文件路径
        '''
        self.cf = ConfigParser()
        self.cf.read(filename, encoding="utf-8")

    def read_int(self,section,option):
        '''读取整型目标并返回值'''
        return self.cf.getint(section,option)

    def read_float(self,section,option):
        '''读取float值目标并返回值'''
        return self.cf.getfloat(section,option)

    def read_bool(self,section,option):
        '''读取bool目标并返回值'''
        return self.cf.getboolean(section,option)

    def read_data(self,section,option):
        '''读取其它类型(dict,list,tup)数据并返回值'''
        return eval(self.cf.get(section,option))

    def read_str(self,section,option):
        return self.cf.get(section,option)

if __name__ == '__main__':
    pass