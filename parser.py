# -*- coding: utf-8 -*-

import re
from pycommon.pylogger import logger

class Parser:
    def __init__(self, regexs):
        self.__regexs  = tuple(map(lambda x: re.compile(x), regexs))

    def parse_file(self, file_path):
        ret_lists = []
        with open(file_path, "r") as fin:
            for line in fin:
                value_list = self.parse_line(line)
                if value_list:
                    ret_lists.append(value_list)
        return ret_lists

    def parse_line(self, line):
        ret_list = []
        for regx in self.__regexs:
            regx_info = regx.search(line)
            if regx_info:
                if len(regx_info.groups()) == 0:
                    ret_list.append(True)
                elif len(regx_info.groups()) == 1:
                    ret_list.append(regx_info.group(1))
                else:
                    logger.error("regx_info.group's len exceed 1")
                    ret_list.append(None)
            else:
                ret_list.append(None)
        return ret_list
            
if __name__ == '__main__':
    sre = 'search/\?s_product=.*&from=browser'
    a = (sre, __taobao_re_expr)
    p = Parser(a)
    print p.parse_file("logs/log.20130423081001.10000")

    for line in open("logs/log.20130423081001.10000", "r"):
        print line
        print p.parse_line(line)
        raw_input()

