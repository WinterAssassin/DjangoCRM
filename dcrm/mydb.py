import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Tqbfjotld!007'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE crm_database")
