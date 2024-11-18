from functools import reduce

def calcula_saldo(lancamentos) -> float:
    valores = map(
        lambda l: l[0] if l[1] == "C" else -l[0], lancamentos
    ) 
    saldo = reduce(
        lambda acumulador, valor: acumulador + valor, valores, 0
    )  

    return saldo

if __name__ == "__main__":
    lancamentos = [(200, "D"), (300, "C"), (100, "C")]  
    saldo = calcula_saldo(lancamentos)
    print(saldo)