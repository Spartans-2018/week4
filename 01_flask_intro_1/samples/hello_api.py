from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

hellos = {
    'english': 'Hello world.',
    'spanish': 'Hola mundo.',
    'french': 'Bonjour le monde.',
    'german': 'Hallo welt.',
    'italian': 'Ciao mondo.',
    'chinese': '你好世界',
}


@app.route('/')
def hello_world():
    # expecting the user give the query in the url, key is languange
    # url/?language=french >> this will print hello world in french
    language = request.args.get('language')

    # print lines or any code here will be active and executed ones user
    # does anything on the url (can refresh or pass arguments etc.)
    print(request)
    print(request.args)
    print(request.method)

    # if language is None hello world will be printed in chinese
    response = hellos.get(language) or hellos['chinese']

    # result will be returned in Json format with html header
    return jsonify(name=response)


if __name__ == "__main__":
    app.run(debug=True)
