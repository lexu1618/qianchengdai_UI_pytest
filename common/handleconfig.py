"""
================================
Author：樵夫
Time：2020/3/31    14:05
================================
"""
import os
from common.handlepath import CONF_PATH
from configparser import ConfigParser


class HandleConfig(ConfigParser):

    def __init__(self, filename):
        super().__init__()
        self.read(filename, encoding="utf8")
        self.write(fp=(open(filename, "w", encoding="utf8")))


config = HandleConfig(os.path.join(CONF_PATH, "config.ini"))
