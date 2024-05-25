import os, datetime, sqlite3, logging
# import auxiliary_module
from rich import print
DebugLevel = 'DEBUG' # info, 

LogNetPath = "\\\more\\copy\\_log\\"
LocLocPath = "C:/UserScripts/_log/"
Project    = 'OMC_Сustomer'

if os.path.isdir(LogNetPath):
    FileNetMod = f'{LogNetPath}{Project}'
    if not os.path.isdir(FileNetMod):
        os.makedirs(FileNetMod)
    FileNetLog = f'{FileNetMod}\\{str(datetime.date.today())}.txt'
else:
    FileNetLog = None
if os.path.isdir(LocLocPath):
    FileLogMod = f'{LocLocPath}{Project}'
    if not os.path.isdir(FileLogMod):
        os.makedirs(FileLogMod)
    FileLocLog = f'{FileLogMod}/{str(datetime.date.today())}.txt'
#------------------------------------------------------------------------------------------------------------------------------------------
logger = logging.getLogger(Project)
if DebugLevel == 'DEBUG': logger.setLevel(logging.DEBUG)
else: logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s ; %(process)-4x ; %(message)s ; %(funcName)11s ; [%(lineno)4s] ; [%(levelname)7s]", datefmt='%Y-%m-%d %H:%M:%S')
# create file handler which logs even debug messages
if FileNetLog: 
    log_net = logging.FileHandler(FileNetLog)
    log_net.setFormatter(formatter)
    if DebugLevel == 'DEBUG': log_net.setLevel(logging.DEBUG)
    else: log_net.setLevel(logging.INFO)
# create console handler with a higher log level
log_loc = logging.FileHandler(FileLocLog)
if DebugLevel == 'DEBUG': log_loc.setLevel(logging.DEBUG)
else: log_loc.setLevel(logging.INFO)
# create formatter and add it to the handlers

log_loc.setFormatter(formatter)
# add the handlers to the logger
if FileNetLog: logger.addHandler(log_net)
logger.addHandler(log_loc)
logger.info('---------------------------------------------------------------------------------------------------------')

# a = auxiliary_module.Auxiliary()
logger.info('created an instance of auxiliary_module.Auxiliary')
logger.info('calling auxiliary_module.Auxiliary.do_something')
# a.do_something()
logger.info('finished auxiliary_module.Auxiliary.do_something')
logger.info('calling auxiliary_module.some_function()')
# auxiliary_module.some_function()
logger.info('done with auxiliary_module.some_function()')


# ------------------------------------------------------------------------------------------------------
if __name__ == '__main__':

    pass
else: # ------------------------------------------------------------------------------------------------------
    pass
