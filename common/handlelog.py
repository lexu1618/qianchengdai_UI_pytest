"""
================================
Author：樵夫
Time：2020/3/31    14:54
================================
"""
import os
import logging
from common.handlepath import LOGS_PATH
from common.handleconfig import config


class HandleLog():

    def __init__(self, filename):
        self.filename = filename

    def write_log(self):
        log = logging.getLogger("logs")
        log.setLevel("DEBUG")
        sh = logging.StreamHandler()
        sh.setLevel("DEBUG")
        log.addHandler(sh)
        fh = logging.FileHandler(self.filename, encoding="utf8")
        fh.setLevel("DEBUG")
        log.addHandler(fh)
        formats = '%(asctime)s -- [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s'
        form = logging.Formatter(formats)
        sh.setFormatter(form)
        fh.setFormatter(form)
        return log


log = HandleLog(os.path.join(LOGS_PATH, config.get("log", "filename")))
log = log.write_log()

if __name__ == '__main__':
    log.error("error")
    log.info("info")
    log.debug("debug")
    log.warning("warning")
    log.critical("critical")
