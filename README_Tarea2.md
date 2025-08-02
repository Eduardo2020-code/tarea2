# 🌐 TAREA 2 – Consumo de API REST con Python

## 🎯 Objetivo

Desarrollar un script en Python que consuma una API REST pública, utilizando métodos `GET` y `POST`, con procesamiento de datos y manejo de errores. Esta tarea demuestra habilidades en integración de servicios externos, uso de librerías como `requests`, y buenas prácticas de manejo de solicitudes HTTP.

---

## 🔗 API utilizada

Se utilizó la API gratuita **JSONPlaceholder**, ideal para pruebas de aplicaciones RESTful:

- **Base URL:** https://jsonplaceholder.typicode.com
- **GET /posts:** devuelve una lista de publicaciones de prueba.
- **POST /posts:** simula la creación de una nueva publicación (aunque no se guarda realmente en el servidor).

---

## 🧠 Enfoque implementado

1. **GET request**  
   Se realizó una solicitud `GET` al endpoint `/posts` para obtener publicaciones de ejemplo.  
   Se procesó la respuesta JSON y se imprimieron los títulos de las primeras 5 publicaciones.

2. **Procesamiento de datos**  
   Los datos obtenidos fueron transformados a una lista de diccionarios en Python.  
   Se extrajeron campos como `title` y se mostraron en consola.

3. **POST request**  
   Se simuló el envío de un nuevo post usando el endpoint `/posts`, con datos como `title`, `body` y `userId`.  
   La respuesta muestra un objeto con un `id` simulado por el servidor (`id: 101`).

4. **Manejo de errores HTTP**  
   Se usaron bloques `try-except` para capturar cualquier excepción derivada de problemas de red o errores de respuesta (`4xx` o `5xx`).

---

## 🧪 Ejecución

El script fue ejecutado en entorno local usando **Visual Studio Code** y Python 3.  
También es compatible con Google Colab o cualquier entorno que soporte `requests`.

---

## ✅ Archivos entregados

- `tarea2_api.py`: Código fuente del script.
- `README_Tarea2.md`: Documentación técnica.
- Captura de consola con resultado de ejecución.

---

## 🧩 Resultado

La ejecución mostró:

- ✅ 5 publicaciones extraídas exitosamente mediante `GET`.
- ✅ Publicación simulada enviada correctamente mediante `POST`.
- ✅ Manejo de errores activo y preparado para fallos de red o respuesta.

---

## 📌 Conclusión

Esta tarea demuestra la capacidad de consumir APIs REST de forma práctica usando Python.  
Se incluyeron elementos clave como manejo de errores, interpretación de respuestas JSON, y simulación de operaciones típicas como lectura y escritura de datos.

