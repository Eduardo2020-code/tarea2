# Tarea 2 – Consumo de API REST con Python

## Objetivo

Se  desarrollo un script en Python realizando el consumo de una API REST pública utilizando los métodos `GET` y `POST`. Se incluyen procesos de transformación de datos, simulación de envío de información y manejo adecuado de errores. Esta actividad demuestra competencias en integración con servicios externos y uso correcto de la librería `requests`.

## API utilizada

Se  implemento la API pública gratuita [JSONPlaceholder](https://jsonplaceholder.typicode.com), útil para pruebas de aplicaciones tipo REST.

**Endpoints utilizados:**

- `GET /posts`: retorna una lista de publicaciones simuladas.
- `POST /posts`: simula la creación de una publicación. Aunque la petición retorna un objeto con éxito, no se guarda en el servidor.

## Enfoque implementado

1. **Solicitud GET**  
   Se realizó una solicitud al endpoint `/posts` para obtener una lista de publicaciones. Se imprimieron los títulos de las primeras 5 entradas.

2. **Procesamiento de datos**  
   La respuesta JSON fue transformada a una lista de diccionarios en Python. Se extrajeron campos como `title` y `body` para su impresión.

3. **Solicitud POST**  
   Se simuló el envío de una nueva publicación, enviando campos como `title`, `body` y `userId`. La respuesta contenía un objeto con un `id` generado por el servidor.

4. **Manejo de errores**  
   Se utilizaron bloques `try-except` para capturar excepciones de red o errores HTTP. Se validó el código de respuesta y se mostraron mensajes adecuados en caso de fallos.

## Requisitos del entorno

- Python 3.7
- Librería `requests` (se puede instalar con `pip install requests`)

## Comandos

1. Primero tener  Python instalado.
2. Se debe intalar la libreria necesaria para ejecutar los comando requeridos:

   1. instalar la libreria para ejecutar el entorno de python:
   pip install requests

   2. Comando para ejecutar el script y muestre resultados:
   python tarea2_api.py
