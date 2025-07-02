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
    value = input("Enter book id: ")
    query = "select * from Books where id = %s"
    mycursor.execute(query, (value,))
    result = mycursor.fetchone()
    if result:
        print(result)
    else: 
        print(f"No book found with id: {value}")
searchBook()

def listBooks():
    query = "Select * from Books"
    mycursor.execute(query)
    results = mycursor.fetchall()
    if results:
        for result in results:
            print(f"Books: {result}")
    else:
        print("No books in database")

listBooks()
mydb.commit()
mycursor.close()
mydb.close()