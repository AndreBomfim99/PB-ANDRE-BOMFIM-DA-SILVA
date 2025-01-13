import csv

animais = [
    "Gatorro", "Cão", "Pato", "Elefante", "Tigre", "Leão", "Vacalo", "Zebra", "Jacaré", "Lobo",
    "Pinguim", "Gavião", "Urso", "Raposa", "Tartaruga", "Golfinho", "Cobra", "Mamaco", "Girafa", "Camelo"
]

animais.sort()

[print(animal) for animal in animais]

caminho_arquivo = r"C:\\EXE_GERACAO\\gera20\\animais.csv"

with open(caminho_arquivo, mode="w", newline="", encoding="utf-8") as arquivo_csv:
    grava = csv.writer(arquivo_csv)
    for animal in animais:
        grava.writerow([animal])

