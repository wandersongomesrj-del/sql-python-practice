'''
Exercício 16: Triagem Cadastral (KYC)

OBJETIVO:
Validar cadastros de PF e PJ usando condicionais aninhadas.

PONTOS CHAVE:
1. Usar len() para contar dígitos de CPF (11) e CNPJ (14).
2. Só pedir a entrada extra (documentação/registro) se a primeira validação falhar.
3. Verificar idade apenas para PF.
'''

# --- SUA VEZ DE CODAR ---

# 1. Entrada inicial
tipo = input("tipo de cliente(CPF/CNPJ): ").upper()

# 2. Fluxo para Pessoa Física
if tipo == "PF":
    cpf = input("Digite o CPF (apenas numeros): ")
    idade = int(input("Idade: "))
    
    if len(cpf) == 11 and idade >= 18:
        print("Cadastro Aprovado")
    else:
        # Se caiu aqui, CPF está errado OU é menor de idade.
        # Mas a regra diz: se o CPF não tem 11, verificamos a doc complementar.
        if len(cpf) != 11:
            doc_extra = input("há documentação complementar ( S ou N): ").upper()
            if doc_extra == "S" and idade >= 18:
                print("Cadastro em Revisao")
            else:
                print("Cadastro Recusado")
        else:
            # CPF tem 11, mas a idade falhou
            print("Cadastro Recusado")

# 3. Fluxo para Pessoa Jurídica
elif tipo == "PJ":
    cnpj = input("Digite o CNPJ (apenas numeros): ")
    
    if len(cnpj) == 14:
        print("Cadastro Aprovado")
    else:
        # CNPJ não tem 14, pede registro provisório
        reg_prov = input("há documentação complementar ( S ou N): ").upper()
        if reg_prov == "S":
            print("Cadastro em Revisao")
        else:
            print("Cadastro Recusado")

# 4. Erro para tipo inválido
else:
    print("Erro: Tipo de cliente inválido")