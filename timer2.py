import time, threading

def timer(interval, times = -1):
    def outer_wrap(function):
        def wrap(*args, **kwargs):
            def inner_wrap():
                i = 0
                while i != times:
                    time.sleep(interval)
                    function(*args, **kwargs)
                    i += 1
            threading.Timer(0, inner_wrap).start()
        return wrap
    return outer_wrap

@timer(5,3)
def msg_test(msg):
    print(msg)

msg_test('testando')
