from pymongo import MongoClient

client = MongoClient("mongodb://localhost")
db = client['Practica_dos']
autores_collection = db['autores']

def from_min_to_mayus(id):
    autor = autores_collection.find_one({'_id': id})
    nom_mayus = autor['nombre_autor'].upper()
    autores_collection.update_one(
        {'_id': id},
        {'$set': {'nombre_autor': nom_mayus}}
    )

from_min_to_mayus(0)

from_min_to_mayus(1)

client.close()