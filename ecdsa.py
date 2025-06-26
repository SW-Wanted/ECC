# ecdsa.py
from sympy import mod_inverse
from random import randint
from hashlib import sha256

# Calcula o hash SHA-256 da mensagem como inteiro.
def hash_message(message):
    digest = sha256(message.encode()).hexdigest()
    return int(digest, 16)


# Calcula a ordem do ponto G (mínimo n tal que nG = O).
def calculate_order(curve, G):
    for i in range(1, curve.p + 1):
        if curve.multiply(G, i) is None:
            return i
    return None

# Gera chave privada aleatória e chave pública correspondente.
def generate_keypair(curve, G, n):
    d = randint(1, n - 1)  # chave privada
    Q = curve.multiply(G, d)  # chave pública
    return d, Q

# Assina uma mensagem com a chave privada d."""
def sign(curve, G, n, d, message):
    e = hash_message(message) % n
    while True:
        k = randint(1, n - 1)
        R = curve.multiply(G, k)
        if R is None:
            continue
        r = R[0] % n
        if r == 0:
            continue
        try:
            k_inv = mod_inverse(k, n)
        except ValueError:
            continue
        s = (k_inv * (e + r * d)) % n
        if s == 0:
            continue
        return (r, s)

# Verifica uma assinatura digital usando a chave pública Q.
def verify(curve, G, n, Q, message, signature):
    r, s = signature
    if not (1 <= r < n and 1 <= s < n):
        return False
    e = hash_message(message) % n
    try:
        w = mod_inverse(s, n)
    except ValueError:
        return False
    u1 = (e * w) % n
    u2 = (r * w) % n
    P = curve.add(
        curve.multiply(G, u1),
        curve.multiply(Q, u2)
    )
    if P is None:
        return False
    x, _ = P
    return r == x % n