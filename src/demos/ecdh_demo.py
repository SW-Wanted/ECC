from ..ecc.ecdh import EllipticCurve
from random import randint
# ---------------------------------------------------
# Simulação do protocolo Elliptic Curve Diffie-Hellman (ECDH)
# ---------------------------------------------------

# 1. Definição dos parâmetros de domínio da curva (p, a, b, G)
# Escolhemos um exemplo simples para demonstração
p = 97  # Um número primo para o corpo finito Fp
a = 2   # Coeficiente 'a' da equação de Weierstrass
b = 3   # Coeficiente 'b' da equação de Weierstrass
curve = EllipticCurve(a, b, p)

# Ponto base G, que deve pertencer à curva
G = (3, 6)
# É fundamental verificar se G está na curva definida
if not curve.is_on_curve(G):
    raise ValueError(f"O ponto base {G} não está na curva y^2 = x^3 + {a}x + {b} mod {p}")
# Também é importante que a curva seja não-singular, ou seja, 4a^3 + 27b^2 != 0 mod p
discriminant = (4 * (a**3) + 27 * (b**2)) % p
if discriminant == 0:
    raise ValueError(f"A curva é singular (4a^3 + 27b^2 = 0 mod p). Escolha outros a e b.")

print(f"Parâmetros da Curva Elíptica: y^2 = x^3 + {a}x + {b} mod {p}")
print(f"Ponto Base (Gerador) G: {G}\n")

# 2. Geração de chaves privadas para Alice e Bob
# A chave privada é um número inteiro aleatório no intervalo [1, n-1],
# onde n é a ordem do subgrupo gerado por G. Para simplificar,
# usaremos p-1 como um limite superior razoável para este exemplo,
# embora em aplicações reais 'n' seja um valor específico para a curva.
priv_A = randint(1, p - 1) # Chave privada de Alice
priv_B = randint(1, p - 1) # Chave privada de Bob

print(f"Chave Privada de Alice (dA): {priv_A}")
print(f"Chave Privada de Bob (dB): {priv_B}\n")

# 3. Cálculo das chaves públicas 
# A chave pública é calculada multiplicando o ponto base G pela chave privada.
pub_A = curve.multiply(G, priv_A) # Chave pública de Alice (QA = dA * G)
pub_B = curve.multiply(G, priv_B) # Chave pública de Bob (QB = dB * G)

print(f"Chave Pública de Alice (QA): {pub_A}")
print(f"Chave Pública de Bob (QB): {pub_B}\n")

# 4. Troca de chaves públicas e cálculo do segredo compartilhado
# Alice e Bob trocam suas chaves públicas.
# Cada um usa a chave pública do outro e sua própria chave privada para
# calcular o segredo compartilhado.
shared_A = curve.multiply(pub_B, priv_A) # Alice calcula S = dA * QB
shared_B = curve.multiply(pub_A, priv_B) # Bob calcula S = dB * QA

print(f"Segredo Compartilhado Calculado por Alice: {shared_A}")
print(f"Segredo Compartilhado Calculado por Bob: {shared_B}")

# A asserção final verifica se ambos calcularam o mesmo segredo,
# demonstrando a eficácia do ECDH.
assert shared_A == shared_B, "As chaves compartilhadas não são iguais!"
print("\nAs chaves compartilhadas são iguais. O protocolo ECDH foi bem-sucedido!")