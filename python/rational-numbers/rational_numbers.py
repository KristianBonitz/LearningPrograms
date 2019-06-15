from __future__ import division


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
        return Rational(self.numer ** power, self.denom ** power)

    def __rpow__(self, base):
        return base ** (self.numer / self.denom)

    def _reduce(self, numer, denom):
        if numer == 0:
            return 0, 1
        elif numer == denom:
            return 1, 1 
        elif denom == 0:
            raise ValueError("Cannot have 0 denominator")

        #See which one is higher
        hcd = 1
        if abs(numer) > abs(denom):
            hcd = abs(denom)
        else:
            hcd = abs(numer)

        #figure out highest common denominator 
        while numer % hcd != 0 or denom % hcd != 0:
            hcd -= 1

        if hcd > 1:
            numer /= hcd
            denom /= hcd

        #adjust minus
        if denom < 0:
            denom *= -1
            numer *= -1

        return int(numer), int(denom)
