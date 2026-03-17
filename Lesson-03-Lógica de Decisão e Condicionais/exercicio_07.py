'''
Exercício 7: Descontos Progressivos TecnoMais

DESCRIÇÃO:
Calcular o valor final de uma compra com base em faixas de preço e método de pagamento.

ENTRADA:
1. Valor total bruto (float)
2. Uso do cartão S ou N (string)

SAÍDA:
Valor final com duas casas decimais.
'''

# --- RESOLUÇÃO ---

# 1. Inputs (valor e cartão)
valor_bruto = float(input("Valor total bruto: "))
uso_cartao = input("Método de pagamento com cartão (S ou N): ").upper()
desconto = 0

# 2. Definir o desconto base
if valor_bruto > 1000:
    desconto = 15
elif valor_bruto > 500:
    desconto = 10
elif valor_bruto > 100:
    desconto = 5
else:
    desconto = 0

# 3. Aplicar bônus do cartão
# Se o cliente já tem algum desconto E usa o cartão, ganha + 2%
if desconto > 0 and uso_cartao == "S":
    desconto = desconto + 2

# 4. Calcular o valor final
# A fórmula é: Valor Bruto menos a porcentagem do desconto
valor_final = valor_bruto * (1 - desconto / 100)

# 5. Saída com exatamente duas casas decimais
print(f"Valor final com desconto: {valor_final:.2f}")
