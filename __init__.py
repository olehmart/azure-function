import logging

import azure.functions as func

from calculator import highest_price_function

import json


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    max_prices = highest_price_function()
    max_prices_json = json.dumps(max_prices)

    return func.HttpResponse(max_prices_json, mimetype='text/json')
