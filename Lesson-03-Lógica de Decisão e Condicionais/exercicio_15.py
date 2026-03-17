'''
Exercício 15: As Regras do Ancião

CONDIÇÕES PARA APROVAÇÃO (Todas devem ser True):
1. Regra da Prova A e B.
2. Regra da Prova C (com exceção condicional).
3. Regra da Prova D (com exceção condicional).
'''

# --- SUA VEZ DE CODAR ---

# 1. entradas
a = int(input("o resultado da Prova A (valor entre 0 e 50): "))
b = int(input("o resultado da Prova B (valor entre 0 e 100): "))
c = int(input("o resultado da Prova C (1 significa sucesso, 0 significa falha): "))
d = int(input("o resultado da Prova D (valor entre 0 e 10): "))

# 2. Avaliando as Regras Estranhas

# Regra 1: A entre 15 e 45 E B até 60
regra1 = (a > 15 and a < 45) and (b <= 60)

# Regra 2: C é Sucesso OU (C falhou e A < 20, B < 30 e D é 10)
regra2 = (c == 1) or (c == 0 and a < 20 and b < 30 and d == 10)

# Regra 3: D >= 5 OU (D < 5 e (A é 10 ou 40) e B é 0)
regra3 = (d >= 5) or (d < 5 and (a == 10 or a == 40) and b == 0)

# 3. Veredito Final
# O Ancião exige que TODAS (and) sejam satisfeitas
if regra1 and regra2 and regra3:
    print("APROVADO")
else:
    print("REPROVADO")