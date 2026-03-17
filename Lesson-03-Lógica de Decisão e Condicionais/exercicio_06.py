'''
Exercício 6: Reinos Esquecidos - Requisitos de Habilidade

DESCRIÇÃO:
Verificar se um herói tem os atributos necessários para uma habilidade lendária.

TAREFA:
Classificar o herói como 'QUALIFICADO' ou 'NAO QUALIFICADO'.

ENTRADA:
1. Valor de Força (int)
2. Valor de Agilidade (int)

SAÍDA:
'QUALIFICADO' ou 'NAO QUALIFICADO'
'''

# --- RESOLUÇÃO ---

# 1. Recebemos os valores de entrada
# Dica: Se for para um teste automático, use apenas input() sem o texto interno.
forca = int(input("Qual a força desse herói: "))
agilidade = int(input("Qual a agilidade desse herói: "))

# 2. Verificamos as duas condições simultaneamente usando o 'and'
if forca > 75 and agilidade > 80:
    print("QUALIFICADO")
else:
    print("NAO QUALIFICADO")

