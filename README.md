# 🔍 Motor de Búsqueda con TF-IDF

## 📌 Descripción
Este proyecto implementa un motor de búsqueda basado en **TF-IDF (Term Frequency - Inverse Document Frequency)** que permite a estudiantes encontrar artículos relevantes dentro de un reglamento académico.

El sistema recibe una consulta en lenguaje natural y devuelve los documentos más relevantes ordenados por su puntuación.

---

## 🎯 Objetivo
Construir un motor de búsqueda que priorice los artículos más relevantes del reglamento académico utilizando el modelo TF-IDF en lugar de una búsqueda simple por palabras.

---

## 🚀 ¿Por qué usar TF-IDF?

Una búsqueda tradicional:
- Solo encuentra coincidencias de palabras
- No mide la importancia de cada término
- Puede devolver resultados poco relevantes

TF-IDF permite:
- Dar mayor peso a palabras importantes
- Reducir la influencia de palabras comunes
- Mejorar la precisión de los resultados

---

## ⚙️ ¿Cómo funciona?

### 1. TF (Term Frequency)
Mide qué tan frecuente es una palabra en un documento:
