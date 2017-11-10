from os.path import dirname, abspath
import os

print('__file__:',__file__)
print('current working directory:', os.getcwd()) # 打印当前工作目录
print(dirname(__file__))
print(abspath(__file__))
print(dirname(abspath(__file__)))
print(dirname(dirname(abspath(__file__))))
