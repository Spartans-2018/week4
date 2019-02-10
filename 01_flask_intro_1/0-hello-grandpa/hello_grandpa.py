from flask import Flask

app = Flask(__name__)


@app.route('/hello-grandpa')
def hello():
    return "Greetings grandpa!"


@app.route('/goodbye-grandpa')
def goodbye():
    return "Bye bye"


@app.route('/i-love-you-grandpa')
def ily_grandpa():
    return "Many thanks. Here, have some butterscotch hard candies."


if __name__ == "__main__":
    app.run(debug=True)
