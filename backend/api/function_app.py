import logging
import azure.functions as func
from azure.cosmos import CosmosClient
import os
import json

COSMOS_DB_ENDPOINT = os.getenv('COSMOS_DB_ENDPOINT')
COSMOS_DB_KEY = os.getenv('COSMOS_DB_KEY')
DATABASE_NAME = os.getenv('DATABASE_NAME')
CONTAINER_NAME = os.getenv('CONTAINER_NAME')


app = func.FunctionApp()

@app.route(route="getcount")
def getCount(req: func.HttpRequest) -> func.HttpResponse:
    try:
        logging.info("Initializing CosmosClient...")
        client = CosmosClient(COSMOS_DB_ENDPOINT, COSMOS_DB_KEY)
        database = client.get_database_client(DATABASE_NAME)
        container = database.get_container_client(CONTAINER_NAME)

        logging.info("CosmosClient initialized successfully.")

        item_id = '1'
        partition_key = '1'
        
        logging.info(f"Fetching document with item_id: {item_id} and partition_key: {partition_key}")
        
        item = container.read_item(item_id, partition_key=partition_key)
        current_counter = item.get('count', 0)
        new_counter = current_counter + 1
        item['count'] = new_counter

        logging.info(f"Counter updated successfully. New value: {new_counter}")

        container.upsert_item(item)

        return func.HttpResponse(json.dumps({"count": new_counter}), status_code=200, mimetype="application/json")

    except Exception as e:
        logging.error(f"Error fetching or updating the counter: {str(e)}")
        return func.HttpResponse(f"Error fetching or updating the counter: {str(e)}", status_code=500)