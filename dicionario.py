# **Kwargs - argumentos nomeados variaveis
# captura qualquer quantidade de argumentos como um dicionário

def exibir_info(**dados): #**Kwargs vira dicionário
    for chave, valor in dados.items():
        print(f"{chave}: {valor}" )

exibir_info(nome="Carlos", idade=30, cidade= "SP")

