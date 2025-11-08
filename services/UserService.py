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

    def get_user(self, user_id):
        # Logic to retrieve a user by ID
        return self.user_repository.find_user_by_id(user_id)

    def update_user(self, user_id, user_data):
        # Logic to update an existing user
        return self.user_repository.update_user(user_id, user_data)

    def delete_user(self, user_id):
        # Logic to delete a user by ID
        return self.user_repository.remove_user(user_id)