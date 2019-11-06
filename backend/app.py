import pandas
from flask import Flask, jsonify
from time import gmtime, strftime
from main import generate_element, amount_combos

import logging
import sys
FORMAT = "%(asctime)-15s - %(levelname)s:%(name)s:%(message)s"

logging.basicConfig(
    format=FORMAT,
    stream=sys.stdout,
    level=logging.INFO,
)


logging.getLogger("werkzeug").setLevel(logging.WARNING)
logging.getLogger("root").setLevel(logging.WARNING)





app = Flask(__name__)

# Disable default logger
from flask.logging import default_handler

app.logger.removeHandler(default_handler)

logger = logging.getLogger("restApi")


logger.info("Application ready to handle requests")


@app.route("/raw")
def generate():

    adjective, name = generate_element()
    logger.info(f"Name is: {name}, adjective is: {adjective}")

    response = f"{adjective.capitalize()} {name.capitalize()}"
    return response

@app.route("/stat")
def stats():
    logger.info("Returning amount of combos")
    amount = amount_combos()

    response = jsonify({"combos": f"{amount}"})
    return response


@app.route("/")
def generate_json():

    adjective, name = generate_element()

    logger.info(f"Name is: {name}, adjective is: {adjective}")
    timestamp = strftime("%Y-%m-%d %H:%M:%S", gmtime())

    json_string = {"name":  f"{cleanUp(name.lower())}", "adjective": f"{cleanUp(adjective.lower())}", "timestamp": timestamp}
    response = jsonify(json_string)
    
    logger.info(f"Returning {json_string}")

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route("/healthz")
def health_check():

    adjective, name = generate_element()

    logger.debug(f"Name is: {name}, adjective is: {adjective}")
    timestamp = strftime("%Y-%m-%d %H:%M:%S", gmtime())

    json_string = {"name":  f"{cleanUp(name.lower())}", "adjective": f"{cleanUp(adjective.lower())}", "timestamp": timestamp}
    response = jsonify(json_string)
    
    logger.debug(f"Returning {json_string}")

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

def cleanUp(text):
    if text and len(text) > 0:
        return text.replace("-", " ")
    else:
        return text