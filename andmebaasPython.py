from sqlite3 import *
from sqlite3 import Error

def create_connectrion (path):
    connection = None
    try:
        connection = connect(path)
        print("Ühendus on edukalt tehtud")
    except Error as e:
        print(f"Tekkis vig'{e}'")
    return connection
conn=create_connection("C:\Users\opilane\source\repos\andmebaasPython\AppData\data.db")


