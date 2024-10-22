from crypt import methods

from flask import Flask, Response
import json

app = Flask(__name__)

@app.route("/prime/<num>", methods=["GET"])
def prime(num):
    try:
        response = {
            "number": num,
            "isPrime": is_prime(int(num))
        }
        return Response(response=json.dumps(response), status=200, mimetype="application/json")
    except ValueError:
        error = {
            "code" : "400",
            "text" : "Unexpected Input"
        }
        return Response(response=json.dumps(error), status=400, mimetype="application/json")

@app.errorhandler(404)
def page_not_found(errorcode):
    error = {
        "code" : "404",
        "text" : "Not Found"
    }
    return Response(response=json.dumps(error), status=404, mimetype="application/json")

def is_prime(num:int)->bool:
    is_prime_num = True
    for i in range(num // 2):
        i += 2
        print(i)
        if num % i == 0:
            return False
    if is_prime_num:
        return True

if __name__ == '__main__':
    app.run(use_reloader=True,
            host='127.0.0.1',
            port=3000,
            debug=True)