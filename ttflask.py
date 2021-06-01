from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/abc/<int:tmp>', methods=['get', 'post'])
def hello(tmp):
    print(request.data)
    print(request.json)
    print(tmp)
    return 'hello'


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")