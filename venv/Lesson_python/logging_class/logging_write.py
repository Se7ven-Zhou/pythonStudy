# coding:utf-8

import logging
import os
import time



current_path = os.getcwd()
file_name = time.strftime("%Y-%m-%d")+".txt"
file_path = os.path.join(current_path,file_name)

logger = logging.getLogger("python_info")
fh = logging.FileHandler(file_path)
logger.addFilter(fh)


if os.path.exists(file_path):
    file = open(file_path,"a")


    file.close()