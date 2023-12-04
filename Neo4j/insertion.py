from neo4j import GraphDatabase
import pandas as pd

import time
inicio_tiempo = time.time()

uri = "neo4j://localhost:7687"  
username = "neo4j"  
password = "master22"

df = pd.read_csv('books.csv', encoding='latin1', nrows=100, delimiter=';')

driver = GraphDatabase.driver(uri, auth=(username, password))

id_count = 0
with driver.session() as session:
	for index, row in df.iterrows():
		autor_query = (
		"MATCH (autor:Autores {nombre_autor: $nombre_autor}) "
		"RETURN id(autor) as id_autor"
		)
		autor_result = session.run(autor_query, nombre_autor=row['Book-Author'])
		autor_record = autor_result.single()

		if not autor_record:

			session.run("MERGE (autor:Autores {id_autor: $id_autor, nombre_autor: $nombre_autor})", id_autor=id_count, nombre_autor=row['Book-Author'])
			session.run("CREATE (libro:Libros {isbn: $isbn, titulo: $titulo, año_edicion: $anyo_edicion})", isbn=row['ISBN'], titulo=row['Book-Title'], anyo_edicion=row['Year-Of-Publication'])
			session.run("MATCH (autor:Autores), (libro:Libros) WHERE autor.nombre_autor = $nombre_autor AND libro.isbn = $isbn CREATE (autor)-[:ESCRIBIR]->(libro)", nombre_autor=row['Book-Author'], isbn=row['ISBN'])
			id_count += 1

# Cerrar la conexión
driver.close()

fin_tiempo = time.time()
tiempo_ejecucion = fin_tiempo - inicio_tiempo

print(f"Tiempo de ejecución: {tiempo_ejecucion} segundos")
