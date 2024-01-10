from route import teste
from flask import Flask

app = Flask(__name__)
app.register_blueprint(teste)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)