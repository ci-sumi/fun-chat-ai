from flask import Flask
import chat

app = Flask(__name__)
@app.route('/')
def hello_world():
    return '<h2>Hello, Tomi Tomi!</h2>'

if __name__ == '__main__':
    app.run(debug=True)
