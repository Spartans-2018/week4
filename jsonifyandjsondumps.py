from flask import Flask
from flask import jsonify
import json
app = Flask(__name__)

class Myclass:
    def __init__(self):
        self.var1 = 1
        self.var2 = 2
        self.var3 = None
        self.mylist = [1,2,3,4,5,"Hello"]

    @app.route ('/add')
    def add(self):
        self.var3 = self.var1 + self.var2
        return jsonify(self.var3)

@app.route('/')
def myfunct():
    obj = Myclass ()
    # return json.dumps(obj,default=lambda o: o.__dict__)
    return json.dumps (obj.__dict__)

if __name__ == "__main__":
    objglobal = Myclass()
    app.run(debug=True)