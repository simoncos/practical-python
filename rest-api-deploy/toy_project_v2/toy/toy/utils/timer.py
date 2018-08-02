from datetime import datetime

from toy.utils.logger import LoggerFactory

# def timeit(func):
#     def timed(*args, **kw):
#         log = LoggerFactory.getDebugLogger()
#         with Timer() as t:
#             result = func(*args, **kw)
#         if 'docid' in result:
#             log.info("docid:{}, Processing time for {} is: {}".format(result['docid'], func.__name__, t.elapse))
#         else:
#             log.info("Processing time for {} is: {}".format(func.__name__, t.elapse))
#         return result
#     return timed

class Timer(object):

    def __enter__(self):
        self.start = datetime.now()
        return self

    def __exit__(self, *args):
        self.end = datetime.now()
        self.elapse = (self.end - self.start).total_seconds()

def a(b):
    return b

if __name__ == '__main__':
    with Timer():
        print(a(1))