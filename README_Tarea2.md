# Tarea 2 – Consumo de API REST con Python

## Objetivo

El propósito de esta tarea es desarrollar un script en Python que realice el consumo de una API REST pública utilizando los métodos `GET` y `POST`. Se incluyen procesos de transformación de datos, simulación de envío de información y manejo adecuado de errores. Esta actividad demuestra competencias en integración con servicios externos y uso correcto de la librería `requests`.

## API utilizada

Se empleó la API pública gratuita [JSONPlaceholder](https://jsonplaceholder.typicode.com), útil para pruebas de aplicaciones tipo REST.

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

- Python 3.7 o superior
- Librería `requests` (se puede instalar con `pip install requests`)

## Ejecución

1. Asegúrese de tener Python instalado.
2. Instale la librería necesaria:

   ```bash
   pip install requests
