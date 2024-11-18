def conta_vogais(texto: str) -> int:
    vogais = "aeiou"
    return len(list(filter(lambda caractere: caractere in vogais, texto.lower())))

resultado = conta_vogais("Xena guerreira")
print(resultado)


