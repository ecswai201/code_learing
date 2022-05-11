"""
-------------------------------------------------------------------------------
Revision:    1.0
Date:        2022-05-12
Author:      ying.xue
Description:
预置条件：
测试步骤：
预期结果
Modifier：
Modifytime：
Description of Modify：
Email:      ying.xue@unisoc.com
-------------------------------------------------------------------------------
"""


import sys
from datetime import datetime
import os.path

from loguru import logger


class Log():
    """
    Log类是对loguru中的logger的简单封装

    """
    def __init__(self, scriptname=__file__, device='',
                 logpath='',  flevel='DEBUG', clevel='DEBUG'):
        self.logger = logger
        self.device = str(device)

        # 创建log路径
        basedir = os.path.dirname(scriptname)
        name = os.path.basename(scriptname).rstrip('.py')
        now = datetime.now()
        datestr = now.strftime('%Y_%m_%d_%H_%M_%S')
        logdir = os.path.join(basedir, "logTraces", name)
        if logpath == '':
            self.logpath = os.path.join(logdir, f'{datestr}.log')
        else:
            self.logpath = os.path.join(logpath, f'{datestr}.log')
        self.logger.remove()
        self.logger.add(self.logpath,
                        format='{time:YYYY-MM-DD HH:mm:ss.SSS}|'
                               '{name}:{function}:line:'
                               '{line}|{level}:[%s  {message}]' % (
                               device),
                        level=flevel)
        self.logger.add(sys.stdout,colorize=True,
                        format='<g>{time:YYYY-MM-DD HH:mm:ss.SSS}</g>|'
                               '{name}:{function}:line:{line}|<c><bold>{level}'
                               ' {level.icon}'
                               '</bold></c>|<r>%s:{message}</r>' % (device),
                        level=clevel)

        self.debug = logger.debug
        self.info = logger.info
        self.error = logger.error
        self.critical = logger.critical
        self.warning = logger.warning
        self.success = logger.success
        # self.log = logger.info

    def log(self, params, level="info"):
        """可以设定log级别的log方法

        :param params: log内容
        :param level: log级别
        :return:
        """
        if level == "info":
            self.info(params)
        elif level == "debug":
            self.debug(params)
        elif level == "warning":
            self.warning(params)
        elif level == "error":
            self.error(params)
        elif level == "critical":
            self.critical(params)
        elif level == "success":
            self.success(params)

if __name__ == '__main__':
    logobj = Log(device='UMS512T4T573345')
    logobj.log('Open Wi-Fi')
    logobj.debug('Wi-Fi 已打开')
    logobj.critical('Close Wi-Fi')
    logobj.warning('Wi-Fi 已连接')
    logobj.success('Wi-Fi 已断开')
    # new_level = logger.level("SNAKY", no=38,color="<yellow>",icon='🐍')
    #
    # logobj.log('SNAKY',"Here we go!")
