from flask import Flask, render_template, request, redirect, session, abort
from app.db.crud import authenticate_user
from app.db.models import Student, Cohort
from peewee import *

app=Flask(__name__)
app.config['SECRET_KEY']='1b973299943650f6c7daf012'

@app.route("/login", methods=['GET','POST'])
def login():
    if request.method=='POST':
        email=request.form['email']
        password=request.form['password']
        if not authenticate_user(email=email, password=password):
            error="Username or password is incorrect"
            return render_template("login.html",error=error)
        else:
            session['logged_in']=True
            session['user_id']=email
            return redirect("/admin")
    else:
        return render_template("login.html")

@app.route('/logout')
def logout():
    if 'logged_in' in session:
        session.pop('logged_in')
    return redirect("/login")

@app.route("/admin", methods=['GET'])
def admin():
    if 'logged_in' not in session:
        abort(403)
    user=session["user_id"]
    return render_template ("admin.html",user=user)

@app.route("/students", methods=['GET'])
def students():
    if 'logged_in' not in session:
        abort(403)
    user=session["user_id"]
    query = Student.select(Student.first_name, Student.last_name, Cohort.title, Student.skill_level).join(Cohort).where(Student.cohort_id == Cohort.co_id).dicts()
    students=[]
    for row in query:
        students.append(row)
    return students

if __name__ == '__main__':
    app.run(debug=True, port=5050, host='0.0.0.0')    