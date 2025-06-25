from random import randint
from sympy import mod_inverse

# Curva elíptica sobre Fp: y² = x³ + ax + b mod p
class EllipticCurve:
    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.p = p

    def is_on_curve(self, P):
        if P is None:
            return True
        x, y = P
        return (y ** 2 - x ** 3 - self.a * x - self.b) % self.p == 0

    def add(self, P, Q):
        if P is None: return Q
        if Q is None: return P
        x1, y1 = P
        x2, y2 = Q

        if x1 == x2 and y1 != y2:
            return None

        if P == Q:
            s = (3 * x1**2 + self.a) * mod_inverse(2 * y1, self.p)
        else:
            s = (y2 - y1) * mod_inverse(x2 - x1, self.p)

        s %= self.p
        x3 = (s ** 2 - x1 - x2) % self.p
        y3 = (s * (x1 - x3) - y1) % self.p
        return (x3, y3)

    def multiply(self, P, n):
        R = None
        Q = P
        while n > 0:
            if n % 2 == 1:
                R = self.add(R, Q)
            Q = self.add(Q, Q)
            n //= 2
        return R
    
# ----------------------------------
# Simulação do protocolo ECDH
# ----------------------------------

p = 97
a = 2
b = 3
curve = EllipticCurve(a, b, p)
G = (3, 6)

priv_A = randint(1, p - 1)
priv_B = randint(1, p - 1)

pub_A = curve.multiply(G, priv_A)
pub_B = curve.multiply(G, priv_B)

shared_A = curve.multiply(pub_B, priv_A)
shared_B = curve.multiply(pub_A, priv_B)

assert shared_A == shared_B
print("Chave compartilhada:", shared_A)