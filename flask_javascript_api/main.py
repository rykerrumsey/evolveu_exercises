import json
from flask import Flask, render_template, request
from my_sql import runSQL

# setup flask project
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/clients/<id>')
def specific_client(id):
    client = runSQL(f'select * from clients \
                    where client_id = ' + id)
    return json.dumps(client[0]), 200

@app.route('/clients')
def client():
    month = request.args.get('month')
    client_credits = request.args.get('credits')
    credits_by_client = request.args.get('client')

    if credits_by_client:
        clients = runSQL(f'select * from clients c \
                         full join credits e on c.client_id = e.client_id \
                         where name is NULL and credits >= 0')
        return render_template('template.html', clients=clients)

    if month and client_credits is None:
        clients = runSQL(f'select * from clients c \
                         full join credits e on c.client_id = e.client_id \
                         where month = \'{month}\' and name != \'\'')
        return render_template('template.html', clients=clients)

    if month is None and client_credits is not None:
        end_statement = '=' + str(client_credits)
        if client_credits == '0':
            end_statement = ' is NULL'

        clients = runSQL(f'select * from clients c \
                         full join credits e on c.client_id = e.client_id \
                         where credits{end_statement}')

        return render_template('template.html', clients=clients)

    if month is None and client_credits is None:
        clients = runSQL('select * from clients')
        return render_template('template.html', clients=clients)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
