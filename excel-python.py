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

    linha = f"{setor}, {nome}, {salario:.2f}, {cargo}, {bonus:.2f} \n"

    # with open("Funcionarios.txt", "+a", encoding="utf-8") as arquivo: arquivo.write(linha)
    print("\nFuncionário cadastrado com sucesso!")
    # print(f"Dados salvos em 'funcionarios.txt'")
    return{"Setor": setor, "Nome": nome, "Salário": salario, "Cargo": cargo, "Bônus": bonus}
    

novo_funcionario = cadastrar_funcionario()
lista = []
lista.append(novo_funcionario)
# print("\nDados cadastrados", novo_funcionario)
print(lista)

