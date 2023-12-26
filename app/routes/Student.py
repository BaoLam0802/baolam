from flask import Blueprint, render_template, request, redirect, url_for
from app.models.Student import Student  # Import Student model từ file models.py

student_bp = Blueprint('student_bp', __name__)

@student_bp.route('/student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        fullName = request.form['fullName']
        dob = request.form['dob']
        gender = request.form['gender']
        email = request.form['email']
        phoneNumber = request.form['phoneNumber']
        address = request.form['address']
        classID = request.form['classID']

        # Tạo một đối tượng Student từ dữ liệu nhập vào
        new_student = Student(fullName=fullName, dob=dob, gender=gender,
                              email=email, phoneNumber=phoneNumber,
                              address=address, classID=classID)

        # Lưu đối tượng Student vào cơ sở dữ liệu
        new_student.save()  # Gọi method save() trên đối tượng Student để lưu vào DB

        # Sau khi thêm sinh viên thành công, có thể chuyển hướng người dùng đến trang chủ hoặc trang quản lý sinh viên
        return redirect(url_for('/'))  # Chuyển hướng đến route home hoặc route quản lý sinh viên

    # Nếu là method GET, render template cho trang thêm sinh viên
    return render_template('Student.html')
