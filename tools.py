#!/usr/bin/python
#-*- coding:utf8 -*-

from pycommon.mysql_client import MysqlClient
from pycommon.pyconfig import Config
import global_define

config = Config()
config.init(global_define.CONFIG_FILE_NAME)

db_client = MysqlClient(
    config.get("mysql_host"),
    config.get("mysql_user"),
    config.get("mysql_passwd"),
    config.get("mysql_db")
)
