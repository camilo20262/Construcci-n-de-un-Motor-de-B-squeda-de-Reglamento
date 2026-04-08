# 🔍 Motor de Búsqueda con TF-IDF

## 📌 Descripción
Este proyecto implementa un motor de búsqueda basado en **TF-IDF (Term Frequency - Inverse Document Frequency)** que permite a estudiantes encontrar artículos relevantes dentro de un reglamento académico.

El sistema recibe una consulta en lenguaje natural y devuelve los documentos más relevantes ordenados por su puntuación (score).

---

## 🎯 Objetivo del Proyecto
Construir un motor de búsqueda que priorice los artículos más relevantes del reglamento académico utilizando el modelo TF-IDF, mejorando la precisión frente a una búsqueda simple por coincidencia de palabras.

---

## ❓ Problema
Una búsqueda tradicional:
- Solo encuentra coincidencias de palabras
- No mide la importancia de cada término
- Devuelve resultados poco relevantes

---

## 💡 Solución: TF-IDF

TF-IDF permite:
- Dar mayor peso a palabras importantes
- Reducir la influencia de palabras comunes
- Mejorar la calidad de los resultados

---

## ⚙️ ¿Cómo funciona?

### 1. TF (Term Frequency)
Mide qué tan frecuente es una palabra en un documento:


---

### 2. IDF (Inverse Document Frequency)
Mide qué tan importante es una palabra en todo el corpus:

---

### 3. Score TF-IDF
Se calcula sumando el TF-IDF de cada palabra de la consulta:

---

## 🛠️ Tecnologías utilizadas
- Python 3
- math
- collections (Counter)
- re (expresiones regulares)

---

## ▶️ Cómo ejecutar el proyecto

1. Clonar el repositorio:

2. Entrar a la carpeta del proyecto:

4. Ingresar una consulta en consola:

---

## 🧪 Ejemplos de ejecución

### 🔍 Consulta 1:


![Evidencia de ejecución del script](rag.png)

---

## 👨‍💻 Autor
- Jholman Camilo Diaz Osuna 

---

## 🚀 Conclusión

TF-IDF es una técnica fundamental en recuperación de información que permite mejorar significativamente la relevancia de los resultados frente a métodos simples.

Este proyecto demuestra cómo aplicar estos conceptos en un caso práctico y sirve como base para sistemas más avanzados como motores de búsqueda inteligentes y soluciones basadas en inteligencia artificial.

---
