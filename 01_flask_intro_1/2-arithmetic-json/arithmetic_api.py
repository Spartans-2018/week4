from flask import Flask, jsonify, request

app = Flask(__name__)

# example use of request object
# test this route with localhost:5000/favorites?name=andrew&food=cereal


@app.route('/favorites')
def favorite_things():
    name = request.args.get('name') or 'sally'
    food = request.args.get('food') or 'cookies'
    show = request.args.get('show') or 'scrubs'
    return jsonify(
        name=name,
        food=food,
        show=show,
    )


@app.route('/add')
def adder():
    num1 = request.args.get('num1') or '0'
    num2 = request.args.get('num2') or '0'
    expression = f"{num1} + {num2}"
    result = int(num1) + int(num2)

    return jsonify(
        expression=expression,
        result=result,
    )


@app.route('/substract')
def substract():
    num1 = request.args.get('num1') or '0'
    num2 = request.args.get('num2') or '0'

    expression = f"{num1} - {num2}"
    result = int(num1) - int(num2)

    return jsonify(
        expression=expression,
        result=result,
    )


@app.route('/multiply')
def multiply():
    num1 = request.args.get('num1') or '0'
    num2 = request.args.get('num2') or '0'

    expression = f"{num1} * {num2}"
    result = int(num1) * int(num2)

    return jsonify(
        expression=expression,
        result=result,
    )


@app.route('/divide')
def divide():
    num1 = request.args.get('num1') or '0'
    num2 = request.args.get('num2') or '1'

    expression = f"{num1} / {num2}"
    result = int(num1) / int(num2)

    return jsonify(
        expression=expression,
        result=result,
    )


if __name__ == "__main__":
    app.run(debug=True)
