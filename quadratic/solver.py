import cmath

class QuadraticEquation:
    def __init__(self, a, b, c):
        if a == 0:
            raise ValueError("a ne peut pas être 0. Ce n'est pas une équation quadratique.")
        self.a = a
        self.b = b
        self.c = c

    def discriminant(self):
        return self.b ** 2 - 4 * self.a * self.c

    def solve(self):
        d = self.discriminant()
        racine = cmath.sqrt(d)
        x1 = (-self.b + racine) / (2 * self.a)
        x2 = (-self.b - racine) / (2 * self.a)
        return x1, x2
