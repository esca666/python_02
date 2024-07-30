import mysql.connector

connection = mysql.connector.connect(
    database ="student" , user="root", password = "" ,host = "localhost", port = 3306
)
_cursor = connection.cursor()
_cursor.execute(    "CREATE TABLE employee (eid INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(100) NOT NULL,phone VARCHAR(15) NOT NULL);")

# _cursor.execute("INSER")
connection.close()