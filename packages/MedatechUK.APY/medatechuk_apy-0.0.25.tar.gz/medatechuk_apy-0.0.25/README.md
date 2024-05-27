# Python API

## About

A Python package of common EDI functions.

## Install

To install this package use:
```
pip install MedatechUK.APY
```

## Imports

### [Logging Class](https://github.com/MedatechUK/Medatech.APY/blob/main/docs/log.md "Logging Class")

A class to create log files.

```python
from MedatechUK.mLog import mLog

log = mLog()
log.start( os.getcwd(), "DEBUG" )
log.logger.debug("Starting {}".format(__file__)) 

```

### [Config Class](https://github.com/MedatechUK/Medatech.APY/blob/main/docs/oDataConfig.md "Config Class")

A class for managing oData settings.

```python
from MedatechUK.oDataConfig import Config

c = Config(	                 # Using this configuration
    env="wlnd" ,    	     # the Priority environment
    path=os.getcwd()    	 # the location of the config file
)

```

### [Command Line Arguments](https://github.com/MedatechUK/Medatech.APY/blob/main/docs/cl.md "Command Line Arguments")

A package of command line tools, including parsing the [sys.argv](https://docs.python.org/3/library/sys.html "sys.argv") function in Python.

```
progname.exe -arg value -arg2 "value two"
```

```
arg.byName(['arg','a']) = "value"
arg.byName(['arg2','a2']) = "value two"
arg.byName(['arg3','a3']) = None
```

### [Serial Class](https://github.com/MedatechUK/Medatech.APY/blob/main/docs/serial.md "Serial Class")

A package for working with serial data.

See also: [Serial object methods](https://github.com/MedatechUK/Medatech.APY/blob/main/docs/serialmethod.md "Serial object methods")

```python
from MedatechUK.Serial import SerialBase , SerialT , SerialF

# Load an Order from json file
with open('test.json', 'r') as the_file:        
    q = order(json=the_file)
    # Save to xml
    q.toFile('test2.xml', q.toXML, root="root")
	
```

### [APY Class](https://github.com/MedatechUK/Medatech.APY/blob/main/docs/apy.md "APY Class")

A class for handling HTTP Request/Response.

See Also: the [http transport example](https://github.com/MedatechUK/Medatech.APY/blob/main/transport/web "http Transport")

```python
from MedatechUK.apy import Request , Response

def ProcessRequest(request) :
    log = mLog()
    try:
        q = order(**request.data)            
        q.toPri(
            Config(
                env=request.environment , 
                path=os.getcwd()
            ) , 
            q.toFlatOdata, 
            request=request 
        )        
    
    except Exception as e:
        log.logger.critical(str(e))
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]        
        request.response.Status = 500
        request.response.Message = "Internal Server Error"
        request.response.data ={ "error" :
            {
                "type": exc_type,
                "message": str(e),
                "script": fname,
                "line": exc_tb.tb_lineno
            }
        } 
```

### [AppSvc Class](https://github.com/MedatechUK/Medatech.APY/blob/main/docs/svc.md  "AppSvc Class")

This package contains a debug-able inheritable Windows Service.

```python
class MySVC(AppSvc):    
    _svc_name_ = "testSVC"
    _svc_display_name_ = "Test Service"    

    def __init__(self , args):    
        self.Main = MySVC.main   
        self.Init = MySVC.init   
        self.Folder = Path(__file__).parent         
        AppSvc.__init__(self , args)

    def init(self):
        if self.debuginit: debugpy.breakpoint() # -debug init
        # Do servce setup

    def main(self):       
        if self.debug: debugpy.breakpoint # -debug          
        
        # Main service    
        self.log.logger.debug(self.clArg.byName(['env','e']))

if __name__ == '__main__':    
    win32serviceutil.HandleCommandLine(MySVC)    

```  

### [EPDM Class](https://github.com/MedatechUK/Medatech.APY/blob/main/docs/epdm.md "EPDM Class")

A package for working with EPDM (Solid Works) serial data.

See Also: [Making the EPDM example executable](https://github.com/MedatechUK/Medatech.APY/blob/main/transport/cl "Command Line Transport").

See Also: [Running the EPDM executable from a service](https://github.com/MedatechUK/Medatech.APY/blob/main/transport/service "Service Transport")

```python
from MedatechUK.epdm import xmlTransactions

# Load an EPDM file.
try:
    with open('example.xml', 'r') as the_file:        
        q = xmlTransactions(_xml=the_file)
        for t in q.transactions:
            recurse(t.document)

except Exception as e:
    log.logger.critical(str(e))
	
```