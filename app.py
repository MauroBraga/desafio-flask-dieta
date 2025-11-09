from flask import Flask, request, jsonify
from flask_login import LoginManager, login_user, current_user, login_required, logout_user

from config.database import db
from models.user import User
from services.LoginService import LoginService
from services.RefeicaoService import RefeicaoService
from services.UserService import UserService

app = Flask(__name__)

app.config['SECRET_KEY'] = "your_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:admin123@127.0.0.1:3306/desafio_flask_dieta'

loginManager = LoginManager()
db.init_app(app)
loginManager.login_view = 'login'
loginManager.init_app(app)


userService = UserService()
refeicaoService = RefeicaoService()
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

@app.route('/user/<int:user_id>', methods=['GET'])
@login_required
def findById(user_id):
    return userService.findById(user_id)

@app.route('/user', methods=['GET'])
@login_required
def findAll():
    return userService.findAll()

@app.route('/user/<int:user_id>', methods=['PUT'])
@login_required
def update(user_id):
    data = request.get_json()
    return userService.update(user_id, data)

@app.route('/user/<int:user_id>', methods=['DELETE'])
@login_required
def delete(user_id):
    return userService.delete(user_id)

#Rotas de Refeição
@app.route('/refeicao', methods=['POST'])
@login_required
def createRefeicao():
    data = request.get_json()
    return refeicaoService.create(data);

@app.route('/refeicao', methods=['GET'])
@login_required
def findAllRefeicao():
    return refeicaoService.findAll()

@app.route('/refeicao/<int:id_refeicao>', methods=['PUT'])
@login_required
def updateRefeicao(id_refeicao):
    data = request.get_json()
    return refeicaoService.update(id_refeicao, data)

@app.route('/refeicao/<int:id_refeicao>', methods=['DELETE'])
@login_required
def deleteRefeicao(id_refeicao):
    return refeicaoService.delete(id_refeicao)

if __name__ == '__main__':
    app.run(debug=True)