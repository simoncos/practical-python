from os.path import dirname, abspath

# 方法1
# path = '../b.txt'

# 方法2
# path = dirname(dirname(abspath(__file__))) + '/b.txt'

# 方法3
path = dirname(abspath(__file__)) + '/../b.txt'

print('path:', path)
with open(path) as f:
   print(f.read())
