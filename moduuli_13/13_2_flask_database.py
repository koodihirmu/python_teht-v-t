from database.database import Database
from flask import Flask, Response, json

db = Database()
app = Flask(__name__)


@app.route("/kenttä/<icao>")
def getAirport(icao: str) -> Response:
    try:
        row = db.fetch_row("airport", "=", {"ident": icao})
        if row:
            status = 200
            answer = {
                "status": status,
                "ICAO": row["ident"],
                "Name": row["name"],
                "Municipality": row["municipality"],
            }
        else:
            raise Exception()
    except:
        status = 400
        answer = {"status": status, "text": "Invalid value for icao field"}

    json_answer = json.dumps(answer)
    return Response(response=json_answer, status=status, mimetype="application/json")


@app.errorhandler(404)
def errorhandling(_):
    status = 404
    answer = {"status": status, "text": "Invalid endpoint"}
    json_answer = json.dumps(answer)
    return Response(response=json_answer, status=status, mimetype="application/json")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=3069)
