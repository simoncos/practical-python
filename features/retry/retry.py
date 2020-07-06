import time, random

MAXIMAL_RETRY = 3

# Function Method

def run():
    result = random.random() # generate random double from 0 to 1
    if result > 0.3:
        raise Exception(f'Wrong result: {result}')
    else:
        print(f'>> Success')
        return result

def run_with_retry(times=0):
    time.sleep(1)
    try:
        return run()
    except Exception as e:
        if times >= MAXIMAL_RETRY:
            print(f'>> Exceed maximal retry {MAXIMAL_RETRY}, Raise exception...')
            raise(e) # will stop the program without further handling
        else:
            times += 1
            print(f'>> Exception, Retry {times} begins...')
            return run_with_retry(times)

def test_retry_func():
    while True:
        print('\nBegin new run...')
        time.sleep(1)
        result = run_with_retry()
        if result:
            print(f'Get result: {result}')

# Decorator Method

def retry(func, times=0):
    def retried(*args, **kwargs):
        nonlocal times
        time.sleep(1)
        try:
            return func()
        except Exception as e:
            if times >= MAXIMAL_RETRY:
                print(f'>> Exceed maximal retry {MAXIMAL_RETRY}, Raise exception...')
                raise(e) # will stop the program without further handling
            else:
                times += 1
                print(f'>> Exception, Retry {times} begins...')
                return run_with_retry(*args, **kwargs)
    return retried

@retry
def run_decorated():
    result = random.random() # generate random double from 0 to 1
    if result > 0.3:
        raise Exception(f'Wrong result: {result}')
    else:
        print(f'>> Success')
        return result

def test_retry_decorator():
    while True:
        print('\nBegin new run...')
        time.sleep(1)
        result = run_decorated()
        if result:
            print(f'Get result: {result}')

if __name__ == "__main__":
    test_retry_func()
    # test_retry_decorator()
    
