
# File: logger.py
#
# Create Loggable and Logger classes for logging activities 
# of objects

############

class Loggable:
    def activity(self):
        return "This needs to be overridden locally";

class Logger:
    
    def __init__(self,logfilename='logger.dat'):
        self._log= open(logfilename,'a');
        
    def log(self, loggedObj):
        self._log.write(loggedObj.activity() +'\n');
        
    def __del__(self):
        self._log.close();
    