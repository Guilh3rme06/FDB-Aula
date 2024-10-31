import sqlite3

# Conexão com a base de dados 'escola.db'
conexao = sqlite3.connect('carros.db')

# Criação de um cursor para executar comandos SQL
cursor = conexao.cursor()

cursor.execute('''
 CREATE TABLE IF NOT EXISTS marcas (
   id INTEGER PRIMARY KEY,
   marca TEXT,
   modelo TEXT
   )
''')

cursor.execute('''
 CREATE TABLE IF NOT EXISTS compradores (
   id INTEGER PRIMARY KEY,
   nome TEXT,
   valor integer,
   mes TEXT
   )
''')

cursor.execute('''
 INSERT INTO marcas (marca, modelo)
 VALUES ('Lamborghini', 'Aventador')
''')

cursor.execute('''
 INSERT INTO compradores (nome, valor, mes )
 VALUES ('Guilherme', '5000000', 'Novembro')
''')

conexao.commit()

cursor.execute('SELECT * FROM marcas')
resultados_marcas = cursor.fetchall()

cursor.execute('SELECT * FROM compradores')
resultados_compradores = cursor.fetchall()

for linha in resultados_marcas:
 print(linha)

for linha in resultados_compradores:
 print(linha)


conexao.close()
