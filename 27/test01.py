# 在下方写你的代码：导入logging模块
import logging

# 设置日志等级，日志文件名
logging.basicConfig(level=logging.DEBUG,
    filename='${time}.log')


# 日志打印info级别的信息
logging.info('info message')

# 日志打印warning级别的信息
logging.warning('warning message')
