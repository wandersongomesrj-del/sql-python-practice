'''
Exercício 2: Sistema de Gestão Acadêmica - Status de Aprovação

DESCRIÇÃO:
O objetivo é identificar rapidamente o status de aprovação de um aluno 
comparando sua nota final com a nota mínima exigida.

TAREFA:
Classificar o estudante como 'APROVADO' ou 'REPROVADO'.

ENTRADA:
Dois valores inteiros (0 a 100):
1. A nota final do estudante.
2. A nota mínima para aprovação.

SAÍDA:
'APROVADO' ou 'REPROVADO'.
'''

# --- RESOLUÇÃO ---

# 1. Recebemos os dois valores de entrada. 
# Importante: Como são duas linhas de entrada, chamamos o input() duas vezes.
nota_final = int(input("A nota final do estudante: "))
nota_minima = int(input("A nota mínima para aprovação: "))

# 2. Verificamos a condição de aprovação
# Se a nota do aluno for MAIOR ou IGUAL à mínima, ele passou.
if nota_final >= nota_minima:
    print("APROVADO")
else:
    print("REPROVADO")