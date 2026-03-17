'''
Exercício 11: Validador de Força de Senha

REQUISITOS (Precisa de pelo menos 2):
1. Comprimento >= 8 caracteres.
2. Contém caracteres especiais (!, @, #).
3. Possui pelo menos um número (0-9).

SAÍDA:
'Segura' ou 'Fraca'
'''

#1. Recebendo a Senha
senha = input("Digite sua senha: ")
pontos = 0

# REGRA 1: Comprimento >= 8
if len(senha) >= 8:
    pontos = pontos + 1

# REGRA 2: Caracteres especiais (!, @ ou #)
if "!" in senha or "@" in senha or "#" in senha:
    pontos = pontos + 1

# REGRA 3: Possui um algarismo (número)
# Aqui vai uma dica: vamos usar um loop simples para checar de 0 a 9
tem_numero = False
for numero in "0123456789":
    if numero in senha:
        tem_numero = True

if tem_numero:
    pontos = pontos + 1

# --- VEREDITO FINAL ---
# Se pontos for 2 ou 3, ela é Segura
if pontos >= 2:
    print("Segura")
else:
    print("Fraca")