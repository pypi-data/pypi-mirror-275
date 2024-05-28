#TEST FILE
import sys
import os
sys.path.append("./traceUts")
from traceUts import *
import traceUts

traceUts.CallBack = lambda x:print(x)

@traceMap(main=True)
def soma(a,b):
    return a/b


res = soma(1,0)


a  =1






