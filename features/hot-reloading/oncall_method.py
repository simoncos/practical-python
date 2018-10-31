import time
from functools import lru_cache

from utils import change_conf_file

class Getter:
    @staticmethod
    @lru_cache(1)
    def getModel():
        with open('config.txt') as f:
            model = f.read()
        return model

class Model():
    def log(self):
        self.model = Getter.getModel()
        print(self.model)

if __name__ == '__main__':
    # Reload only when cache_clear() is called
    model = Model()
    while True:
        model.log()
        time.sleep(2)
        change_conf_file() # change data
        Getter.getModel.cache_clear()
        print('Cache cleared, reloading config...')
        model.log()
