from flask import Blueprint, render_template, request, redirect, url_for
from app.models.User import User  # Import User model từ file models.py

login_bp = Blueprint('login_bp', __name__)

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Kiểm tra xem tên đăng nhập và mật khẩu có khớp với cơ sở dữ liệu không
        user = User.query.filter_by(UserName=username, PassWord=password).first()

        if user:
            # Đăng nhập thành công, có thể thực hiện các hành động khác ở đây
            return redirect(url_for('student'))  # Chuyển hướng đến trang chủ hoặc trang khác
        else:
            # Đăng nhập thất bại, có thể hiển thị thông báo lỗi hoặc redirect đến trang đăng nhập lại
            return render_template('Login.html', error='Tên đăng nhập hoặc mật khẩu không đúng')

    # Nếu là method GET, render template cho trang đăng nhập
    return render_template('Login.html')
