from flask import Flask, request, jsonify
from flask_login import LoginManager, login_user, current_user, login_required, logout_user

from config.database import db
from models.user import User
from services.LoginService import LoginService
from services.UserService import UserService

app = Flask(__name__)

app.config['SECRET_KEY'] = "your_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:admin123@127.0.0.1:3306/desafio_flask_dieta'

loginManager = LoginManager()
db.init_app(app)
loginManager.login_view = 'login'
loginManager.init_app(app)


userService = UserService()
loginService = LoginService()

#Rotas de Autenticação

@loginManager.user_loader
def load_user(user_id):
    try:
        return User.query.get(int(user_id))
    except Exception:
        return None

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    return loginService.login(username, password)

@app.route('/logout', methods=['GET'])
@login_required
def logout():
    return loginService.logout()

#Rotas de Usuário
@app.route('/user', methods=['POST'])
def create():
    data = request.get_json()
    return userService.create_user(data);

def findById(user_id):
    return userService.findById(user_id)

#Rotas de Refeição

if __name__ == '__main__':
    app.run(debug=True)