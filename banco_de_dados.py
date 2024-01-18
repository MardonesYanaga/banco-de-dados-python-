import sqlite3

connect = sqlite3.connect('meu_bd.db')
cursor = connect.cursor()

nome = input ('digite seu nome')
idade = int (input('Digite sua idade '))


cursor.execute(f"INSERT INTO pessoas  VALUES('{nome}', {idade})")
connect.commit()