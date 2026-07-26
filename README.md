# Alura Agente - Consultas Internas Empresariales

## Descripción

Agente de consultas internas empresariales capaz de responder preguntas sobre onboarding, vacaciones, compras y soporte técnico utilizando documentación corporativa como base de conocimiento.

## Estado

🚧 En desarrollo

### Implementado

- Base de conocimiento documental
- Lectura de documentos TXT
- Lectura de FAQ CSV
- Consultas por consola
- Búsqueda por palabras clave
- Búsqueda mediante sinónimos
- Búsqueda con sistema de puntuación
- Interfaz web desarrollada con Streamlit

### Próximos pasos

- Mejorar precisión de búsqueda
- Evolucionar hacia un sistema RAG
- Desplegar la aplicación

## Tecnologías utilizadas actualmente

- Python 3
- CSV
- Archivos TXT
- Git
- GitHub
- Streamlit

## Tecnologías previstas

- LangChain
- Gemini API

## Estructura del proyecto

```text
challenge-alura-agente/
│
├── app.py
│
├── data/
│   ├── onboarding.txt
│   ├── vacaciones.txt
│   ├── compras.txt
│   ├── soporte_tecnico.txt
│   └── faq.csv
│
├── docs/
│   ├── pruebas.md
│   ├── captura-github.png
│   ├── captura-consulta-vacaciones.png
│   ├── captura-consulta-soporte.png
│   ├── captura-streamlit.png
│   └── captura-demo-final.png
│
├── src/
│   └── main.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

## Evidencias

Las capturas de funcionamiento del proyecto se encuentran en la carpeta `docs`.

### Capturas disponibles

- captura-github.png
- captura-consulta-vacaciones.png
- captura-consulta-soporte.png
- captura-streamlit.png
- captura-demo-final.png

## Funcionalidades implementadas

✅ Lectura de documentos TXT

✅ Lectura de archivo FAQ CSV

✅ Consultas interactivas

✅ Búsqueda por palabras clave

✅ Sistema de sinónimos para mejorar coincidencias

✅ Sistema de puntuación por relevancia

✅ Respuestas basadas en documentación interna empresarial

✅ Interfaz web desarrollada con Streamlit

## Objetivo del proyecto

Este proyecto forma parte del Challenge Alura ONE AI for Tech.

El objetivo es evolucionar progresivamente desde una búsqueda basada en palabras clave hacia un sistema de recuperación de información más avanzado utilizando técnicas de RAG (Retrieval-Augmented Generation).

## Autor

Lucía Mendoza León

## Repositorio

https://github.com/lusuml13-stack/challenge-alura-agente
