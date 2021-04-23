import sqlite3

try:
    sqlite_Connection = sqlite3.connect('temp.db')
    conn = sqlite_Connection.cursor()
    print("\nDatabase created and connected to SQLite")

except sqlite3.Error as error:
    print("\nError while connecting to sqlite", error)
