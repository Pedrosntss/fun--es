# Funções com *args - calculadora flexível 

def estatisticas (*numeros):
    total = sum(numeros)
    media = total / len(numeros)
    maximo = max(numeros)
    minimo = min(numeros)
    print(f"Total: {total} | Média: {media:.2f} | Máx: {maximo} | Mín: {minimo}")

qnt = ("Digite quantas vezes deseja calcular: ")
cont = 0
while True:
    if cont != qnt:
        valor1 = int(input("Digite: "))
    else:
        break

estatisticas(valor1)