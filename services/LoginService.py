import bcrypt
from flask import jsonify
from flask_login import login_user, logout_user

from models.user import User


class LoginService:


    def login(self, username, password):

        if username and password:
            user = User.query.filter_by(username=username).first()
            if user and bcrypt.checkpw(str.encode(password), str.encode(user.password)):
                login_user(user)
                return jsonify({'message':'Login Successful'}), 200
            else:
                return jsonify({'message':'Invalid Credentials'}), 401

        return jsonify({'message':'Username and Password required'}), 400

    def logout(self):
        logout_user()
        return jsonify({'message':'Logout Successful'}), 200