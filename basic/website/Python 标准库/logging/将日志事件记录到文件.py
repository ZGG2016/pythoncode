import logging


def log_file():
    # logging.basicConfig(filename="20220414.log",level=logging.DEBUG)  # 追加写
    # logging.basicConfig(filename="20220414.log",filemode="w",level=logging.DEBUG) # 覆盖写
    logging.basicConfig(
        filename ="otherfiles/20220414.log",
        filemode = "w",
        # 时间、代码所在文件名、代码行号、日志级别名字、日志信息
        format = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
        # 控制日期/时间的格式
        datefmt = '%Y:%m:%d %H:%M:%S',
        level = logging.DEBUG)

    logging.debug("this is a logging debug")
    logging.info("this is a logging info")
    logging.warning("this is a logging warning")
    logging.error("this is a logging error")


log_file()