import os

"""
# loggerV1
"""

# def write_log(level, msg):
#     with open(f"""{os.getcwd()}
#     +/log/test_log1.log""", "a") as log_file:
#     log_file.write("[{0}] {1}\n".format(level, msg))

# def critical(msg)    :
#     write_log('CRITICAL', msg)

# def error(msg):
#     write_log('ERROR', msg)

# def warn(msg):
#     write_log('WARN', msg)

# def info(msg):
#     write_log('INFO', msg)

# def debug(msg):
#     write_log('DEBUG', msg)
    
        
"""
# loggerV2
"""

class Logger(object):
    """
    A file based message logger with the following 
    properties

    Attributes:
        file_name: a string representing the full path
        of the log file to which this logger will write
        its messages
    """
    def __init__(self, file_name):
        """
        Returns a Logger object whose file_name is *file_name*
        """
        self.file_name = file_name

    def _write_log(self, level, msg):
        """
        writes a message to the file+Name for a specific
        Logger instance
        """
        # try:
        #     with open(self.file_name, "a+") as log_file:
        #         log_file.write("[{0}] {1}".format(level, msg))
        # except:
        #     print('file not created')
        with open(self.file_name, "a") as log_file:
            log_file.write("\n[{0}] {1}".format(level, msg))

        
        
    def critical(self, msg):
        self._write_log('CRITICAL', msg)
    
    def error(self, msg):
        self._write_log('ERROR', msg)
    
    def warn(self, msg):
        self._write_log('WARN', msg)
    
    def info(self, msg):
        self._write_log("INFO", msg)

    def debug(self, msg):
        self._write_log('DEBUG', msg)