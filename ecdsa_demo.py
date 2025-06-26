from ecdh import EllipticCurve
from ecdsa import *

# Define curva e G
curve = EllipticCurve(a=2, b=3, p=97)
G = (3, 6)
n = calculate_order(curve, G)

# Geração de chave
d, Q = generate_keypair(curve, G, n)

# Mensagem
msg = "Segurança digital com ECC é eficiente"
assinatura = sign(curve, G, n, d, msg)

print("Assinatura:", assinatura)
print("Verificação:", "Válida ✅" if verify(curve, G, n, Q, msg, assinatura) else "Inválida ❌")