import MySQLdb
# open mysql
db = MySQLdb.connect("localhost","root",'123456','test')

# get cursor
cursor = db.cursor()
# create a table
# sql = "create table employee(id INT PRIMARY KEY ,name CHAR (20) NOT NULL ,age INT ,sex CHAR (1),income FLOAT )"
# cursor.execute(sql)

# insert data
sql = """insert into user(id,user) VALUES (3,'Tom')"""
try:
    cursor.execute(sql)
    db.commit()
except Exception,e:
    print e
    db.rollback()

db.close()