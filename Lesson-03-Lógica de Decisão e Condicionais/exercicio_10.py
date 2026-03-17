'''
Exercício 10: Sistema de Pontuação BattleQuest

TAREFA:
Calcular a pontuação final somando 4 critérios e verificar o status de Elite.

PONTUAÇÃO FINAL = (Inimigos) + (Objetivos) + (Penalidade Mortes) + (Tempo)

STATUS:
Se Pontuação Final > 100: "Jogador Elite"
'''

# --- RESOLUÇÃO ---

#1. Serão fornecidos quatro valores em linhas separadas.
#Um inteiro representando o número de inimigos derrotados.
#Um inteiro representando o número de objetivos conquistados.
#Um inteiro representando o número de mortes sofridas (quanto maior, pior).
#Um inteiro representando o tempo de partida em minutos.

inimigos = int(input("Número de inimigos derrotados: "))
objetivos = int(input("Número de objetivos conquistados: "))
mortes = int(input("Número de mortes sofridas (quanto maior, pior): "))
tempo = int(input("Tempo de partida em minutos: "))

# 1. Pontos por inimigos derrotados
if inimigos < 10:
    ponto_inimigos = 10
elif 10 <= inimigos <= 29:
    ponto_inimigos = 30
else:
    ponto_inimigos = 50

# 2. Pontos por objetivos conquistados
if objetivos == 0:
    ponto_objetivos = 0
elif 1 <= objetivos <= 2:
    ponto_objetivos = 25
# Aqui entra o objetivos >= 3
else:
    ponto_objetivos = 60

# 3. Penalidade por mortes sofridas
if mortes < 5:
    ponto_mortes = 0
elif 5 <= mortes <= 10:
    ponto_mortes = -10
# Aqui entra o mortes > 10
else:
    ponto_mortes = -30

# 4. Pontos por tempo de partida
if tempo < 5:
    ponto_tempo = 25
elif 5 <= tempo <= 14:
    ponto_tempo = 15
# Aqui entra o tempo >= 15
else: 
    ponto_tempo = 5

pontuacao_final = ponto_inimigos + ponto_objetivos + ponto_mortes + ponto_tempo

print("Pontuação final do jogador: ", pontuacao_final)

# Verificamos se é Elite
if pontuacao_final > 100:
    print("Jogador Elite")
    print("Parabéns pelo seu desempenho!")




    