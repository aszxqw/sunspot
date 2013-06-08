import pickle
import os
import global_define
import time
import datetime

class CounterBase:
    def __init__(self):
        pass

    def dump(self, file_path):
        pickle_dump(self.__dict, file_path)

    """
    def _insert(self, _table_name, _schema_list, _value_list, _log_day):

        key_str = 'log_day'
        for key_name in _schema_list:
            key_str += ', `%s`' %key_name

        value_str = '"%s"' %_log_day
        for value in _value_list:
            value_str += ', "%s"' %value

        sql = 'insert into %s (%s) values (%s)' %(_table_name, key_str, value_str)

        db_client.insert(sql)
        logger.debug('insertdb sql[%s] finished.' %sql)
    """


if __name__ == '__main__':
    pass
