from flask import Flask, request, jsonify

app = Flask(__name__)


# This is an example of a variable rule.
@app.route("/<word>")
def deaf_grandpa(word):
    for letter in word:
        if letter.isupper():
            response = "You are too young to know that my son :)"
        else:
            response = "What? I can't hear you!"

    print(request)
    print(request.args)
    print(request.method)
    return jsonify(name=response)


if __name__ == "__main__":
    app.run(debug=True)
