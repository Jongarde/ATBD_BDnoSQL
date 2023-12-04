from pymongo import MongoClient

client = MongoClient("mongodb://localhost")
bd = client["Practica_dos"]
book_collection = bd['libros']
author_collection = bd['autores']
author_isbn_collection = bd["autor_isbn"]


def filter_by_year():
    book = book_collection.find_one({'año_edición': {'$gt': 2020}})
    autor = author_collection.find_one({'_id': book['id_autor']})
    return autor

def filter_by_title():
    book = book_collection.find_one({'título': {'$regex': '^The'}})
    autor = author_collection.find_one({'_id': book['id_autor']})
    return autor

def filter_by_ISBN(isbn = '0312261594'):
    book = book_collection.find_one({'isbn': isbn})
    autor = author_collection.find_one({'_id': book['id_autor']})
    return book, autor

result_5a_i = filter_by_year()
result_5a_ii = filter_by_title()
result_5b = filter_by_ISBN()

print("================================== Ejercicio 5a i ==================================")
print(result_5a_i)
print("================================== Ejercicio 5a ii ==================================")
print(result_5a_ii)
print("================================== Ejercicio 5b ==================================")
print(result_5b)