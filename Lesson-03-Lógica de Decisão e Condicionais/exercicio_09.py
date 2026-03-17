'''
Exercício 9: Caverna dos Caminhos Incertos

TAREFA:
Simular um sistema de decisões encadeadas (uma escolha leva a outra).

ENTRADAS POSSÍVEIS:
- Caminho (Esquerda ou Direita)
- Dependendo do caminho: Coragem (int) ou Tocha (S/N)
- Dependendo do subcaminho: Vida (int) ou Tempo Tocha (int)
'''

# --- RESOLUÇÃO ---

caminho = input("Qual caminho irá seguir (esquerda ou direita): ").capitalize()

if caminho == "Esquerda":
    coragem = int(input("Nível de coragem: "))
    #Se a coragem for maior ou igual a 80, o resultado é Tesouro Encontrado.
    if coragem >= 80:
        print("Tesouro Encontrado")
    else:
        # Se coragem for menor que 80, o jogo pede a VIDA
        vida = int(input("Nível de vida restante: "))
        #Se a vida restante for maior ou igual a 30, o resultado é Fuga Bem-Sucedida. caso contrario o resultado é Derrota na Caverna.
        if vida >= 30:
            print("Fuga Bem-Sucedida")
        else:
            print("Derrota na Caverna")

elif caminho == "Direita":
    tocha = input("O jogador possui uma tocha (Sim ou Não): ").capitalize()
    #Se o jogador não possui tocha, o resultado é Perdido na Escuridao.
    if tocha == "Nao":
        print("Perdido na Escuridao")
    else:
        # Se tem tocha, o jogo pede o TEMPO
        tempo = int(input("O tempo restante da tocha em minutos é: "))
        #Se o tempo da tocha for maior que 10 minutos, o resultado é Caminho Seguro. caso contrario o resultado é Avanço Arriscado. 
        if tempo > 10:
            print("Caminho Seguro")
        else:
            print("Avanço Arriscado")