import logging

# 配置日志
logging.basicConfig(level=logging.DEBUG,
                    filename='homework.log')

computer = 7
# 请在下方写你的代码
user = int(input("请输入一个整数:"))

logging.info('user:%s' % user)

