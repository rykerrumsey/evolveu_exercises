import sqlite3

from flask_restful import Resource, reqparse
from flask_jwt import jwt_required


class Client(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'email',
        type=str,
        required=True,
        help="This argument is required."
    )

    parser.add_argument(
        'phone',
        type=str,
        required=True,
        help="This argument is required."
    )

    parser.add_argument(
        'payment_type',
        type=str,
        required=True,
        help="This argument is required."
    )

    parser.add_argument(
        'payment_status',
        type=str,
        help="This is an optional argument"
    )

    parser.add_argument(
        'issues',
        type=str,
        help="This is an optional argument"
    )

    parser.add_argument(
        'notes',
        type=str,
        help="This is an optional argument."
    )

    # @jwt_required()
    def get(self, name):
        try:
            client = Client.find_by_name(name)
        except:
            return {'message': 'Client not found.'}, 404
        return client

    def post(self, name):
        if Client.find_by_name(name):
            return {'message': 'An item with id \'{}\' already exists.'.format(name)}, 400

        data = Client.parser.parse_args()

        client = {
            'name': name,
            'email': data['email'],
            'phone': data['phone'],
            'payment_type': data['payment_type'],
            'payment_status': data['payment_status'],
            'issues': data['issues'],
            'notes': data['notes']
        }

        try:
            Client.insert(client)
        except:
            return {"message": "An error occurred inserting the item."}, 500

        return client, 201

    def delete(self, name):
        if not Client.find_by_name(name):
            return {'message': 'Client {} was not found.'.format(name)}, 404

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "DELETE FROM clients WHERE name=?"
        cursor.execute(query, (name,))

        connection.commit()
        connection.close()

        return {'message': 'Client {} was deleted.'.format(name)}, 200

    def put(self, name):
        data = Client.parser.parse_args()

        client = Client.find_by_name(name)

        updated_client = {
            'name': name,
            'email': data['email'],
            'phone': data['phone'],
            'payment_type': data['payment_type'],
            'payment_status': data['payment_status'],
            'issues': data['issues'],
            'notes': data['notes']
        }

        if client is None:
            try:
                print(updated_client)
                Client.insert(updated_client)
            except:
                return {"message": "An error occurred inserting the item."}, 500
        else:
            try:
                print(updated_client)
                Client.update(updated_client)
            except:
                return {"message": "An error occurred updating the item."}, 500

        return updated_client

    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = 'SELECT * FROM clients WHERE name=?'

        result = cursor.execute(query, (name,))
        row = result.fetchone()

        connection.close()

        if row:
            return {'client': {'id': row[0], 'name': row[1], 'email': row[2]}}, 200

    @classmethod
    def insert(cls, client):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO clients VALUES(NULL, ?, ?, ?, ?, ?, ?, ?)"

        cursor.execute(query, (client['name'], client['email'], client['phone'], client['payment_type'], client['payment_status'], client['issues'], client['notes']))

        connection.commit()
        connection.close()

    @classmethod
    def update(cls, client):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "UPDATE clients SET email=? AND phone=? AND payment_type=? AND payment_status=? AND issues=? AND notes=? WHERE name=?"

        cursor.execute(query, (
        client['email'], client['phone'], client['payment_type'], client['payment_status'],
        client['issues'], client['notes'], client['name']))

        connection.commit()
        connection.close()


class ClientList(Resource):
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = 'SELECT * FROM clients'

        result = cursor.execute(query)

        clients = []
        for row in result:
            clients.append({'id': row[0], 'name': row[1], 'email': row[2], 'phone': row[3] })

        connection.close()

        return {'clients': clients}
