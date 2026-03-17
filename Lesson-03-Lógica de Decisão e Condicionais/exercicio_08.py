'''
Exercício 8: Triagem de Candidatos TechSolutions

TAREFA:
Determinar se o candidato é 'Candidato Elegível' ou 'Candidato Não Elegível'.

REGRAS DE ELEGIBILIDADE:
1. Pelo menos 8 anos de experiência;
OU
2. Escolaridade (Pós-graduação ou Mestrado) AND Python Avançado;
OU (Desafio)
3. Conter a palavra "Infnet" na escolaridade ou no nível de Python.
'''

# --- RESOLUÇÃO ---

# 1. Inputs (Anos, Escolaridade, Nível)
anos = int(input("Quantos anos de experiência: "))
escolaridade = input("Qual a escolaridade(Graduação, Pós-graduação ou Mestrado): ").lower()
nivel = input("Seu nível em Python é Básico, Intermediário ou Avançado: ").lower()

# 2. Verificação do Desafio (Palavra Infnet)
candidato_infnet = "infnet" in escolaridade or "infnet" in nivel

# 3. Verificação das Condições Principais
if anos >= 8:
    print("Candidato Elegível")

elif (escolaridade == "pós-graduação" or escolaridade == "mestrado") and nivel_python == "avançado":
    print("Candidato Elegível")

elif candidato_infnet:
    print("Candidato Elegível")

else:
    print("Candidato Não Elegível")


