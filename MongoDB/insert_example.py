from pymongo import MongoClient

client = MongoClient("mongodb://localhost")
bd = client["Practica_dos"]

book_collection = bd["libros"]

libro = {
    'isbn': '0123456789',
    'título': "Libro insertado",
    'año_edición': 2021,
    'id_autor': 57
}

book_collection.insert_one(libro)

client.close()