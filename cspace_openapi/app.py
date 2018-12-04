from flask import (
    Flask,
    jsonify,
    request,
    render_template
)

import connexion

app = connexion.App(__name__, specification_dir='./openapi', template_folder='templates')

app.add_api('openapi.yaml')


@app.route('/')
def home():
    return render_template('home.html')

# @app.route('/store', methods=['POST'])
# def create_store():
#     pass
#
# @app.route('/store/<string:name>')
# def get_store(name):
#     pass
#
# @app.route('/stores')
# def get_stores():
#     return jsonify({'stores': stores})
#
# @app.route('/store/<string:name>/item', methods=['POST'])
# def create_item_in_store(name):
#     pass
#
# @app.route('/store/<string:name>/item')
# def get_item_in_store(name):
#     pass

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
