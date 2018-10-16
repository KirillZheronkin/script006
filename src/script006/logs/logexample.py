import logging

def get_configured_logger():
    logFormatter = logging.Formatter("%(asctime)s %(name)s:%(levelname)s:: %(message)s")
    logger = logging.getLogger(__name__)
    fh = logging.FileHandler("logfile.log")
    fh.setFormatter(logFormatter)
    logger.addHandler(fh)
    sh = logging.StreamHandler()
    sh.setFormatter(logFormatter)
    logger.addHandler(sh)
    logger.setLevel(logging.DEBUG)
    return logger

if __name__ == '__main__':
    l = get_configured_logger()
    l.info("Testing log messages")