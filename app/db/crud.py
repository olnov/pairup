from datetime import datetime, date
from .models import User, Cohort, Student

# Create a new user with a hashed password
def create_user(first_name:str, second_name: str, email: str, password: str) -> User:
    user = User(first_name=first_name, second_name=second_name, email=email)
    user.set_password(password)
    user.save()
    return user

# Get a user by ID
def get_user_by_id(user_id: int) -> User:
    user = User.get(User.id == user_id)
    return user

# Authenticate a user
def authenticate_user(email: str, password: str) -> bool:
    try:
        user = User.get(User.email == email)
        return user.check_password(password)
    except User.DoesNotExist:
        return False

# Create a new cohort
def create_cohort(title:str, date_start:date, date_end:date) -> Cohort:
    cohort = Cohort(title = title, date_start = date_start, date_end = date_end)
    cohort.save()

# Get all cohorts    
def get_cohorts():
    cohorts = [cohort for cohort in Cohort.select()]
    return cohorts

# Get cohort by id
def get_cohort_by_id(cohort_id:int) -> Cohort:
    cohort = Cohort.get(Cohort.co_id == cohort_id)
    return cohort