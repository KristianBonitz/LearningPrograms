from __future__ import division


class Rational(object):
    def __init__(self, numer, denom):
        self.numer, self.denom = self._reduce(numer, denom)

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __truediv__(self, other):
        pass

    def __abs__(self):
        pass

    def __pow__(self, power):
        pass

    def __rpow__(self, base):
        pass

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

        #figure out lowest common denominator, 
        while numer % hcd != 0 and denom % hcd != 0:
            hcd -= 1

        numer /= hcd
        denom /= hcd

        #adjust minus
        if denom < 0:
            denom *= -1
            numer *= -1

        return numer, denom

