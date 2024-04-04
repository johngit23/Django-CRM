import mysql.connector as mysql

dataBase = mysql.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Yohannes@23',
)

cursor = dataBase.cursor()

cursor.execute('CREATE DATABASE IF NOT EXISTS dcrm')

print('AllDone!')