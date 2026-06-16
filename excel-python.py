# fucionarios = [
#     {"Setor": "Jurídico", "Nome": "Anderson", "Salário": 1459.00, "Cargo": "Gerente", "Bônus": }
# ]


def cadastrar_funcionario():
    print("="*50)
    print("Cadastro de Funcionáios")
    print("="*50)

    nome = input("Nome do funcionário: ")
    setor = input("Setor (Jurídico/Marketing/TI/Vendas): ")
    salario = float(input("Salário (Ex: 1450.00): R$"))
    cargo = input("Cargo (Gerente/Analista): ")
    bonus = float(input("Bônus (Ex: 850.00): R$ "))

    linha = f"{setor}, {nome}, {salario:.2f}, {cargo}, {bonus:.2f}"

    with open("Funcionarios.txt", "+a", encoding="utf-8") as arquivo: arquivo.write(linha + "\n")
    print("\nFuncionário cadastrado com sucesso!")
    # print(f"Dados salvos em 'funcionarios.txt'")
    return{"Setor": setor , "Nome": nome, "Salário": salario, "Cargo": cargo, "Bônus": bonus}

def ler_funcionarios():
    funcionarios = []
    with open("Funcionarios.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(",") 

            funcionario = {
                "Setor": dados[0].strip(),
                "Nome": dados[1].strip(),
                "Salário": float(dados[2]),
                "Cargo": dados[3].strip(),
                "Bônus": float(dados[4])
            }

            funcionarios.append(funcionario)

    return funcionarios
        # funcionarios.append(dados)
        # return funcionarios

cadastrar_funcionario()
lista = ler_funcionarios()

for funcionarios in lista: 
    print(f"{funcionarios}\n")

def somase(inter_soma, criterio, soma):
    somar = 0

    for funcionario in inter_soma:
        if funcionario == criterio:
            soma += lista[5]
            print(soma)


somase(lista,'ti', 'salário') 































            # dados = linha.strip().split(",")

            # funcionarios = { 
            #     "Setor": dados[0].strip(),
            #     "Nome": dados[1].strip(),
            #     "Salário": float(dados[2]),
            #     "Cargo": dados[3].strip()
            #     "Bônus": dados[4].strip() 
            # }
# novo_funcionario = cadastrar_funcionario()
# funcionarios = []
# funcionarios.append(novo_funcionario)
# # print("\nDados cadastrados", novo_funcionario)
# print(f"{funcionarios}\n")

