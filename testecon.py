import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="teste"
)

cursor = conexao.cursor()

cursor.close()
conexao.close()
