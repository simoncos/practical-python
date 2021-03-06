from datetime import datetime
from contextlib import ContextDecorator

def timer(func):
    '''Function Level Timer via Decorator'''
    def timed(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        end = datetime.now()
        elapse = (end - start).total_seconds()
        print("Processing time for {} is: {} seconds".format(func.__name__, elapse))
        return result
    return timed

class Timer(object):
    '''Code Block Level Timer via Context'''
    def __enter__(self):
        self.start = datetime.now()
        return self
    def __exit__(self, *args):
        self.end = datetime.now()
        self.elapse = (self.end - self.start).total_seconds()

def timer_(func):
    '''Function Level Timer via Context & with Statement'''
    def timed(*args, **kw):
        with Timer() as t:
            result = func(*args, **kw)
        print("Processing time for {} is: {} seconds".format(func.__name__, t.elapse))
        return result
    return timed

class timer_elegant(ContextDecorator):
    '''Elegant Timer via ContextDecorator'''
    def __init__(self, name):
        self.name = name
    def __enter__(self):
        self.start = datetime.now()
    def __exit__(self, *args):
        self.end = datetime.now()
        self.elapse = (self.end - self.start).total_seconds()
        print("Processing time for {} is: {} seconds".format(self.name, self.elapse))

# Tests

@timer
def test_1(a):
    '''Function Level'''
    a *= 2
    return a

def test_2(a):
    '''Code Block Level'''
    with Timer() as t:
        a *= 2
    print("Processing time for {} is: {} seconds".format('You Name It', t.elapse))
    return a

@timer_
def test_3(a):
    '''Function Level'''
    a *= 2
    return a

@timer_elegant('test_4')
def test_4(a):
    a *= 2
    return a

def test_5(a):
    a *= 2
    return a

if __name__ == '__main__':
    print(test_1(1))
    print(test_2(2))
    print(test_3(3))
    print(test_4(4))

    with timer_elegant('test_5'):
        result_5 = test_5(5)
    print(result_5)