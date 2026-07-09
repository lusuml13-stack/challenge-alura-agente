"""
Agente de Consultas Internas Empresariales
Versión 1: búsqueda por palabra clave con sinónimos y puntaje (sin RAG todavía)
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

# Sinónimos para mejorar las coincidencias
SINONIMOS = {
    "demora": "tarda",
    "demoran": "tarda",
    "tardan": "tarda",
    "tiempo": "tarda",
    "duracion": "tarda",
    "dura": "tarda",

    "tecnico": "soporte",
    "tecnica": "soporte",
    "ticket": "soporte",
    "incidencia": "soporte",
    "problema": "soporte",

    "vacacion": "vacaciones",
    "descanso": "vacaciones",
    "licencia": "vacaciones",

    "comprar": "compra",
    "compras": "compra",
    "adquisicion": "compra",

    "ingreso": "onboarding",
    "induccion": "onboarding",
    "nuevo": "onboarding",

    "aprueba": "aprobacion",
    "aprobar": "aprobacion",
}


def normalizar(texto):
    """Convierte a minúsculas, limpia signos y aplica sinónimos."""
    palabras = texto.lower().replace("¿", "").replace("?", "").split()

    palabras_normalizadas = {
        SINONIMOS.get(palabra, palabra)
        for palabra in palabras
    }

    return palabras_normalizadas - PALABRAS_VACIAS


def cargar_documento(ruta):
    """Lee y devuelve el contenido de un archivo de texto."""
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            return archivo.read()
    except FileNotFoundError:
        return None


def cargar_faq(ruta):
    """Lee el archivo faq.csv y devuelve pregunta-respuesta."""
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            return [
                (fila["pregunta"], fila["respuesta"])
                for fila in lector
            ]
    except FileNotFoundError:
        return []


def buscar_en_faq(consulta, faq):
    """
    Busca la pregunta del FAQ con más similitud
    usando coincidencia de palabras.
    """

    palabras_consulta = normalizar(consulta)

    if not palabras_consulta:
        return None

    mejor_respuesta = None
    mejor_puntaje = 0

    for pregunta, respuesta in faq:

        palabras_pregunta = normalizar(pregunta)

        coincidencias = palabras_consulta & palabras_pregunta
        puntaje = len(coincidencias)

        if puntaje > mejor_puntaje:
            mejor_puntaje = puntaje
            mejor_respuesta = respuesta

    if mejor_puntaje >= 1:
        return mejor_respuesta

    return None


def buscar_respuesta(consulta, faq):
    """
    Busca primero en FAQ.
    Si no encuentra, busca en documentos.
    """

    respuesta_faq = buscar_en_faq(consulta, faq)

    if respuesta_faq:
        return respuesta_faq

    consulta_normalizada = consulta.lower()

    for palabra_clave, ruta in DOCUMENTOS.items():

        if palabra_clave in consulta_normalizada:

            contenido = cargar_documento(ruta)

            if contenido:
                return contenido

            return f"Encontré el tema, pero no pude leer el archivo: {ruta}"

    return (
        "No encontré información relacionada. "
        "Probá con: onboarding, vacaciones, compras o soporte."
    )


def main():

    print("\n=== Agente de Consultas Internas ===")
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

        print("\nRespuesta:")
        print(respuesta)
        print()


if __name__ == "__main__":
    main()