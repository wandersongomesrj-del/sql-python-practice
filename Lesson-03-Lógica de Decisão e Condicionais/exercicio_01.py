'''
Exercício 1: Verificação de Maioridade para E-commerce

DESCRIÇÃO:
Uma loja online que comercializa produtos com restrição de idade precisa garantir 
que apenas clientes legalmente aptos finalizem suas compras. 

TAREFA:
Implemente um programa que verifique a elegibilidade de um cliente para realizar 
uma compra, considerando a idade legal (18 anos).

ENTRADA:
Um valor numérico inteiro representando a idade.

SAÍDA:
'Compra autorizada.' ou 'Compra negada.'
'''

# --- RESOLUÇÃO ---

# 1. Recebemos a idade e convertemos para inteiro (int)
idade = int(input("Digite sua idade: "))

# 2. Verificamos se a idade é maior ou igual a 18
if idade >= 18:
    print("Compra autorizada.")
else:
    print("Compra negada.")