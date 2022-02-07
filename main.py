import sqlite3

# before i do anything i need to create a connection to the database.
# i do this by creating a variable and make it equal to sqlite3.connect()
# now inside the .connect() i want to pass in the name of the database i want to create
conn = sqlite3.connect('customer.db')
# when i run the bove line of code in the terminal, it will create a db file for customer

# Create a DataBase Table
# a table is like an excel sheet with rows and columns
# to create a table in sqlite3 i first need to make a cursor
# the cursor tells the database what you want to do

# i start by making a cursor variable with a cursor instance.
# this will allow me to do all kinds of things.
cursor = conn.cursor()

# now i will create a table 
# i need to use the .execute function to pass in the docstring where-
# i will put my data.
# then i need to define where i want to put my rows and columns 

# QUICK Note: sqlite3 is case sensetive do the caps matter.

# i need to define the DATATYPE for each thing i want to put in the table. 
# sqlite3 only has 5 datatypes i can choose from. (NULL, INTEGER, REAL, TEXT, BLOB)
# NULL = Does it exist 
# INTEGER = whole number 
# REAL = decimal number 
# TEXT = words
# BLOB = image, mp3 file, ect

# cursor.execute("""CREATE TABLE customers (
#         first_name text,
#         last_name text,
#         email text 
#   )""")

# i can update records as well. 
# i god way of doing this is by using the rowid to look for the data you i want updated.
# cursor.execute("""UPDATE customers SET first_name = 'Dominique'
#                WHERE rowid = 3
#                 """)

# i can easily delete a row using DELETE
# cursor.execute("DELETE from customers WHERE rowid = 5")

# now that i have created the table, i can put data into the table.
# i use the sql command INSERT TO
# now i have one row in my table
# cursor.execute("INSERT INTO customers VALUES ('Leo', 'Muntaner', 'leo.muntaner@yahoo.com')")
# cursor.execute("INSERT INTO customers VALUES ('John', 'Doe', 'john.doe@hotmail.com')")
# cursor.execute("INSERT INTO customers VALUES ('Dominique', 'Zuluaga', 'domi.zulu@yahoo.com')")
# after executing the three lines of code, i now have 3 records in my database

# i added those records one at a time. now i will insert many records into the table at once,
# i start by creating variable that is a list data structure
# inside this list i can make individual items i want to store!
# many_customers = [
#                   ('Wes', 'Brown', 'wes@brown.com'), 
#                   ('Steph', 'Curry', 'steph@curry.com'), 
#                   ('Dan', 'White', 'dan@white.com'),
#                 ]

# now i want to use the .executemany() function. 
# inside the function i will include a tuple with placeholders which will be the '?'
# the '?' stand for first, last, email.
# then i will pass the name of my list variable

# cursor.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)

# now that i have put a bunch of data into the database, i want to display it
# query the database by using the SELECT command. i included the '*' which-
# means i want to see everything FROM the customers table.
# by adding the rowid, i get the primary key for the rows
# if i want to look for something i can use the WHERE last_name = 'Zuluaga'
# i can use the LIKE 'Br%' that searches things that start with the letters Br.

# cursor.execute("SELECT * FROM customers WHERE last_name = 'Zuluaga'")
# cursor.execute("SELECT * FROM customers WHERE last_name LIKE 'Br%' ")
# cursor.execute("SELECT * FROM customers WHERE email LIKE '%yahoo.com' ")

# cursor.execute("SELECT rowid, * FROM customers")

# orders in descending fashion
# cursor.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC")

# orders in alphabetical order of last name.
cursor.execute("SELECT rowid, * FROM customers ORDER BY last_name")


# now i use the .fetch() function to specify what i want to get
# .fetchone() gets the first item in the table. 
# .fetchmany(3) gets the first three
# .fetchall() gets everything
# i need to wrap it all into a print function so that it shows when i run the program
# (the contents can be accessed using [] because its a tuple)
# this is all returned as a python list.

# print(cursor.fetchone())
# print(cursor.fetchall())
# print(cursor.fetchmany(3))

# by assigning .fetchall() to the variable items, i can now use a simple-
# for loop to print out the contents one line at a time.
items = cursor.fetchall()
for item in items:
  # i can use the [] to be more accurate on what i wan to print.
  # for ex: [0] will show the first name for everyone in my database
  # i could go even further and concatinate first, last, email name by adding + [1] + [2]
  # print(item[0])
  print(item)


# print('Command executed succesfully...')
# now after i have made the cursor command from the code above-
# i need to commit this to the database. i do this by commiting the connection
# now my data is pushed into the database.
conn.commit()

# now i need to close my connection (this is best practice)
conn.close()