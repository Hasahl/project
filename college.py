College.py
# import
from unicodedata import name
from urllib import request
from flask import Flask,render_template,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

# config
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydata.db'
db = SQLAlchemy(app)

# Schema
class College(db.Model):
    id = db.Column(db.Integer,primary_Key=True)
    name = db.Column(db.String)
    address = db.Column(db.String)
    department = db.relationship('Department',backref='all_departments')

class Department(db.Model):
    id = db.Column(db.Integer,Primary_Key=True)
    name = db.Column(db.String)
    description = db.column(db.String)
    College = db.column(db.ForeignKey('college.id')) 
    course = db.relationship('Course',backref='all_courses')

class Courses(db.Model):
    id = db.Column(db.Integer,Primary_Key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    mob = db.Column(db.String)
    department = db.Column(db.ForeignKey('department.id'))
    Semester = db.relationship('Semester',backref='all_semesters')

class Semester(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String)
    relation = db.Column(db.String)
    Course = db.Column(db.ForeignKey('course.id'))
    student = db.relationship('Student',backref='all_students')

class Students(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String)
    mob = db.Column(db.String)
    Semester = db.Column(db.ForeignKey('semester.id'))
   
    # DB execution
db.create_all()
c1 = College(id=1,name='khracademy',address='london')
db.session.add(c1)
db.session.commit()
d1 = Department(id=1,name='HR',description='Hiring & Management',College=1)
d2 = Department(id=2,name='Admin',description='Registration',College=2)
d3 = Department(id=3,name='IT',description='support',College=3)
db.session.add(d1)
db.session.add(d2)
db.session.add(d3)
db.session.commit()
e1 = Courses(id=1,name='Physics',email='physics@demo.com',mob='999998',department=2)
e2 = Courses(id=2,name='Chemistry',email='Chemistry@demo.com',mob='977999',department=1)
e3 = Courses(id=1,name='Mathematics',email='Maths@demo.com',mob='999998',department=2)
e4 = Courses(id=2,name='Geography',email='Geo@demo.com',mob='977999',department=1)
db.session.add(e1)
db.session.add(e2)
db.session.add(e3)
db.session.add(e4)
db.session.commit()
dd1 = Semester(id=1,name='halfterm',relation='Half')
dd2 = Semester(id=2,name='Fullterm',relation='Full')
db.session.add(dd1)
db.session.add(dd2)
db.session.commit()
dd1 = Semester(id=1,name='Steve',gender='M',email='steve@demo.com',mob='7546799')
dd2 = Semester(id=2,name='Becky',gender=,'F',email='Becky@demo.com',mob='93215678')
dd1 = Semester(id=1,name='Harry',gender='M',email='Harry@demo.com',mob='8764326')
dd2 = Semester(id=2,name='Lina',gender='F',email='Lina@demo.com',mob='7453278')
db.session.add(dd1)
db.session.add(dd2)
db.session.commit()

#Read operation
# all_college = College.query.all()
# cal_college = College.query.filter_by(address)= london )
# for com in all_college:
    print(com.id,com.name)
# com2 = college.query.get(2)
# print(com2.id.com2.name.com2.address)

#update operation
# cc1 = College.query.get(1)
# cc2 = College.query.get(2)
# cc1.address = 'london'
# cc2.address = 'london'
# db.session.commit()
# joy_object = course.query.filter by(name='physics')(0)
# dd1 = Semester.query.get(2)
# dd1.course = joy_object.id
# db.session.commit()

# Delete operation
# com_to_del = College.query.get(5)
#db.session.delete(com to del)
# db.session.commit()

# Routes
@app.route('/',methods=['GET','POST'])
def home_fun():
    if request.method == 'POST' and request.form.get('action') == 'Create':
        id = int(request.form.get('id'))
        name = request.form.get('name')
        address = request.form.get('address')
        c_new = College(id=id,name=name,address=address)
        db.session.add(c_new)
        db.session.commit()
        return redirect(url_for_('home_fun'))

    if request.method == 'POST' and request.form.get('action') == 'Search':
        search_query = request.form.get('location')
        data_to_show = College.query.filter_by(address=search_query)

    else:
        data_to_show = Company.query.all()
    return render_template("home.html",List_of_data=data_to_show)

@app.route('/college/<int:id>')
def company_fun(id):
    company_object = College.query.get(id)
    return render_template("college.htmt",data=college_object)

@app.route('/contact_url')
def contact_fun():
    return render_template("contact.html")

@app.route('/education_url')
def education_fun():
    # processing
    return render_template("education.html")

@app.route('/study')
def study_fun():
    # processing (only backend)
    return redirect(url_for('education_fun'))
    
        


