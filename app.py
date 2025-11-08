from flask import Flask, request
from flask_login import LoginManager

from config.database import db
from services.LoginService import LoginService
from services.UserService import UserService

app = Flask(__name__)

app.config['SECRET_KEY'] = "your_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:admin123@127.0.0.1:3306/desafio_flask_dieta'

loginManager = LoginManager()
db.init_app(app)
loginManager.init_app(app)
loginManager.login_view = 'login'

userService = UserService()
loginService = LoginService()

#Rotas de Autenticação
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    return loginService.login(username, password)

@app.route('/logout', methods=['GET'])
def logout():
    return loginService.logout()

#Rotas de Usuário
@app.route('/user', methods=['POST'])
def create():
    data = request.get_json()
    return userService.create_user(data);


if __name__ == '__main__':
    app.run(debug=True)