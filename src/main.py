"""
Agente de Consultas Internas Empresariales
Versión 1: búsqueda por palabra clave (sin RAG todavía)
"""

import csv

# Diccionario que asocia palabras clave con su archivo correspondiente
DOCUMENTOS = {
    "onboarding": "data/onboarding.txt",
    "vacaciones": "data/vacaciones.txt",
    "compra": "data/compras.txt",
    "compras": "data/compras.txt",
    "soporte": "data/soporte_tecnico.txt",
}

RUTA_FAQ = "data/faq.csv"

# Palabras muy comunes que no aportan significado a la búsqueda
PALABRAS_VACIAS = {
    "el", "la", "los", "las", "un", "una", "de", "del", "en", "que",
    "y", "a", "mi", "es", "si", "pasa", "qué", "cómo", "quién", "puedo",
    "debo", "para", "con", "mis",
}


def cargar_documento(ruta):
    """Lee y devuelve el contenido de un archivo de texto."""
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            return archivo.read()
    except FileNotFoundError:
        return None


def cargar_faq(ruta):
    """Lee el archivo faq.csv y devuelve una lista de pares pregunta/respuesta."""
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            return [(fila["pregunta"], fila["respuesta"]) for fila in lector]
    except FileNotFoundError:
        return []


def buscar_en_faq(consulta, faq):
    """Busca coincidencias de palabras significativas entre la consulta y las preguntas del FAQ."""
    palabras_consulta = set(consulta.lower().split()) - PALABRAS_VACIAS

    if not palabras_consulta:
        return None

    for pregunta, respuesta in faq:
        pregunta_limpia = pregunta.lower().replace("¿", "").replace("?", "")
        palabras_pregunta = set(pregunta_limpia.split()) - PALABRAS_VACIAS

        if palabras_consulta & palabras_pregunta:
            return respuesta

    return None


def buscar_respuesta(consulta, faq):
    """Busca primero en el FAQ y luego en los documentos por palabra clave."""
    consulta = consulta.lower()

    respuesta_faq = buscar_en_faq(consulta, faq)

    if respuesta_faq:
        return respuesta_faq

    for palabra_clave, ruta in DOCUMENTOS.items():

        if palabra_clave in consulta:
            contenido = cargar_documento(ruta)

            if contenido:
                return contenido

            return f"Encontré el tema, pero no pude leer el archivo: {ruta}"

    return "No encontré información relacionada. Probá con: onboarding, vacaciones, compras o soporte."


def main():

    print("=== Agente de Consultas Internas ===")
    print("Escribí 'salir' para terminar.\n")

    faq = cargar_faq(RUTA_FAQ)

    while True:

        consulta = input("Ingrese una consulta: ").strip()

        if consulta.lower() == "salir":
            print("¡Hasta luego!")
            break

        if not consulta:
            print("Por favor, escribí una consulta.\n")
            continue

        respuesta = buscar_respuesta(consulta, faq)

        print(f"\n{respuesta}\n")


if __name__ == "__main__":
    main()