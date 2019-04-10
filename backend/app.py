import pandas
import structlog
from flask import Flask, jsonify
from time import gmtime, strftime
from main import generate_element, amount_combos

logger = structlog.get_logger()


app = Flask(__name__)

logger.msg("Application ready to handle requests")


@app.route("/")
def generate():

    adjective, name = generate_element()
    logger.msg(f"Name is: {name}, adjective is: {adjective}")

    response = f"{adjective.capitalize()} {name.capitalize()}"
    return response

@app.route("/stat")
def stats():
    logger.info("Returning amount of combos")
    amount = amount_combos()

    response = jsonify({"combos": f"{amount}"})
    return response


@app.route("/json")
def generate_json():

    adjective, name = generate_element()

    logger.msg(f"Name is: {name}, adjective is: {adjective}")

    response = jsonify({"name":  f"{name.lower()}", "adjective": f"{adjective.lower()}", "timestamp": strftime("%Y-%m-%d %H:%M:%S", gmtime())})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
