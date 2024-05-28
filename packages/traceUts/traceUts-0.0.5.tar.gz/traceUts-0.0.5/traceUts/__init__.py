from functools import wraps
import json
import inspect
import copy
import os
import sys
import time

ERROR_ROBOT=       3
ERROR_PROCESS=     4
SUCESS=            2

CallBack = None


class error():
    def __init__(self):
        self.ec_timeout    =1
        self.ec_unmaped    =3
        self.ec_process    =4
        self.ec_offline    =6
        self.ec_api        =5
        self.ec_success    =2
        self.err = [getattr(self, attr) for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("__")]

class Trace(error):
    def __init__(self):
        super().__init__()
        self.Status = None
        self.Message = ""
        self.Value = None
        self.Story = []
        self.Excpt = ""
        self.Type = True  #True para erro de robo
        self.ErrorNum = 6
        self.htmlFile = os.path.dirname(os.path.abspath(__file__)) + "\\TraceHtml.txt"

    def error(self,msg = None,vl = None,tp = None,exp=None,er_num=0):
        self.Status     = False
        self.Message    = msg if not msg is None else "" #) + f" at step {inspect.stack()[1][3]}"
        self.Value      = vl
        self.Story      = [inspect.stack()[1][3]]
        self.Type       = tp
        self.Excpt      = exp if not exp is None else self.Message
        self.ErrorNum   = self.ec_unmaped if not er_num or not er_num in self.err else er_num
        return copy.copy(self)

    def back(self,functionName = inspect.stack()[1][3]):
        self.Story.append(functionName)
        return copy.copy(self)

    def excpt(self,msg = None,vl = None,tp=True,er_num=None,functionName=inspect.stack()[1][3]): #usado depois do except
        self.Status     = False
        self.Message    = msg if not msg is None else f"error at '{functionName}' step!"
        self.Value      = vl
        self.Story      = [functionName]
        self.Type       = tp
        #self.Excpt      = traceback.format_exc()
        self.Excpt      = str(sys.exc_info()[1])
        self.ErrorNum   = self.ec_unmaped if not er_num or not er_num in self.err else er_num
        return copy.copy(self)
    
    def success(self,msg = "OK",vl = None):
        self.Status     = True
        self.Message    = msg
        self.Value      = vl
        self.Story      = []
        self.Type       = None
        self.Excpt      = None
        self.ErrorNum   = self.ec_success
        return copy.copy(self)


    def __repr__(self):
        ret = {
            "Status":   self.toString(self.Status),
            "Message":  self.toString(self.Message),    
            "Value":    self.toString(self.Value),      
            "Story":    self.toString(self.Story),      
            "Type":     self.toString(self.Type),       
            "Expt":     self.toString(self.Excpt),
            "ErrorNum": self.toString(self.ErrorNum)      
        }
        return json.dumps(ret)
        #return json.dumps(self.toJSON())

    def rep(self):
        return self.__repr__()
        dic = {}
        for k in self.__dict__:
            if not "__" in k:
                dic[k] = getattr(self,k)
        return str(dic)

    def toJSON(self):
        jsn = json.loads(json.dumps(self, default=lambda o: o.__dict__, sort_keys=True))
        del jsn["htmlFile"]
        return jsn

    def toString(self,obj):
        if obj == None :                                                        return "None"
        if type(obj) == list or type(obj) == dict:                              return json.dumps(obj)
        if True in [isinstance(obj,x) for x in [int, float, complex,tuple,str]]:return str(obj)
        return "Not suported"
    
    def __add__(self,value):
        return value + self.Value
    def __sub__(self,value):
        return self.Value - value
    def __bool__(self):
        return self.Status
    def __eq__(self,value):
        return self.Value == value
    def __gt__(self,value):
        return self.Value > value
    def __lt__(self,value):
        return self.Value < value
    def __ge__(self,value):
        return self.Value >= value
    def __le__(self,value):
        return self.Value <= value
    def __ne__(self,value):
        return self.Value != value
    def __str__(self):
        return str(self.Value)
    def __iter__(self):
        self.n = 0
        return self
    def __next__(self):
        tp = isinstance(self.Value,dict)

        if self.n < len(self.Value):
            result = self.Value[self.n] if not tp else list(self.Value.keys())[self.n]
            self.n += 1
            return result
        else:
            raise StopIteration
    
    def __getitem__(self,value):
        return self.Value[value]

class TraceError(Exception):
    def __init__(self,rsp:Trace):
        self.rsp = rsp


def traceMap(main=False):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            try:
                rsp = Trace()
                funcName = function.__name__
                data = {"func_name":funcName,"status":"SUCCESS","message":"START","time":0}
                start = time.time()
                if CallBack:CallBack(data)
                ret = function(*args, **kwargs)
                end = time.time()
                
                if isinstance(ret,Trace):
                    if ret:
                        data = {"func_name":funcName,"status":"SUCCESS","message":"FINISH","time":end - start}
                        if CallBack:CallBack(data)
                        return ret
                    else:
                        if ret.Story[-1] == funcName:
                            raise TraceError(ret)
                        raise TraceError(ret.back(functionName = funcName))
                else:
                    data = {"func_name":funcName,"status":"SUCCESS","message":"FINISH","time":end - start}
                    if CallBack:CallBack(data)
                    return ret

            except TraceError as err:
                end = time.time()
                data = {"func_name":funcName,"status":"FAILURE","message":err.rsp.Excpt,"time":end - start}
                if CallBack:CallBack(data)
                if main: return
                raise TraceError(err.rsp.back())
            
            except:
                end = time.time()
                data = {"func_name":funcName,"status":"FAILURE","message":str(sys.exc_info()[1]),"time":end-start}
                if CallBack:CallBack(data)
                if main: return
                raise TraceError(rsp.excpt(functionName = funcName))

        return wrapper
    return decorator



