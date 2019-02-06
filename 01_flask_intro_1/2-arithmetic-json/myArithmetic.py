from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/add')
def add_nums():
    num1 = request.args.get ('num1')
    num2 = request.args.get ('num2')
    exp = num1 + "+" + num2
    ans = int(num1) + int(num2)
    return jsonify(exp = exp, result = ans)

@app.route('/sub')
def sub_nums():
    num1 = request.args.get ('num1')
    num2 = request.args.get ('num2')
    exp = num1 + "-" + num2
    ans = int(num1) - int(num2)
    return jsonify(exp = exp, result = ans)

@app.route('/mul')
def mul_nums(num1, num2):
    num1 = request.args.get ('num1')
    num2 = request.args.get ('num2')
    exp = num1 + "*" + num2
    ans = int(num1) * int(num2)
    return jsonify(exp = exp, result = ans)

@app.route('/div')
def div_nums():
    num1 = request.args.get ('num1')
    num2 = request.args.get ('num2')
    exp = num1 + "/" + num2
    ans = int(num1) / int(num2)
    return jsonify(exp = exp, result = ans)

if __name__ == "__main__":
    app.run(debug=True)