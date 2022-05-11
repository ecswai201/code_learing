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

import platform

from setuptools import setup, find_packages

requires = ["pyserial>=3.4", "uiautomator2", "loguru"]
if platform.system().lower() == 'windows':
    requires.append("pywin32>=224")
    requires.append("pywin32-ctypes>=0.2.0")
setup(
    name="mytest",
    version="1.0",
    author="ying.xue",
    author_email="ecswai@163.com",
    description="Learn to Pack Python Module  ",

    # 项目主页
    # url="http://iswbm.com/",

    # 你要安装的包，通过 setuptools.find_packages 找到当前目录下有哪些包
    packages=find_packages(),
    install_requires = requires,
    python_requires = '>=3.6',
    test_requires = []
)
