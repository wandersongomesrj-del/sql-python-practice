'''
Exercício 12: Níveis de Alerta Meteorológico

ORDEM DE PRIORIDADE:
1. Vermelho -> 2. Laranja -> 3. Amarelo -> 4. Azul -> 5. Sem Alerta

ENTRADAS:
- vento (int)
- temp (int)
- umidade (int)
- prec (string)
'''

# --- RESOLUÇÃO ---

# 1. Inputs
vento = int(input())
temp = int(input())
umidade = int(input())
prec = input()

#  ALERTA VERMELHO
if (vento > 80) or (prec == "Granizo" and vento > 60):
    print("ALERTA VERMELHO (Perigo Iminente)")

#  ALERTA LARANJA
elif (temp < -10) or \
     (prec == "Neve" and vento > 40) or \
     (prec == "Neve" and temp < 0) or \
     (vento > 50):
    print("ALERTA LARANJA (Cuidado)")

# ALERTA AMARELO (Tente montar este!)
elif (prec == "Chuva" and vento > 40 and umidade > 90) or \
     (vento > 20) or \
     (umidade > 80):
    print("ALERTA AMARELO (Atenção)")

# ALERTA AZUL
elif (prec == "Nenhum" and temp < 5 and vento > 30) or \
     (temp < 10) or \
     (umidade > 75) or \
     (prec == "Chuva"):
    print("ALERTA AZUL (Observação)")

# SEM ALERTA
else:
    print("SEM ALERTA")
