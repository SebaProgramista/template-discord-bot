import logging
import colorlog
import json

class MessageLogger(logging.Logger):
    MESSAGE_LEVEL = 25
    
    def __init__(self, name):
        super().__init__(name)
        logging.addLevelName(self.MESSAGE_LEVEL, "MESSAGE")
        
    def message(self, msg, *args, **kwargs):
        if self.isEnabledFor(self.MESSAGE_LEVEL):
            self._log(self.MESSAGE_LEVEL, msg, args, **kwargs)
        
logging.setLoggerClass(MessageLogger)

class LoggerManager:
    def __init__(self, debug_mode):
        logger = logging.getLogger(__name__)
        logging_level = logging.DEBUG if debug_mode else logging.INFO
        logger.setLevel(logging_level)
        
        # Use colorlog's formatter
        formatter = colorlog.ColoredFormatter(
            "%(fg_bold_black)s%(asctime)s %(levelname_log_color)s%(levelname)-8.8s%(reset)s %(purple)s%(funcName)s %(reset)s%(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
            secondary_log_colors={
                'levelname': {
                    'ERROR': 'red',
                    'INFO': 'blue',
                    'DEBUG': 'green',
                    'WARNING': 'yellow',
                    'MESSAGE': 'cyan'
                }
            }
        )
        
        consoleHandler = logging.StreamHandler()
        consoleHandler.setFormatter(formatter)
        consoleHandler.setLevel(logging_level)

        logger.addHandler(consoleHandler)

        self.logger = logger