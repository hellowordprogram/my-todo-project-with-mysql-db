import mysql.connector

conn = mysql.connector.connect(
    host = "sql12.freesqldatabase.com",
    port = 3306,
    username = "sql12791045",
    password = "NBB8lXGiZP",
    database = "sql12791045"
)

csr = conn.cursor()