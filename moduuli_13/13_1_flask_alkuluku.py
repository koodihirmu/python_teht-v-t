from flask import Flask, Response, json

app = Flask(__name__)


@app.route("/isprime/<number>")
def isprime(number: int) -> Response:
    # trying to errorhandle
    try:
        isPrime = True
        number = int(number)
        for i in range(2, number):
            if number % i == 0:
                isPrime = False
                break
        # set status to 200 to indicate successful query
        status = 200
        # set answer if everything went alright
        answer = {
            "status": status,
            "number": number,
            "isprime": isPrime,
        }
    except ValueError:
        # assign return value if there was an error
        status = 400
        answer = {"status": status, "text": "Invalid Value For isPrime Function"}

    # convert the answer to json format
    jsonAnswer = json.dumps(answer)
    return Response(response=jsonAnswer, status=status, mimetype="application/json")


@app.errorhandler(404)
def errorhandler(_) -> Response:
    answer = {"status": 404, "text": "Invalid enpoint"}
    jsonAnswer = json.dumps(answer)
    return Response(response=jsonAnswer, status=404, mimetype="application/json")


if __name__ == "__main__":
    try:
        app.run(host="127.0.0.1", port=3000)
    except Exception as e:
        print(e)
