import sqlite3

connection = sqlite3.connect('movies.db')

cursor = connection.cursor()

# cursor.execute('''
# CREATE TABLE IF NOT EXISTS Movies(Title TEXT, Director TEXT, Year INT)
# ''')


# famous_films = [('Pulp Fiction', 'Quentin Tarantino', 1994),
#                 ('Back to the Future', 'Steven Spielberg', 1985),
#                 ('Moonrise Kingdom', 'Wes Anderson', 2012)]
# cursor.execute(
#     "INSERT INTO Movies VALUES ('Taxi Driver', 'Martin Scorsese', 1995)")

# cursor.executemany('Insert INTO Movies VALUES (?,?,?)', famous_films)

# records = cursor.execute("SELECT * FROM Movies")

# print(cursor.fetchall())

# for record in records:
#     print(record)

release_year = (1985,)

cursor.execute("SELECT * FROM Movies WHERE year=?", release_year)

print(cursor.fetchall())

connection.commit()
connection.close()
