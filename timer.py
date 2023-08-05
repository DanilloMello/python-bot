from threading import Timer
import time
import keyboard

class RepeatTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)

def teste(msg="foo"):
    print(msg)

timer1 = RepeatTimer(2, teste)

timer2 = RepeatTimer(2, teste)

timer1.start()
timer2.start()

def stop()
timer1.cancel()