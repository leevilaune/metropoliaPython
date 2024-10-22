from flask import Flask, Response
import json
import mysql.connector

app = Flask(__name__)

@app.route("/airport/<icao>")
def get_airport(icao):
	airport = get_airports(icao)
	if airport is None:
		return Response(response=json.dumps({"code": 404, "text": f"Airport {icao} not found"}), status=404,
		                mimetype="application/json")
	response = {
		"ICAO": icao,
		"Name": airport["name"],
		"Municipality": airport["municipality"]
	}
	return Response(response=json.dumps(response), status=200, mimetype="application/json")

@app.errorhandler(404)
def page_not_found(errorcode):
	error = {
        "code" : "404",
        "text" : "Not Found"
    }
	return Response(response=json.dumps(error), status=404, mimetype="application/json")

def get_airports(icao: str)->dict:
	connection = mysql.connector.connect(host="127.0.0.1",
	                                     port=3306,
	                                     database="flightgame",
	                                     username="root",
	                                     password="secretpassword",
	                                     autocommit=True)
	cursor = connection.cursor(dictionary=True)
	fetch_airport_sql = f"""
		SELECT name, municipality
		FROM airport
		WHERE airport.ident='{icao}'
	"""
	cursor.execute(fetch_airport_sql)
	return cursor.fetchone()

if __name__ == '__main__':
	app.run(use_reloader=True,
            host='127.0.0.1',
            port=3000,
            debug=True)