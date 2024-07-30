#database
import sqlite3 #file based database

connection = sqlite3.connect('cars.db')
_cursor = connection.cursor()
try:
    _cursor.execute("create table  car (name,brand,color)")
except sqlite3.OperationalError as e:
    print(str(e))
    pass
_cursor.execute("insert into car values ('Hurrican','lamborghini','black')")
result =_cursor.execute('select * from car')
print(result)
for row in result:
    print(row)
connection.commit()