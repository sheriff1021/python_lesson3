import psutil
import datetime
import time
import psutil_reader
from config_reader import config_reader
from result_writter import writter,conf_analyze
from psutil_reader import system_data_reader
while True:
    bab=system_data_reader()
    krak=conf_analyze().analyze(bab.result)
    ins=config_reader()
    time.sleep(ins.time)