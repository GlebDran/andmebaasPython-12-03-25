from sqlite3 import *
from sqlite3 import Error

def create_connection(path):
    connection = None
    try:
        connection = connect(path)
        print("Ühendus on edukalt tehtud")
    except Error as e:
        print(f"Tekkis vig'{e}'")
    return connection
conn=create_connection(r"data.db")

def execute_query(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Tabel on loodud või andmed on sisestatud")
    except Error as e:
        print(f"Viga'{e}' tabeli loomisega")

create_users_table= """
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
age INTEGER,
gender TEXT,
nationality TEXT
);
"""
execute_query(conn, create_users_table)

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"Viga'{e}'")

create_users = """
INSERT INTO
    users (name, age, gender, nationality)
VALUES
    ('Mati', 25, 'mees', 'USA'),
    ('Marina', 30, 'naine', 'Eesti'),
    ('Gleb', 30, 'mees', 'Vene'),
    ('Irina', 35, 'naine', 'Prantsusmaa');
    """
execute_query(conn, create_users)

select_users ="SELECT * from users"

users = execute_read_query(conn, select_users)
for user in users:
    print(user)

def add_users_query(connection, user_data):
    query="INSERT INTO users(name,age,gender,nationality) VALUES("+user_data+")"
    execute_query(connection, query)

insert_user="'"+input("Nimi: ")+"','"+input("Vanus: ")+"','"+input("Sugu: ")+"','"+input("Riik:")+"'"

add_users_query(conn, insert_user)

def add_users_query_2(connection, user_data):
    """Lisame userit, mis on eralid sisestatud"""
    query="INSERT INTO users(name,age,gender,nationality) VALUES(?,?,?,?)"
    cursor=connection.cursor()
    cursor.execute(query, user_data)
    connection.commit()

insert_user=(input("Nimi: "),int(input("Vanus: ")), input("Sugu: "), input("Riik: "))
print(insert_user)
add_users_query_2(conn, insert_user)

def delete_data_from_tabel(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Andmed on kustutatud")
    except Error as e:
        print(f"Viga'{e}' andmete kustutamisega")

print("Andmete kustutame tabelist 'users'")
delete_data_from_users="DELETE FROM users WHERE age<30"
delete_data_from_tabel(conn,delete_data_from_users)
print("Tabelis 'users' on jäänud neid kes vanem kui 30:")
users = execute_read_query(conn, select_users)

for users in users:
    print(user)

create_gender_tabel="""
CREATE TABLE IF NOT EXISTS gender(
Id INTEGER PRIMARY KEY AUTOINCREMENT,
Nimetus TEXT NOT NULL)"""

insert_gender="""
INSERT INTO
gender(Nimetus)
VALUES
('mees')
('naine')
"""
create_users_table2="""
CREATE TABLE IF NOT EXISTS users2(
Id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
Lname TEXT NOT NULL,
Age INTEGER NOT NULL,
GenderID INTEGER,
FOREIGN KEY (GenderId) REFERENCES gender (Id)
"""
insert_users2="""
INSERT INTO
users2(Name,Lname,Age,GenderID)
VALUES
('Mati, 'Tamm', 50, 1),
('Kati, 'Kask', 54, 2)"""

