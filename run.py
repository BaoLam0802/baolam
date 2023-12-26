from flask import Flask, render_template, redirect, url_for, request
from config import Config
from app.models.User import User, db
from app.service.UserService import server_bp, jwt
from app.routes.Login import login_bp

app = Flask(__name__, template_folder='app/templates')
app.config.from_object(Config)

db.init_app(app)
app.register_blueprint(server_bp, url_prefix='/api')
app.register_blueprint(login_bp)
jwt.init_app(app)

@app.route('/')
def home():
    return render_template('Home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        new_user = User(UserName=username, Email=email, PassWord=password)
        new_user.save()

        return redirect(url_for('login'))

    return render_template('Register.html')

@app.route('/login')
def login():
    return render_template('Login.html')

@app.route('/student')
def student():
    return render_template('Student.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
