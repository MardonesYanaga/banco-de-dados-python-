import sqlite3


connection = sqlite3.connect('newdatabase.db')
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS persons(
    id PRIMARY KEY, 
    first_name TEXT,
    laste_name TEXT,
    age INTEGER)
""")
cursor.execute("""
INSERT INTO persons VALUES 
(1,'carlols','antonio',60),
(2,'joão', 'antonio',18),
(3,'joelma','vitoria',26)
""")
connection.commit()
connection.close()
class Person:
    def __init__(self,id=-1, first="", last="", age=-1):
        self.id = id
        self.first = first
        self.last = last
        self.age = age
        self.connection = sqlite3.connect('newdatabase.db')
        self.cursor = self.connection.cursor()


    def load_person(self, id):
        self.cursor.execute("""
        SELECT* FROM persons 
        WHERE id={}
        """.format(id))
        results = self.cursor.fetchone()

        self.id = id
        self.first = results[1]
        self.last = results[2]
        self.age = results[3]

    def inserindo_person(self):
        self.cursor.execute("""
        INSERT INTO persons VALUES
        ({},'{}','{}',{})
        """.format(self.id, self.first, self.last, self.age))

        self.connection.commit()
        self.connection.close()


p1 = Person(7,"Alex","parana",30)
p1.inserindo_person()

connection = sqlite3.connect('newdatabase.db')
cursor = connection.cursor()
cursor.execute("SELECT* FROM persons")
results = cursor.fetchall()
print(results)
connection.close()



