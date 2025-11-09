import bcrypt

from config.database import db
from models.user import User


class UserService:


    def create_user(self, user_data):
        username = user_data.get('username')
        password = user_data.get('password')
        role = user_data.get('role')
        if role == '':
            role= 'user'
        if username and password:
            if User.query.filter_by(username=username).first():
                return {'message': 'Nome de usuário já existe!'}, 409
            hashdpassword = bcrypt.hashpw(str.encode(password), bcrypt.gensalt());
            new_user = User(username=username, password=hashdpassword, role=role)
            db.session.add(new_user)
            db.session.commit()
            return {'message': 'Usuário criado com sucesso!'}, 201

        return {'message': 'Nome de usuário e senha são obrigatórios!'}, 400

    def findById(self, user_id):
        user = User.query.get(user_id)
        if user:
            return {'id': user.id, 'username': user.username, 'role': user.role}, 200
        return {'message': 'Usuário não encontrado!'}, 404

    def update(self, user_id, data):
        user = User.query.get(user_id)
        if user:
            username = data.get('username')
            password = data.get('password')

            if username:
                user.username = username
            if password:
                hashdpassword = bcrypt.hashpw(str.encode(password), bcrypt.gensalt());
                user.password = hashdpassword
            db.session.commit()
            return {'message': 'Usuário atualizado com sucesso!'}, 200
        return {'message': 'Usuário não encontrado!'}, 404

    def findAll(self):
        users = User.query.all()
        user_list = [{'id': user.id, 'username': user.username, 'role': user.role} for user in users]
        return {'users': user_list}, 200

    def delete(self, user_id):
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return {'message': 'Usuário deletado com sucesso!'}, 200
        return {'message': 'Usuário não encontrado!'}, 404