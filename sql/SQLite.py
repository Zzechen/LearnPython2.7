# because SQLite driver is in Python stander library,we can use it operate directly

# import SQLite driver
import sqlite3

# connect to SQLite,the file is 'test.db',if the file doesn't exist,the api will create the file
conn = sqlite3.connect('test.db')

# # create a Cursor
# cursor = conn.cursor()
#
# # exect a sql statement to create a table(user)
# cursor.execute('create table user(id VARCHAR(20) PRIMARY KEY ,name VARCHAR(20))')
#
# # insert one record
# cursor.execute('insert into USER (id,name) VALUES (\'1\',\'Michael\')')
#
# # get the line of the insert record
# print cursor.rowcount
#
# # close the cursor
# cursor.close()
#
# # commit the transaction
# conn.commit()
#
# # close the connection
# conn.close()

# select the data from user table
# get the cursor
cursor = conn.cursor()

# select all
cursor.execute('SELECT * FROM user')

# get a list
values = cursor.fetchall()
print values

