from flask import Blueprint, jsonify, request
from app.models.Student import Student, db

student_bp = Blueprint('student', __name__)

@student_bp.route('/student', methods=['POST'])
def create_student():
    data = request.get_json()

    new_student = Student(fullName=data['fullName'], dob=data['dob'], gender=data['gender'],
                          email=data['email'], phoneNumber=data['phoneNumber'],
                          address=data['address'], classID=data['classID'])

    db.session.add(new_student)
    db.session.commit()  # Lưu thay đổi vào cơ sở dữ liệu

    return jsonify({'message': 'Student created successfully'}), 201

# Get all students
@student_bp.route('/student', methods=['GET'])
def get_all_students():
    students = Student.query.all()
    student_list = [{'StudentID': student.StudentID, 'FullName': student.FullName, 'DOB': student.DOB,
                     'Gender': student.Gender, 'Email': student.Email, 'PhoneNumber': student.PhoneNumber,
                     'Address': student.Address, 'ClassID': student.ClassID} for student in students]
    return jsonify({'students': student_list})

# Get a specific student by ID
@student_bp.route('/student/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = Student.query.get(student_id)

    if student:
        student_info = {'StudentID': student.StudentID, 'FullName': student.FullName, 'DOB': student.DOB,
                        'Gender': student.Gender, 'Email': student.Email, 'PhoneNumber': student.PhoneNumber,
                        'Address': student.Address, 'ClassID': student.ClassID}
        return jsonify({'student': student_info})

    return jsonify({'message': 'Student not found'}), 404

# Update a student by ID
@student_bp.route('/student/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    student = Student.query.get(student_id)

    if student:
        data = request.get_json()
        student.FullName = data.get('fullName', student.FullName)
        student.DOB = data.get('dob', student.DOB)
        student.Gender = data.get('gender', student.Gender)
        student.Email = data.get('email', student.Email)
        student.PhoneNumber = data.get('phoneNumber', student.PhoneNumber)
        student.Address = data.get('address', student.Address)
        student.ClassID = data.get('classID', student.ClassID)

        db.session.commit()

        return jsonify({'message': 'Student updated successfully'})

    return jsonify({'message': 'Student not found'}), 404

# Delete a student by ID
@student_bp.route('/student/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    student = Student.query.get(student_id)

    if student:
        db.session.delete(student)
        db.session.commit()
        return jsonify({'message': 'Student deleted successfully'})

    return jsonify({'message': 'Student not found'}), 404
