import sqlite3

# this function will query the database and return all records:
def show_all():
  # connect to database
  conn = sqlite3.connect('customer.db')
  # create a cursor
  cursor = conn.cursor()
  
  # Query the database 
  cursor.execute("SELECT rowid, * FROM customers")
  
  items = cursor.fetchall()
  for item in items:
    print(item)
  
  # commit my command 
  conn.commit()

  # close my connection
  conn.close()
  
# function that adds a new record to the table:
# takes in the first/last name and email as its parameters
def add_one(first,last,email):
  # connect to database
  conn = sqlite3.connect('customer.db')
  # create a cursor
  cursor = conn.cursor()
  
  # sql command to add into the table what i want.
  cursor.execute("INSERT INTO customers VALUES (?,?,?)", (first,last,email))
  
  # commit my command 
  conn.commit()
  # close my connection
  conn.close()
  
# function that deletes a record from the table:
def delete_rec(id):
  # connect to database
  conn = sqlite3.connect('customer.db')
  # create a cursor
  cursor = conn.cursor()
  
  # sql command to delete from the record based on the parameter 
  cursor.execute("DELETE from customers WHERE rowid = (?)", id)
  
  # commit my command 
  conn.commit()
  # close my connection
  conn.close()
  
# function that adds many records to the table:
def add_many(list):
  # connect to database
  conn = sqlite3.connect('customer.db')
  # create a cursor
  cursor = conn.cursor()
  
  # sql command to add into the table what i want.
  cursor.executemany("INSERT INTO customers VALUES (?,?,?)", (list))
  
  # commit my command 
  conn.commit()
  # close my connection
  conn.close()
  
# function that uses the WHERE to lookup emails
def find_email(email):
  # connect to database
  conn = sqlite3.connect('customer.db')
  # create a cursor
  cursor = conn.cursor()
  
  # sql command to lookup emails from the table.
  # since its a tuple i need the email parameter in paranthesis and a comma.
  cursor.execute("SELECT * from customers WHERE email = (?)", (email,))
  
  # this will loop through all the emails
  items = cursor.fetchall()
  for item in items:
    print(item)
  
  
  # commit my command 
  conn.commit()
  # close my connection
  conn.close()