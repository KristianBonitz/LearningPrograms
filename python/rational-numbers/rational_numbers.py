from __future__ import division

# find greatest common denominator of a & b
def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

class Rational(object):
    def __init__(self, numer, denom):
        self.numer, self.denom = self._reduce(numer, denom)

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        return Rational((self.numer * other.denom) + (other.numer * self.denom), self.denom * other.denom)

    def __sub__(self, other):
        return Rational((self.numer * other.denom) - (other.numer * self.denom), self.denom * other.denom)

    def __mul__(self, other):
        return Rational(self.numer * other.numer, self.denom * other.denom)

    def __truediv__(self, other):
        return Rational(self.numer * other.denom, self.denom * other.numer)

    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        if power > 0:
            return Rational(self.numer ** power, self.denom ** power)
        else:
            return Rational(self.denom ** power, self.numer ** power)

    def __rpow__(self, base):
        return base ** (self.numer / self.denom)

    def _reduce(self, numer, denom):
        if denom == 0:
            raise ValueError("Cannot have 0 denominator")

        gcd = find_gcd(numer, denom)
        numer /= gcd
        denom /= gcd

        return int(numer), int(denom)
