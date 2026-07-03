import pandas as pd

faq = pd.read_csv("data/faq.csv")

print("=== FAQ ===")
print(faq)

print("\n=== ONBOARDING ===")

with open("data/onboarding.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()

print(contenido)
print("\n=== VACACIONES ===")

with open("data/vacaciones.txt", "r", encoding="utf-8") as archivo:
    vacaciones = archivo.read()

print(vacaciones)

print("\n=== COMPRAS ===")

with open("data/compras.txt", "r", encoding="utf-8") as archivo:
    compras = archivo.read()

print(compras)

print("\n=== SOPORTE TECNICO ===")

with open("data/soporte_tecnico.txt", "r", encoding="utf-8") as archivo:
    soporte = archivo.read()

print(soporte)

