"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, num):
        self.ogNum = num
        self.num = num

    def serial(self):
        self.num += 1
    
    def reset(self):
        self.num = self.ogNum


ser = SerialGenerator(5)
print(ser.num)
ser.serial()
print(ser.num)
ser.reset()
print(ser.num)


        


