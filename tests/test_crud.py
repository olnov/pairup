from app.db.crud import create_user, get_user_by_id, authenticate_user, create_cohort, get_cohorts, get_cohort_by_id
from app.db.init_db import init_db, drop_table
from app.db.models import Cohort
from datetime import date


"""
Test creating new user
"""

def test_create_user():
    drop_table()
    init_db()
    create_user(first_name='John',second_name='Doe',email='john@doe.com',password='password!1')
    app_user=get_user_by_id(user_id=1)
    assert app_user.first_name=='John'
    assert app_user.second_name=='Doe'
    assert app_user.email=='john@doe.com'

"""
Test user authentication
"""
def test_user_auth():
    assert authenticate_user(email='john@doe.com',password='password!1')==True


"""
Test create cohort
"""
def test_create_cohort():
    drop_table()
    init_db()
    create_cohort(title='May 2024',date_start=date(2024,5,1),date_end=date(2024,9,1))
    cohort = get_cohort_by_id(1)
    assert cohort.title == 'May 2024'
    assert cohort.date_start == date(2024,5,1)
    assert cohort.date_end == date(2024,9,1)
    
"""
Test get all cohorts
"""
def test_get_cohorts():
    drop_table()
    init_db()
    create_cohort(title='May 2024',date_start=date(2024,5,1),date_end=date(2024,9,1))
    create_cohort(title='July 2024',date_start=date(2024,7,1),date_end=date(2024,11,1))
    cohorts = get_cohorts()
    print (f"Cohorts: {cohorts}")
    assert cohorts[0].title == 'May 2024'
    assert cohorts[0].date_start == date(2024,5,1)
    assert cohorts[0].date_end == date(2024,9,1)
    assert cohorts[1].title == 'July 2024'
    assert cohorts[1].date_start == date(2024,7,1)
    assert cohorts[1].date_end == date(2024,11,1)     
    