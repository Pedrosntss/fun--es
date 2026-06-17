# Oficina Mecânica Charuri

oficina_geral = []

def cadastrar_ordem_servico():
    print("\n--- NOVA ORDEM DE SERVIÇO ---")
    # Capturando os dados iniciais do mundo real
    cliente = input("Nome do cliente: ")
    modelo_carro = input("Modelo do veículo: ")

    while True:
        try:
            ano_carro = int(input("Ano do veículo (AAAA): "))
            if ano_carro < 1900 or ano_carro > 2026:
                print("Ano inválido, digite novamente!")
                continue  
            break
        except ValueError:
            print("Erro: O ano deve ser um número inteiro")

    while True:
        try:
            quilometragem = int(input("Quilometragem atual: "))
            if quilometragem < 0:
                print("Valor invalido. Digite novamente!")
                continue
            break
        except ValueError:
            print("Erro: A quilometragem deve ser um número inteiro")

    necessita_revisão_completa = False

    if quilometragem > 10000 or ano_carro < 2020:
        print("\n Alerta do sistema: veículo necessita de revisão preventiva")
        necessita_revisão_completa = True
    else:
        print("\n Status: Manutenção de rotina.")
    
    lista_pecas = []
    total_orcamento = 0.00
    print("\n--- LANÇAMENTO DE PEÇAS E SERVIÇOS ---")

    while True:
        peca = input("Nome da peça/serviço (ou 'fim' para encerrar): ").strip()
        if peca.lower() == "fim":
            break # Quebra o laço e envia o fluxo para o fechamento
        try:
            preco = float(input(f"Preço de '{peca}': R$ "))
            if preco < 0:
                print("O preço não pode ser negativo")
                continue
            lista_pecas.append(peca)
            total_orcamento += preco
        except ValueError:
            print("Erro: Preço invalido! Item desconsiderado. Tente novamente.")


    #Estruturação de Dados
    ordem_servico = {
        "cliente": cliente, 
        "veiculo": modelo_carro,
        "ano": ano_carro,
        "km": quilometragem,
        "alerta_revisao": necessita_revisao_completa,
        "itens": lista_pecas,
        "total": total_orcamento,
        "status": "Em aberto",

    }

    # Conexão Final: Adicionamos o dicionario da O.S. na nossa global (banco de dados)
    oficina_geral.append(ordem_servico)
    print(f"\n Ordem de serviços de {cliente} gerada com sucesso")

#Esse função varre a lista global e exibe os dados estruturados de cada dicionário

def listar_todas_as_ordens():
    print("\n" + 30 * "=")
    print("     RELATÓRIO GERAL DA OFICINA      ")
    print("\n" + 30 * "=")

    if not oficina_geral:
        print("Nenhum veículo em manutenção no momento.")
        return
    # O "for" percorre a lista de dicionários
    for indice, ordem in enumerate(oficina_geral, 1):
        print(f"\n#OS: {indice} | Cliente: {ordem['cliente']} | Carro: {ordem['veiculo']}")
        print(f"Ano: {ordem} | KM: {ordem['km']}")
        print(f"Revisão Critica: {'SIM' if ordem['alerta_revisão'] else 'NÃO'}")
        print(f"Itens Trocados: {','.join(ordem['itens']) if ordem ['itens'] else 'Nenhum item lançado'}")
        print("Total")
        print(f"Total: R${ordem ['total']:.2f} ")
        print(f"Status: {ordem['status']}")
        print("-" * 45)

# Criação do menu
while True:
    print("\n=== SISTEMA OFICINA INTELIGENTE ===")
    print("1. Cadastrar nova ordem de serviço")
    print("2. Listar ordens de serviços relatório")
    print("3. SAir do sistema")

    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        cadastrar_ordem_servico()
    elif opcao == "2":
        listar_todas_as_ordens()
    elif opcao == "3":
        print("Fechando o sistema. Até logo, meu caro!")
        break
    else:
        print("Opção inválida! Tente outra vez!")
