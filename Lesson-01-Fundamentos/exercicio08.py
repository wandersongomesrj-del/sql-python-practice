## Exercício 8
"""
Uma equipe de eventos está preparando um sistema simples para gerar **cartões de boas-vindas** em texto (ASCII) para participantes de um workshop. O cartão deve ter uma borda superior e inferior feitas com o caractere `=`, e linhas do meio com bordas laterais feitas com `=` e espaços no conteúdo, seguindo um padrão visual fixo.
"""
### Tarefa
"""
Crie um programa que gere e exiba um cartão semelhante ao do formato abaixo, usando um caracter (no exemplo, ""="") e operações de repetição/concatenação. O cartão deve ser armazenado em uma variável string (por exemplo, `cartao`) e depois exibido.

O resultado é semelhante à:

```
==================================
=                                =
=                                =
==================================
```
"""


caractere = "="
linha = caractere * 30
conteudo = " Sistema De Vendas "

cartao = linha + "\n" + conteudo + "\n" + linha

print(cartao)



