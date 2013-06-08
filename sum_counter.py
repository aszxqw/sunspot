import os
import global_define
import time
import datetime
from pycommon.pypickle import pickle_dump, pickle_load
from pycommon.pylogger import logger
from parser import Parser
from counter_interface import CounterInterface
from counter_base import CounterBase


class SumCounter(CounterBase, CounterInterface):
    def __init__(self, name, keys, regexs):
        CounterBase.__init__(self)
        CounterInterface.__init__(self)

        self.__name = name
        self.__keys = tuple(keys)
        self.__regexs = tuple(regexs)
        #self.__table_name = table_name
        #self.__colnames = tuple(schema_list)
        
        self.__parser = Parser(self.__regexs)

        self.__dict = {}
        for key in  self.__keys:
            self.__dict.setdefault(key, 0)

    def _count_line(self, _list):
        for i, _val in enumerate(_list):
            _key = self.__keys[i]
            if _val == True:
                self.__dict[_key] += 1

    def call_counter(self, lines):
        for line in lines:
            _list = self.__parser.parse_line(line)
            if _list:
                self._count_line(_list)
            else:
                logger.error('parse line [%s] error' %line)

        file_path = os.path.join(
            global_define.options["pickle_dir"], 
            self.__name + global_define.options["date"]
        )
        self.dump(file_path)
        logger.debug("parse file[%s] finished ." %file_path)

if __name__ == '__main__':
    sumcounter = SumCounter("testsumcounter", "ip", "^.")
    sumcounter.call_counter(open("./logs/log.20130423081001.10000", "r"))
    pass
