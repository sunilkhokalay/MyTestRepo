class ComplexMath(object):
    '''
    This class represent complex numbers
    '''
    def __init__(self, realpart, imaginarypart):
        self.x = realpart
        self.y = imaginarypart

    def __add__(self, other):
        return ComplexMath(self.x+other.x,self.y+other.y)

    def __sub__(self, other):
        return ComplexMath(self.x + other.x, self.y + other.y)

    def __str__(self):
        if self.y < 0:
            return "{}-j{}".format(self.x,self.y)

    def __repr__(self):
        return "ComplexMath({},{})".format(self.x,self.y)

