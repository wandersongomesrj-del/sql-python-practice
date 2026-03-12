## Exercício 6
"""
A empresa SecureNet está empenhada em fortalecer a segurança da informação para seus clientes. Para isso, está implementando novas políticas que exigem a inclusão de caracteres especiais em todas as senhas, além de critérios básicos relacionados ao uso de letras maiúsculas e minúsculas. Você foi encarregado de desenvolver um pequeno programa em Python, que será executado em blocos no Deepnote, para verificar a conformidade dessas senhas.

Este programa deve analisar a senha fornecida pelo usuário e determinar se ela atende aos requisitos de segurança definidos, garantindo assim uma camada extra de proteção.
"""
### Tarefa
"""
Considerando uma senha inserida pelo usuário por meio de `input()` (por exemplo, `Infnet123!@#`), o programa deve:

- Verificar a presença do caractere arroba (`'@'`), do símbolo de exclamação (`'!'`) e do caractere cerquilha (`'#'`) na senha, utilizando o operador `in`.
- Verificar se a senha está composta apenas por letras minúsculas.
- Verificar se a senha está composta apenas por letras maiúsculas.

Para cada uma dessas verificações, o resultado deve ser armazenado em variáveis distintas, indicando se cada critério de segurança foi atendido ou não. Exiba cada uma delas devidamente sinalizadas.
"""

senha = input("Digite a senha: ")

tem_arroba = "@" in senha
tem_exclamacao = "!" in senha
tem_cerquilha = "#" in senha

apenas_minusculas = senha.islower()
apenas_maiusculas =  senha.isupper()

print(f"contém @ : {tem_arroba}")
print(f"contém ! : {tem_exclamacao}")
print(f"contém # :  {tem_cerquilha}")

print(f"Apenas letras minúsculas: {apenas_minusculas}")
print(f"Apenas maiúsculas: {apenas_maiusculas}")
