import database 

# calling the functions from database.py

# add a record to the database
# database.add_one("Puchy", "Rios", "puchyrios@yahoo.com")

# delete a record from the database. (remeber to use rowid as string)
# database.delete_rec('6')

# add many records at once to the database
# new_data = [
#       ('Angel', 'Gonzalez', 'angelgonz@hotmail.com'),
#       ('Tito', 'Sanchez', 'titosanch@gmail.com'),
#       ('Alex', 'Reyes', 'alexreyes@new.com'),
# ]
# database.add_many(new_data)

# lookup the email address records
database.find_email('domi.zulu@yahoo.com')

# show all the records
# database.show_all()