import os
import global_define
import tools

from parser import Parser
from pycommon.pylogger import logger
from pycommon.utilities import dicts_merge
from pycommon.pypickle import pickle_dump, pickle_load
from counter_base import CounterBase
from counter_interface import CounterInterface

class UniqSumCounter(CounterBase, CounterInterface):
    def __init__(self, name, keys, regexs):
        CounterBase.__init__(self)
        CounterInterface.__init__(self)
        
        self.__name = name
        self.__keys = tuple(keys)
        self.__regexs = tuple(regexs)

        self.__parser = Parser(self.__regexs)

        self.__dict = {}
        for key in self.__keys:
            self.__dict.setdefault(key, {})
        
    def call_counter(self, lines):
        for line in lines:
            _list = self.__parser.parse_line(line)
            if _list:
                self._count_line(_list)
            else:
                logger.error('parse line [%s] error' %line)
        file_path = os.path.join(
            global_define.options["pickle_dir"], 
            "%s_%s" %(self.__name, global_define.options["date"])
        )
        pickle_dump(self.__dict, file_path)
        logger.debug("parse file[%s] finished ." %file_path)

    def _count_line(self, _list):
        for i, _val in enumerate(_list):
            _key = self.__keys[i]
            if _val is not None:
                self.__dict[_key].setdefault(_val, 0)
                self.__dict[_key][_val] += 1

if __name__ == '__main__':
    s = UniqSumCounter("testusc", ('dp_query', 'tip', 'tip_tbres'), ('GET /brwext/dp_query/', 'GET /brwext/tip/', 'GET /brwext/tip_tbres/'))
    s.call_counter(open("logs/log.20130423081001.10000", "r"))
