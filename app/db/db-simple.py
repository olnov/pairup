from peewee import *
from datetime import date

# Configuration settings
DATABASE = {
    'name': 'pairup-dev',        
    'user': 'postgres',            
    'password': 'ujylehfc!1',    
    'host': 'localhost',          
    'port': 5432,                 
}

# Initialize the database connection
db = PostgresqlDatabase(
    DATABASE['name'],
    user=DATABASE['user'],
    password=DATABASE['password'],
    host=DATABASE['host'],
    port=DATABASE['port']
)


class Person(Model):
    name = CharField()
    birthday = DateField()

    class Meta:
        database = db # This model uses the "people.db" database.
        
def init_db():
    db.connect()
    db.create_tables([Person])
    db.close()
    return "Table created"


print(init_db())
oleg=Person(name='Oleg', birthday=date(1980,6,26))
oleg.save()