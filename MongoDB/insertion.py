from pymongo import MongoClient
import pandas as pd
import re
import time

inicio_tiempo = time.time()

client = MongoClient("mongodb://localhost")
bd = client["Practica_dos"]

book_collection = bd["libros"]
author_collection = bd["autores"]

book_collection.delete_many({})
author_collection.delete_many({})

csv_path = 'books.csv'
df = pd.read_csv(csv_path, encoding='latin1', nrows=100, delimiter=';')

count = 0
for index, row in df.iterrows():
    autor = author_collection.find_one({'nombre_autor': {'$regex': re.compile(row['Book-Author'], re.IGNORECASE)}})

    if not autor:
        autor_result = author_collection.insert_one({'_id': count, 'nombre_autor': row['Book-Author']})
        id_autor = autor_result.inserted_id
        count = count + 1
    else:
        id_autor = autor['_id']

    libro = {
        'isbn': row['ISBN'],
        'título': row['Book-Title'],
        'año_edición': row['Year-Of-Publication'],
        'id_autor': id_autor
    }
    book_collection.insert_one(libro)

client.close()

fin_tiempo = time.time()
tiempo_ejecucion = fin_tiempo - inicio_tiempo

print(f"Tiempo de ejecución: {tiempo_ejecucion} segundos")