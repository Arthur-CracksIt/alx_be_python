import mysql.connector

mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "Protocol11#@ip.com", database="Library")

mycursor = mydb.cursor()

# mycursor.execute("""
#                 Create Table if not exists Books(id int auto_increment primary key, title varchar(255) not null, author varchar(255) not null,
#                  ISBN varchar(255))
#                  """)
# mydb.commit()
# print("Books Table created")

# sql = "Insert into Books(id, title, author, ISBN) Values(%s, %s, %s, %s)"
# values = (2, "Merlin", "Kojo Musra", "11223345")
# mycursor.execute(sql, values)
# mydb.commit()

def searchBook():
    query = input("Enter your search book sql query...In sql format: ")
    mycursor.execute(query)
    result = mycursor.fetchone()
    print(result)
searchBook()