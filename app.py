from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    usn = db.Column(db.String(20), nullable=False)
    branch = db.Column(db.String(20), nullable=False)
    semester = db.Column(db.String(20), nullable=False)
    section = db.Column(db.Integer())
    dob = db.Column(db.Date)
    address = db.Column(db.String(200), nullable=True)
    phone_number = db.Column(db.String(15), nullable=True)
    father_name = db.Column(db.String(50), nullable=True)
    father_phone = db.Column(db.String(15), nullable=True)
    mother_name = db.Column(db.String(50), nullable=True)
    mother_phone = db.Column(db.String(15), nullable=True)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    students = Students.query.all()
    return render_template('index.html', students=students)

@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        usn = request.form['usn']
        branch = request.form['branch']
        semester = request.form['semester']
        section = request.form['section']
        dob_str = request.form['dob']
        dob = datetime.strptime(dob_str, '%Y-%m-%d').date()
        address = request.form.get('address')
        phone_number = request.form.get('phone_number')
        father_name = request.form.get('father_name')
        father_phone = request.form.get('father_phone')
        mother_name = request.form.get('mother_name')
        mother_phone = request.form.get('mother_phone')
        new_student = Students(
            name=name, usn=usn, branch=branch, semester=semester,
            section=section, dob=dob, address=address, phone_number=phone_number,
            father_name=father_name, father_phone=father_phone,
            mother_name=mother_name, mother_phone=mother_phone
        )
        db.session.add(new_student)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_student.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    student = Students.query.get_or_404(id)
    if request.method == 'POST':
        student.name = request.form['name']
        student.usn = request.form['usn']
        student.branch = request.form['branch']
        student.semester = request.form['semester']
        student.section = request.form['section']
        dob_str = request.form['dob'].strip()
        student.dob = datetime.strptime(dob_str, '%Y-%m-%d').date()
        student.address = request.form.get('address')
        student.phone_number = request.form.get('phone_number')
        student.father_name = request.form.get('father_name')
        student.father_phone = request.form.get('father_phone')
        student.mother_name = request.form.get('mother_name')
        student.mother_phone = request.form.get('mother_phone')

        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit_student.html', student=student)

@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_student(id):
    student = Students.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return jsonify({'message': 'Student deleted successfully'})

if __name__ == "__main__":
    app.run(debug=True)
