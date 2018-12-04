from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from user import UserRegister
from client import Client, ClientList

app = Flask(__name__)
app.secret_key = 'ryker'
api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(ClientList, '/clients')
api.add_resource(Client, '/client/<string:name>')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
