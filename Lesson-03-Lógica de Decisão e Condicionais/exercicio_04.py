'''
Exercício 4: Controle de Peso - Transportadora Entrega Rápida

DESCRIÇÃO:
Verificar se os pacotes estão dentro do limite de peso (10kg) para evitar multas.

TAREFA:
Classificar o pacote em: 'Excesso de peso', 'Peso próximo ao limite' ou 'Permitido'.

ENTRADA:
Um valor numérico real (float) representando o peso do pacote.

SAÍDA:
- Peso > 10.0: 'Excesso de peso'
- Peso entre 9.5 e 10.0: 'Peso próximo ao limite. Verificar embalagem.'
- Outros: 'Permitido'
'''

# --- RESOLUÇÃO ---

# 1. Recebemos um valor de entrada numérico (float).
PESO_DO_PACOTE = float(input("Informe o peso do pacote: "))

# 2. Verificamos as classificações dos pesos.
EXCESSO_DE_PESO = 10.0
PESO_LIMITE = 9.5

# 3. Verificamos as condições
if PESO_DO_PACOTE > EXCESSO_DE_PESO:
    print("Excesso de peso.")
elif PESO_DO_PACOTE >= PESO_LIMITE:
    print("Peso próximo ao limite. Verificar embalagem.")
else:
    print("Permitido.")

