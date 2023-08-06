from threading import Timer

class RepeatebleTimer(Timer):
    def run(self):
        print(self.args)
        if (self.args[0] == 0):
            self.function(*self.args,**self.kwargs)
            while not self.finished.wait(self.interval):  
                self.function(*self.args,**self.kwargs)  
        else:
            i = 1
            self.function(*self.args,**self.kwargs)
            while not self.finished.wait(self.interval) & i != self.args :
                self.function(*self.args,**self.kwargs)
                i += 1
