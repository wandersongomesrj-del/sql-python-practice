'''
Exercício 14: Compatibilidade Sanguínea

REGRAS:
1. Tipo ABO: Receptor precisa aceitar o tipo do Doador.
2. Fator Rh: Receptor precisa aceitar o Rh do Doador.
'''

# --- SUA VEZ DE CODAR ---

# 1. entradas
tipo_rec = input("O tipo sanguíneo do receptor (`A`, `B`, `AB` ou `O`: ").upper()
rh_rec = input("O fator Rh do receptor (`+` ou `-`.): ")
tipo_doa = input("O tipo sanguíneo do doador (`A`, `B`, `AB` ou `O`: ").upper()
rh_doa = input("O fator Rh do doador (`+` ou `-`.): ")

tipo_ok = False
rh_ok = False

# 2. Verificando o Tipo Sanguíneo (ABO)
if tipo_rec == "A":
    if tipo_doa == "A" or tipo_doa == "O":
        tipo_ok = True
elif tipo_rec == "B":
    if tipo_doa == "B" or tipo_doa == "O":
        tipo_ok = True
elif tipo_rec == "AB":
    # AB recebe de todo mundo!
    tipo_ok = True
elif tipo_rec == "O":
    if tipo_doa == "O":
        tipo_ok = True

# 3. Verificando o Fator Rh
# Dica: Se o receptor for '+', ele aceita qualquer um. 
# Se for '-', só aceita se o doador também for '-'.
if rh_rec == "+":
    rh_ok = True
elif rh_rec == "-" and rh_doa == "-":
    rh_ok = True

# 4. Resultado Final
if tipo_ok and rh_ok:
    print("Doacao compativel")
else:
    print("Doacao incompativel")