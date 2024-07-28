from flask import Flask, render_template, request, redirect, session, abort, url_for
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
    return render_template ("admin/admin.html",user=user)

@app.route("/cohorts", methods = ["GET"])
def cohorts():
    if 'logged_in' not in session:
        abort(403)
    user=session["user_id"]
    query = Cohort.select(Cohort.title, Cohort.date_start, Cohort.date_end).dicts()
    cohorts = []
    for row in query:
        cohorts.append(row)
    # return cohorts
    return render_template("admin/admin-cohorts.html", user=user, cohorts=cohorts)

@app.route("/cohorts", methods = ["POST"])
def add_cohort():
    if 'logged_in' not in session:
        abort(403)
    user=session["user_id"]
    title = request.form['title']
    date_start = request.form['date_start']
    date_end = request.form['date_end']
    Cohort.create(title = title, date_start = date_start, date_end = date_end)
    return redirect(url_for('cohorts'))

@app.route("/students", methods=['GET'])
def students():
    if 'logged_in' not in session:
        abort(403)
    user=session["user_id"]
    query = Student.select(Student.first_name, Student.last_name, Cohort.title, Student.skill_level).join(Cohort).where(Student.cohort_id == Cohort.co_id).dicts()
    students=[]
    for row in query:
        students.append(row)
    # return students
    return render_template("admin/admin-students.html", user=user, students=students)

if __name__ == '__main__':
    app.run(debug=True, port=5050, host='0.0.0.0')    