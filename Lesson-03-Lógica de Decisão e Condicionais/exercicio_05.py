'''
Exercício 5: Gestor de Finanças Pessoais da Clara

DESCRIÇÃO:
Classificar despesas com base em palavras-chave na descrição.

TAREFA:
Identificar se a despesa é 'Essencial', 'Investimento' ou 'Lazer e Outros'.

ENTRADA:
1. Descrição (Texto)
2. Valor (Número Real)

SAÍDA:
Categoria - Valor (Exemplo: Essencial - 1500.0)
'''

# --- RESOLUÇÃO ---

# 1. Recebemos a descrição e já transformamos tudo em minúsculo (.lower())
# Isso garante que "ALUGUEL", "Aluguel" ou "aluguel" sejam lidos da mesma forma.
descricao = input("Identificação da despesa: ").lower()

# 2. Recebemos o valor da despesa
valor = float(input("Valor: "))

# 3. Definimos as listas de palavras-chave (Nossa biblioteca de consulta)
termos_essencial = ['aluguel', 'moradia', 'supermercado', 'alimentacao', 'agua', 'luz', 'internet']
termos_investimento = ['acoes', 'fundos', 'previdencia', 'bolsa']

# 4. Verificação de Categorias com base na Prioridade
# Usamos um laço (for) dentro do if para checar cada palavra da lista.
# O "any" verifica se PELO MENOS UMA das palavras da lista está na descrição.

if any(palavra in descricao for palavra in termos_essencial):
    categoria = "Essencial"
    
elif any(palavra in descricao for palavra in termos_investimento):
    categoria = "Investimento"
    
else:
    categoria = "Lazer e Outros"

# 5. Saída formatada conforme o exercício pediu (Categoria - Valor)
print(f"{categoria} - {valor}")