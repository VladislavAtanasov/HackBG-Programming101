class Fraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator


    def __str__(self):
        if self.denominator == 1:
            return "{}".format(self.numerator)
        elif self.numerator == self.denominator:
            return str(1)
        elif self.numerator == 0:
            return str(0)
        elif self.denominator == 0:
            return "Illegal Math Operation!"
        else:
            return "{} / {}".format(self.numerator, self.denominator)

    def __add__(self, other):
        if self.denominator == other.denominator:
            return Fraction(self.numerator + other.numerator, self.denominator)
        else:
            return Fraction(self.numerator * other.denominator + other.numerator * self.denominator, self.denominator * other.denominator)

    def __sub__(self, other):
        if self.denominator == other.denominator:
            return Fraction(self.numerator - other.numerator, self.denominator)
        else:
            return Fraction(self.numerator * other.denominator - other.numerator*self.denominator, self.denominator * other.denominator)

    def __repr__(self):
        return self.__str__()

    def __eq__(self,other):
        if self.denominator // self.numerator == other.denominator // other.numerator and self.denominator % self.numerator == other.denominator % other.numerator:
            return True
        elif self.numerator == other.numerator and self.denominator == other.denominator:
            return True
        else:
            return False

    def __mul__(self, other):
        newnum = self.numerator * other.numerator
        newden = self.denominator * other.denominator
        for x in range(2, max(newnum, newden)):
            while newnum % x == 0 and newden % x == 0:
                newnum /= x
                newden /= x
        return Fraction(newnum, newden)

a = Fraction(2, 8)
b = Fraction(2, 4)

print(a == b) # True
print(a + b) # 1
print(a - b) # 0
print(a * b) # 1 / 4
