import time

def timer(interval, timesInput = -1):
    def outer_wrap(function):
        def wrap(*args, **kwargs):
            times = True if (timesInput == 0) else timesInput
            function(*args, **kwargs)
            i = 1
            while i != times:
                time.sleep(interval)
                function(*args, **kwargs)
                i += 1
        return wrap
    return outer_wrap