import random as _random
import flask

app = flask.Flask(__name__)

@app.route('/alive/', methods=['GET'])
def alive():
    return "I'm alive"

@app.route('/', methods=['GET'])
def random():
    return 'a pseudo randomly generated number: %s' % _random.random()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
