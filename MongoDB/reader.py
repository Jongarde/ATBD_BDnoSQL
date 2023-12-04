from pymongo import MongoClient

client = MongoClient("mongodb://localhost")
bd = client["Practica_dos"]

book_collection = bd["libros"]
author_collection = bd["autores"]

print("=========================== Libros ===========================")
for book in book_collection.find():
    print(book)

print("=========================== Autores ===========================")
for author in author_collection.find():
    print(author)

client.close()