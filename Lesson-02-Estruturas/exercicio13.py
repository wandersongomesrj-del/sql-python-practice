### Exercício 13 – Engenharia Reversa de Tributação e Logística
"""
Um analista financeiro precisa calcular o custo de faturamento de uma licença de software internacional que custa 2.500 reais. Sobre esse valor base, deve incidir uma alíquota de 
serviço de 5%. Somente após o cálculo do valor tributado, deve-se somar uma taxa de suporte fixo de 150 reais. O impacto esperado é a emissão de notas fiscais corretas onde a taxa
de suporte não sofra incidência tributária.

**Tarefa:**
Defina os valores para custo base (2500), alíquota (0.05) e suporte (150). Calcule, em apenas uma linha utilizando parênteses, o valor final que o cliente deverá pagar, garantindo
que a ordem das operações respeite a regra de negócio descrita. Exiba o total final.
"""

custo_base = 2500
aliquota = 0.05
suporte = 150

valor_final = (custo_base * (1 + aliquota)) + suporte

print("Valor final/total que o cliente deverá pagar: ", valor_final)

