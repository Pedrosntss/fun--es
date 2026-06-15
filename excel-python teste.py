def somase():
    print("="*50)
    print("Funcionáios")
    print("="*50)

    nome = input("Nome do funcionário: ")
    setor = input("Setor (Jurídico/Marketing/TI/Vendas): ")
    salario = float(input("Salário (Ex: 1450.00): R$"))
    cargo = input("Cargo (Gerente/Analista): ")
    bonus = float(input("Bônus (Ex: 850.00): R$ "))
    print ("Setor:", )

    lista = [{"Setor": setor, "Nome": nome, "Salário": salario, "Cargo": cargo, "Bônus": bonus}]


    # linha = f"{setor}, {nome}, {salario:.2f}, {cargo}, {bonus:.2f} \n"
    print (lista)
    