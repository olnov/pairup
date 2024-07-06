from peewee import Model, CharField, IntegerField, DateField, ForeignKeyField, AutoField
import bcrypt
from .database import db

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    first_name = CharField(max_length=50)
    second_name = CharField(max_length=50)
    email = CharField(max_length=100)
    password_hash = CharField()
    
    class Meta:
        table_name='users'
    
    def set_password(self, password:str):
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        
    def check_password(self, password:str)->bool:
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash.encode('utf-8'))    

class Cohort(BaseModel):
    co_id = AutoField()
    title = CharField(max_length=50)
    date_start = DateField()
    date_end = DateField()
    
    class Meta:
        table_name = 'cohorts'
        
class Student(BaseModel):
    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50)
    cohort_id = ForeignKeyField(Cohort, column_name = 'co_id')
    skill_level = IntegerField()
    
    class Meta:
        table_name = 'students'