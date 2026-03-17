'''
Exercício 3: Monitoramento de Temperatura Hospitalar

DESCRIÇÃO:
Identificar rapidamente se um paciente está com "Estado febril" ou "Febre".

TAREFA:
Analisar a temperatura e exibir a mensagem correta conforme o limiar.

ENTRADA:
Um valor numérico de ponto flutuante (float).

SAÍDA:
- Se >= 38.0: 'Febre'
- Se >= 37.5 (e menor que 38): 'Estado febril'
- Outros casos: Sem saída.
'''

# --- RESOLUÇÃO ---

#1. Recebemos a temperatura e convertemos para decimais (float)
temperatura = float(input("Monitoramento de Temperatura: "))

# 2. Verificamos a temperatura do paciente.
febre = 38.0
Estado_febril = 37.5

# 3. Verificamos as condições
if temperatura >= febre:
    print("Febre")
elif temperatura >= Estado_febril:
    print("Estado febril")