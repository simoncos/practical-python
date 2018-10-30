import random

def change_conf_file():
    '''Simulate parameter update in config file'''
    with open('config.txt', 'w') as f:
        f.write('parameter: {}'.format(random.random()))

if __name__ == '__main__':
    change_conf_file()