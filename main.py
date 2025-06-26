from ecdh import EllipticCurve
from ecdsa import calculate_order, generate_keypair, sign, verify

# 1. Definição dos parâmetros da curva
p = 97
a = 2
b = 3
G = (3, 6)
curve = EllipticCurve(a, b, p)

if not curve.is_on_curve(G):
    raise ValueError("O ponto base G não está na curva.")

n = calculate_order(curve, G)
print(f"Parâmetros da curva: y^2 = x^3 + {a}x + {b} mod {p}")
print(f"Ponto base G: {G} com ordem {n}\n")

# 2. ECDH - Geração de chave compartilhada
priv_A, pub_A = generate_keypair(curve, G, n)
priv_B, pub_B = generate_keypair(curve, G, n)

shared_A = curve.multiply(pub_B, priv_A)
shared_B = curve.multiply(pub_A, priv_B)

assert shared_A == shared_B
print(f"ECDH - Chave compartilhada: {shared_A}\n")

# 3. ECDSA - Assinatura e verificação de mensagem
mensagem = "Autenticando com ECC ✔"
assinatura = sign(curve, G, n, priv_A, mensagem)
valido = verify(curve, G, n, pub_A, mensagem, assinatura)

print(f"Mensagem: \"{mensagem}\"")
print(f"Assinatura gerada: {assinatura}")
print(f"Verificação da assinatura: {'Válida' if valido else 'Inválida'}")