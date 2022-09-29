import logging
from mylib import do_something

def f():
    logging.basicConfig(
        filename="otherfiles/20220414.log",
        filemode="w",
        level=logging.DEBUG
    )
    logging.info("begin...")
    do_something()
    logging.info("end...")

if __name__ == "__main__":
    f()