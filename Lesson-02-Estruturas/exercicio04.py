### Exercício 4 – Fluxo IPO: Entrada, Processamento e Saída
"""
Uma equipe de logística precisa de um pequeno utilitário para registrar dados de estoque. O planejamento exige que o código siga uma estrutura organizada de entrada, processamento
e saída (IPO). Para este teste, os dados de entrada são o peso de uma caixa (80kg) e a quantidade (10 unidades). O impacto esperado é a facilidade de manutenção do código através 
de um fluxo lógico claro.

**Tarefa**

Crie um programa que siga o fluxo IPO:
1. **Entrada:** Defina as variáveis `peso_unidade = 80` e `quantidade = 10`.
2. **Processamento:** Crie a variável `peso_total` que multiplica o peso pela quantidade.
3. **Saída:** Exiba o valor armazenado em `peso_total` usando o comando `print()`.
"""

peso_unidade = 80
quantidade = 10

peso_total = peso_unidade * quantidade

print("Peso total é: ", peso_total)
