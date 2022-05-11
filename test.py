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

from common.log import Log
class Test():
    def __init__(self, device='', logobj=None):
        if logobj is None:
            self.logobj = Log(scriptname=__file__, device=device)
        else:
            self.logobj = logobj

        self.logobj.success('aaaaa')

    def setup(self):
        self.logobj.info('=======initial=======')
if __name__ == '__main__':
    test = Test()
    test.setup()