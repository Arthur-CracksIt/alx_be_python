import mysql.connector

db = mysql.connector.connect(host= "localhost", user= "root", passwd= "Protocol11#@ip.com", database = "Students")

# print(db.server_info)

mycursor = db.cursor() #to enable you scroll over the database/ walk through your database

# mycursor.execute("select * from Students")
# result = mycursor.fetchall()
# for i in result:
#     print(i)

# mycursor.close()
# db.close()

#running my hands on it
# script = "INSERT INTO Students(StudentId, firstName, secondName, email, hometown, age) Values(%s, %s, %s, %s, %s, %s)"
# values = ('21123458', 'Emmanuel', 'Kwarko', 'emma.3@hotmail.com', 'bogoso', 23)

# update = "UPDATE Students set firstName = %s where StudentId = %s"
# # val = ("Percy", '20750963')
# # mycursor.execute(update, val)
# # # db.commit()
# query = "select * from Students where StudentId = %s"
# value = '20750963',
# mycursor.execute(query, value)
# result = mycursor.fetchall()
# for i in result:
#     print(i)
# db.commit()
mycursor.execute("""
                 CREATE TABLE IF NOT EXISTS studentCourse(courseid int auto_increment primary key, studentId char(8), courseTitle varchar(50) not null) """)
print("Table created")

sql = "INSERT INTO studentCourse(courseid, studentId, courseTitle) Values(%s, %s, %s)"
values = (2, "27531130", "CSM5023")
mycursor.execute(sql, values)
db.commit()

print(mycursor.rowcount, "records inserted succesfully")

mycursor.execute("Select * from studentCourse")
result = mycursor.fetchall()
for i in result:
    print(i)




