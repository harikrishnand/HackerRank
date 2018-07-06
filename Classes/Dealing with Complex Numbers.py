class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, no):
        rel = self.real + no.real
        img = self.imaginary + no.imaginary
        return Complex(rel,img)
    def __sub__(self, no):
        return Complex(self.real - no.real,self.imaginary - no.imaginary)
        
    def __mul__(self, no):
        mul = complex(self.real,self.imaginary)* complex(no.real,no.imaginary)
        return Complex(mul.real,mul.imag)

    def __truediv__(self, no):
        tdiv = complex(self.real,self.imaginary)/ complex(no.real,no.imaginary)
        return Complex(tdiv.real,tdiv.imag)

    def mod(self):
        return Complex(abs(complex(self.real,self.imaginary)),0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result
if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
