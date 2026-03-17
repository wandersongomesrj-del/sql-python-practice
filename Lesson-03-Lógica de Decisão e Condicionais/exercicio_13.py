'''
Exercício 13: Calculadora Básica

TAREFA:
Realizar uma operação matemática entre dois números reais.

ENTRADAS:
1. Primeiro número (float)
2. Segundo número (float)
3. Operação (string: 'soma', 'subtracao', 'multiplicacao' ou 'divisao')

SAÍDA:
O resultado da conta (float).
'''

# --- RESOLUÇÃO  ---

# 1. Recebendo os dados
num1 = float(input("Primeiro valor da operação: "))
num2 = float(input("Segundo valor da operação: "))
operacao = input("Qual operação matematica será usada (soma, multiplicação, subtração e divisão): ").lower()

# 2. Verificando a operação e calculando
if operacao == "soma":
    resultado = num1 + num2

elif operacao == "subtracao":
    resultado = num1 - num2

# --- ETAPA 3: Multiplicação e Divisão ---
elif operacao == "multiplicacao":
    resultado = num1 * num2

elif operacao == "divisao":
    resultado = num1 / num2

# 4. Exibindo o resultado final
print("O resultado da operação é: ",  resultado)