from .database import db
from .models import User, Cohort, Student

def init_db():
    db.connect()
    db.create_tables([User],safe = True)
    db.create_tables([Cohort],safe = True)
    db.create_tables([Student],safe = True)
    db.close()
    
def drop_table():
    db.connect(reuse_if_open=True)
    db.drop_tables([User],safe = True)
    db.drop_tables([Student],safe = True)
    db.drop_tables([Cohort],safe = True)
    db.close()
