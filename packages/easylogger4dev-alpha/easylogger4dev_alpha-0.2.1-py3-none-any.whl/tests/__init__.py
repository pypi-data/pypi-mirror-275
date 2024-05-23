from easylogger4dev_alpha import *


@log4csv("测试")
def function_without_return():
    pass


@log4csv("测试")
def function_with_return():
    return "函数被执行"


@log4excel("测试")
def function_without_return2():
    pass


@log4excel("测试")
def function_with_return2():
    return "函数被执行"


if __name__ == '__main__':
    logger_ini()
    function_without_return()
    function_with_return()
    function_with_return2()
    function_without_return2()
