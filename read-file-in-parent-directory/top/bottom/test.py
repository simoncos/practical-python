from os.path import dirname, abspath

print('test results:')
print(__file__)
print(dirname(__file__))
print(abspath(__file__))
print(dirname(abspath(__file__)))
print(dirname(dirname(abspath(__file__))))
print('---')
print('方法2:')
print(dirname(dirname(abspath(__file__))) + '/b.txt') # 方法2
print('方法3:')
print(dirname(abspath(__file__)) + '/../b.txt') # 方法3
