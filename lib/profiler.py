import time


def time_profile(function):
    def inner(*args, **kwargs):
        t1 = time.time()
        ret_value = function(*args, **kwargs)
        t2 = time.time()
        print(t2-t1, "seconds")
        return ret_value
    return inner

