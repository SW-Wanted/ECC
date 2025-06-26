from random import randint
from sympy import mod_inverse

# Curva elíptica sobre Fp: y² = x³ + ax + b mod p
class EllipticCurve:
    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.p = p

    # Verifica se um ponto P(x, y) está na curva.
    def is_on_curve(self, P):
        if P is None: # O ponto no infinito (O) é considerado na curva.
            return True
        x, y = P
        # Verifica se y² % p == (x³ + ax + b) % p
        return (y ** 2 - x ** 3 - self.a * x - self.b) % self.p == 0

    def add(self, P, Q):
        """Implementa a adição de dois pontos P e Q na curva elíptica.
        Considera os casos para o ponto no infinito (None), pontos distintos
        e duplicação de pontos.
        """
        if P is None: return Q # P + O = P
        if Q is None: return P # Q + O = Q
        x1, y1 = P  # Desempacota as coordenadas de P
        x2, y2 = Q  # Desempacota as coordenadas de Q

        # Se P = -Q (reflexão no eixo x), a soma é o ponto no infinito (O)
        if x1 == x2 and y1 != y2:
            return None

        if P == Q: # Duplicação de ponto (P + P)
            # A inclinação da tangente é [(3x₁² + a) * (2y₁)⁻¹] mod p
            # É necessário verificar se 2y₁ ≠ 0 mod p para o inverso modular (ou seja, 2y₁ ≠ 0 (mod p))
            if (2 * y1) % self.p == 0: # Caso especial onde a tangente é vertical
                return None # Resulta no ponto no infinito
            s = (3 * x1**2 + self.a) * mod_inverse(2 * y1, self.p)
        else: # Adição de dois pontos distintos (P + Q)
            # A inclinação da secante é [(y₂ - y₁) * (x₂ - x₁)⁻¹] mod p
            if (x2 - x1) % self.p == 0: # Caso especial onde a linha é vertical
                return None # Resulta no ponto no infinito
            s = (y2 - y1) * mod_inverse(x2 - x1, self.p)

        s %= self.p  # Garante que a inclinação está no intervalo do corpo finito
        x3 = (s ** 2 - x1 - x2) % self.p  # Calcula a coordenada x do ponto resultante
        y3 = (s * (x1 - x3) - y1) % self.p  # Calcula a coordenada y do ponto resultante
        return (x3, y3)  # Retorna o novo ponto na curva

    # Implementa a multiplicação escalar de um ponto P por um inteiro n usando o algoritmo 'double-and-add'.
    def multiply(self, P, n):
        
        if n == 0: return None # 0 * P = O
        if n < 0: # Para n negativo, calcula -n * (-P)
            P = (P[0], -P[1] % self.p) # Inverso aditivo de P
            n = abs(n)

        R = None # Inicializa o resultado como o ponto no infinito
        Q = P    # Q é o ponto que será dobrado (P, 2P, 4P, 8P, ...)
        
        while n > 0:
            if n % 2 == 1: # Se o bit menos significativo de n for 1, adiciona Q a R
                R = self.add(R, Q)
            Q = self.add(Q, Q) # Dobra Q
            n //= 2 # Desloca n para a direita (divide por 2)
        return R