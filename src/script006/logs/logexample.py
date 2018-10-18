import logging
import logsettings


# def get_configured_logger(name=__name__):
#     logFormatter = logging.Formatter(logsettings.LOG_FORMAT)
#     logger = logging.getLogger(name)
#     fh = logging.FileHandler(logsettings.LOGFILE)
#     fh.setFormatter(logFormatter)
#     logger.addHandler(fh)
#     sh = logging.StreamHandler()
#     sh.setFormatter(logFormatter)
#     logger.addHandler(sh)
#     logger.setLevel(logsettings.LOGLEVEL)
#     return logger

if __name__ == '__main__':
    # l = get_configured_logger("logexample")
    # l.info("Testing log messages")
    logging.debug("Test log output from logging")
    logging.basicConfig()