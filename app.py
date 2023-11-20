
from flask import Flask, jsonify

app = Flask(__name__)
CORS(app)
backend_link = ''

@app.route('/backend-link', methods=['GET'])
def get_backend_link():
    response = {
        'backend_link': backend_link
    }
    return jsonify(response)

@app.route('/set-backend-link',methods=['POST'])
def set_backend_link():
    backend_link = request.get_json().get('backend_link')
    return jsonify({'status':'success'})

if __name__ == '__main__':
    app.run(debug=True) 
