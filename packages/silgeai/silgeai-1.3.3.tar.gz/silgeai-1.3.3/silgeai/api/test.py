# -*- coding:utf-8 -*-
"""
@Author: 风吹落叶
@Contact: waitKey1@outlook.com
@Version: 1.0
@Date: 2024/5/27 7:29
@Describe: 
"""
from asrapi import  asr
apikey='sk-1af_sGIZpyrkAZZoKy9ZilNsQYBGRONrvP5jpV86TO0M3jTwhDqN27pPMDKktD'
file='test4.wav'

ret=asr(apikey,file)
print(ret)