import logging

logger = logging.getLogger("handlers-example")
logger.setLevel(logging.DEBUG)

sh1 = logging.StreamHandler()  # 到控制台
sh1.setLevel(logging.ERROR)

sh2 = logging.FileHandler("otherfiles/20220414.log")  # 到日志文件
sh2.setLevel(logging.INFO)

fmt = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
sh1.setFormatter(fmt)
sh2.setFormatter(fmt)

logger.addHandler(sh1)
logger.addHandler(sh2)

logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')