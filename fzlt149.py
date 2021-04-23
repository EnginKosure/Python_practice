import sqlite3

try:
    sqlite_Connection = sqlite3.connect('temp.db')
    conn = sqlite_Connection.cursor()
    print("\nDatabase created and connected to SQLite")
    sqlite_select_Query = "select sqlite_version();"
    conn.execute(sqlite_select_Query)


except sqlite3.Error as error:
    print("\nError while connecting to sqlite", error)
