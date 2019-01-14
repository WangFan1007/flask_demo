from flask import Flask

app = Flask(__name__)

@app.route('/index')
def index():
    return "Nice to meet you"


if __name__ == '__main__':
    app.run()