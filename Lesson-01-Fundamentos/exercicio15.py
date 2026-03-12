## Exercício 15
"""
Uma equipe de comunicação digital está analisando a qualidade textual das mensagens enviadas em 
campanhas de marketing. Um dos indicadores utilizados é a porcentagem de vogais em relação ao 
total de caracteres da mensagem, considerando que textos muito pobres em vogais podem indicar 
erros de digitação ou baixa legibilidade. Para essa análise, todos os caracteres devem ser 
considerados no total, incluindo letras, espaços e sinais de pontuação. Um programa em Python, 
executado em blocos no Deepnote, será utilizado para realizar esse cálculo de forma automática e 
padronizada.

### Tarefa

Desenvolva um programa que calcule a porcentagem de vogais presentes em uma mensagem de inserida 
pelo usuário, em relação ao número total de caracteres da string. O programa deve conter 
comentários explicando as principais etapas do código. Atenção, considere todas as vogais 
independente de serem maiúsculas ou minúsculas

#### Entrada
O texto a ser analisado é a string definida na variável `mensagem`, recebida do usuário.

#### Saída
O programa deve produzir uma única linha de texto exibindo a porcentagem de vogais em relação ao 
total de caracteres da mensagem
"""


mensagem = input("Ensira uma mensagem de texto: ")
total_caracteres = len(mensagem)

vogais = "aeiouAEIOU"
contador_vogais = 0

for letra in mensagem:
    if letra in vogais:
        contador_vogais += 1


porcentagem = (contador_vogais / total_caracteres) * 100

print(f"Porcentagem de Vogais em relação ao total de caractere da mensagem é: {porcentagem}%")






