import pulseio
import time
class RGB:
    kind = "color"  # class variable shared by all instances

    def __init__(self, r, g, b):           #sets a value for all duty cycle to follow
        self.r = pulseio.PWMOut(r, frequency=5000, duty_cycle=0)
        self.g = pulseio.PWMOut(g, frequency=5000, duty_cycle=0)
        self.b = pulseio.PWMOut(b, frequency=5000, duty_cycle=0)

    def red(self):
        self.r.duty_cycle = 0
        self.g.duty_cycle = 2**16-1
        self.b.duty_cycle = 2**16-1

    def green(self):
        self.r.duty_cycle = 2**16-1
        self.g.duty_cycle = 0
        self.b.duty_cycle = 2**16-1

    def blue(self):
        self.r.duty_cycle = 2**16-1
        self.g.duty_cycle = 2**16-1
        self.b.duty_cycle = 0

    def cyan(self):
        self.r.duty_cycle = 2**16-1
        self.g.duty_cycle = 0
        self.b.duty_cycle = 0

    def magenta(self):
        self.r.duty_cycle = 0
        self.g.duty_cycle = 2**16-1
        self.b.duty_cycle = 0

    def yellow(self):
        self.r.duty_cycle = 0
        self.g.duty_cycle = 0
        self.b.duty_cycle = 2**16-1

    def rainbow(self):
        self.r.duty_cycle = 0
        self.g.duty_cycle = 2**16-1
        self.b.duty_cycle = 2**16-1
        for val in range(0,2**16,64):
            #red
            self.r.duty_cycle = val
            self.g.duty_cycle = 2**16-1-val
            self.b.duty_cycle = 2**16-1
            time.sleep(.01)
        for val in range(0,2**16,64):
            #green
            self.r.duty_cycle = 2**16-1
            self.g.duty_cycle = val
            self.b.duty_cycle = 2**16-1-val
            time.sleep(.01)
        for val in range(0,2**16,64):
            #blue
            self.r.duty_cycle = 2**16-1-val
            self.g.duty_cycle = 2**16-1
            self.b.duty_cycle = val
            time.sleep(.01)