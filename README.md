# 🔐 Elliptic Curve Cryptography (ECC) – Simples. Elegante. Poderoso.

> A matemática que protege bilhões de dispositivos… e cabe em um gráfico no plano cartesiano.

Este repositório é uma jornada completa pela Criptografia de Curvas Elípticas (**ECC**), explorando desde as bases matemáticas até a implementação prática em Python, **sem depender de bibliotecas externas** para as operações principais. Aqui, a segurança digital deixa de ser uma caixa preta e se revela como uma construção geométrica compreensível.

---

## 🌌 Por que ECC?

A ECC não é apenas mais um algoritmo de segurança: é uma **obra-prima da matemática aplicada**.

- 🧠 Baseada em **curvas algébricas** sobre corpos finitos
- 🌀 Estrutura de **grupo abeliano** via adição de pontos
- 🔐 Substitui a exponenciação modular por **operações geométricas**
- 📉 Proporciona **segurança comparável ao RSA** com chaves **muito menores**
- ⚡ Ideal para sistemas restritos: **IoT, dispositivos móveis, blockchain**

Em uma era onde eficiência e segurança são essenciais, a ECC tornou-se o **padrão moderno** para comunicações seguras.

---

## ✍️ O que você encontra aqui

Este projeto é **educacional** e **exploratório**, feito para aprender e ensinar:

- 📘 **Teoria Matemática**: curvas elípticas, grupos, leis de adição, singularidade
- 🧮 **Classe `EllipticCurve`**: adição e multiplicação de pontos
- 🔄 **Simulação do protocolo ECDH** – troca segura de chaves
- ✍️ **Implementação do ECDSA** – assinatura digital
- 🎨 **Gráficos interativos com GeoGebra** – visualização de \( P + Q = R \)
- 📄 **Relatório completo** (PDF): da álgebra ao Python, com análises e referências

---

## 📐 Intuição Visual – A magia de \( P + Q = R \)

Imagine dois pontos \( P \) e \( Q \) sobre uma curva. Traçando uma reta entre eles, ela intercepta a curva em um terceiro ponto. Refletindo esse ponto sobre o eixo x, obtemos \( R = P + Q \).

Essa operação é a base de tudo: geração de chaves, criptografia, assinaturas.

> 💡 "A segurança da ECC está na dificuldade de inverter essa operação:  
> dado \( P \) e \( R = kP \), encontrar \( k \) é praticamente impossível."

---

## 🧠 O que você aprende aqui

- Como curvas elípticas funcionam **sobre corpos finitos**
- Como construir operações seguras com **aritmética modular**
- Por que o **ECDLP (Elliptic Curve Discrete Log Problem)** é resistente
- Como implementar **ECDH** e **ECDSA** do zero
- Como **visualizar criptografia** de forma intuitiva

---

## 🚀 Comece agora

Clone este repositório:

```bash
git clone https://github.com/SW-Wanted/ecc.git
cd ecc
python main.py
```

### Explore os arquivos

| Arquivo    | Descrição                                      |
|------------|------------------------------------------------|
| ecdh.py    | Classe EllipticCurve e implementação do ECDH   |
| ecdsa.py   | Funções de assinatura e verificação digital    |
| main.py    | Execução combinada e simulações                |
| ECC.pdf    | Relatório completo, com teoria, gráficos e análise |

---

## 🌍 Relevância

ECC está presente em:

- 🔒 TLS/SSL (HTTPS)
- 📲 Mensagens criptografadas (Signal, WhatsApp)
- 💰 Criptomoedas (Bitcoin, Ethereum)
- 🔐 GPG, OpenSSH, JWT

Se você quer dominar criptografia moderna, entender ECC é fundamental.

---

## 📚 Referências

- Neal Koblitz & Victor S. Miller (1985) – Fundadores da ECC
- NIST, IETF, ENISA – Curvas recomendadas
- Certicom Research – ECC Challenges
- RFC 7748 – Curve25519 para X25519 e EdDSA

---

## 👨‍💻 Autor

<a href="https://github.com/SW-Wanted"><img src="https://github.com/SW-Wanted.png" alt="Emanuel dos Santos" width="25" height="25" align="center"> Emanuel dos Santos</a>