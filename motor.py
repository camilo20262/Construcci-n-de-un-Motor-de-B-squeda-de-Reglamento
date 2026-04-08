import math
import re
from collections import Counter


# PASO 1: DATASET

documentos = [
    "Artículo 15: La pérdida de cupo ocurre por promedio inferior a 3.0 o falta disciplinaria grave.",
    "Artículo 22: El estudiante tiene derecho a solicitar supletorios en los tres días siguientes a la falta.",
    "Artículo 45: Las becas por excelencia académica se otorgan al promedio más alto de cada facultad.",
    "Artículo 50: La cancelación de semestre debe hacerse antes de la semana 10 del calendario académico.",
    "Artículo 12: Las faltas disciplinarias se dividen en leves, graves y gravísimas según el manual.",
    "Artículo 30: El estudiante podrá cancelar materias dentro de las primeras semanas del semestre.",
    "Artículo 18: La beca socioeconómica se otorga a estudiantes con dificultades económicas comprobadas.",
    "Artículo 60: Las faltas graves incluyen plagio académico y suplantación de identidad.",
    "Artículo 70: El proceso disciplinario inicia con notificación formal al estudiante.",
    "Artículo 80: El estudiante puede apelar sanciones ante el comité académico."
]

# PASO 2: PREPROCESAMIENTO

def tokenizar(texto):
    texto = texto.lower()
    texto = re.sub(r"[^a-z0-9\s]", "", texto)
    return texto.split()

# TF: frecuencia / total palabras

def calcular_tf(tokens):
    total = len(tokens)
    conteo = Counter(tokens)
    return {palabra: conteo[palabra] / total for palabra in conteo}


# IDF: log(N / docs_con_palabra)

def calcular_idf(corpus):
    N = len(corpus)
    idf = {}

    palabras = set(p for doc in corpus for p in doc)

    for palabra in palabras:
        docs_con_palabra = sum(1 for doc in corpus if palabra in doc)
        idf[palabra] = math.log(N / docs_con_palabra)

    return idf


# SCORE: suma TF-IDF

def calcular_score(query_tokens, tf_doc, idf):
    return sum(tf_doc.get(p, 0) * idf.get(p, 0) for p in query_tokens)


# MOTOR DE BÚSQUEDA

def buscar(consulta, documentos, top_n=3):
    corpus = [tokenizar(doc) for doc in documentos]
    idf = calcular_idf(corpus)
    query_tokens = tokenizar(consulta)

    resultados = []

    for i, doc_tokens in enumerate(corpus):
        tf = calcular_tf(doc_tokens)
        score = calcular_score(query_tokens, tf, idf)

        resultados.append({
            "documento": documentos[i],
            "score": score
        })

    # ordenar por score descendente
    resultados.sort(key=lambda x: x["score"], reverse=True)

    return resultados[:top_n]


# EJECUCIÓN (PRUEBA)

def main():
    print("=== MOTOR DE BÚSQUEDA TF-IDF ===")

    while True:
        consulta = input("\nConsulta (o 'salir'): ")

        if consulta.lower() == "salir":
            print("Fin del programa.")
            break

        resultados = buscar(consulta, documentos)

        print("\nResultados:")
        for r in resultados:
            print(f"\nScore: {r['score']:.4f}")
            print(r["documento"])

if __name__ == "__main__":
    main()