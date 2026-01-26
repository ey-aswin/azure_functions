from azure.cosmos import CosmosClient
from config import (
    COSMOS_DB_CONNECTION_STRING,
    COSMOS_DB_CONTAINER_NAME,
    COSMOS_DB_DATABASE_NAME,
)
import logging
from email_utils import generate_todo_ack_email,generate_todo_not_found_email


def emptyCosmosDB():
    try:
        logging.info(
            "Cosmos DB config: conn='%s', db='%s', container='%s'",
            COSMOS_DB_CONNECTION_STRING,
            COSMOS_DB_DATABASE_NAME,
            COSMOS_DB_CONTAINER_NAME,
        )

        cosmos_client = CosmosClient.from_connection_string(COSMOS_DB_CONNECTION_STRING)
        database = cosmos_client.get_database_client(COSMOS_DB_DATABASE_NAME)
        container = database.get_container_client(COSMOS_DB_CONTAINER_NAME)

        logging.info("Connected to Cosmos successfully")

        items = container.query_items(
            query="SELECT c.id FROM c WHERE c.test = @pk",
            parameters=[{"name": "@pk", "value": "react-demo"}],
            enable_cross_partition_query=False,  # single-partition quer
        )

        items = list(items)  # IMPORTANT: Convert iterator to list
        logging.info("Fetched %d items", len(items))

        for item in items:
            logging.info(
                "Deleting item id=%s partition_key=%s", item["id"], item.get("test")
            )
            container.delete_item(item["id"], partition_key="react-demo")

        logging.info("Deleted all items successfully")
        return True

    except Exception as e:
        logging.error("An exception occurred: %s", e)
        return False


def generateEmailContent(item_id: str):
    logging.info(
        "Cosmos DB config: conn='%s', db='%s', container='%s'",
        COSMOS_DB_CONNECTION_STRING,
        COSMOS_DB_DATABASE_NAME,
        COSMOS_DB_CONTAINER_NAME,
    )

    cosmos_client = CosmosClient.from_connection_string(COSMOS_DB_CONNECTION_STRING)
    database = cosmos_client.get_database_client(COSMOS_DB_DATABASE_NAME)
    container = database.get_container_client(COSMOS_DB_CONTAINER_NAME)
    logging.info("Connected to Cosmos successfully")

    query = "SELECT * FROM c WHERE c.id = @id"
    params = [{"name": "@id", "value": item_id}]

    item = list(container.query_items(
            query=query, parameters=params, enable_cross_partition_query=True
        ))
     
    # logging.info(list(item))
    if len(item) != 0:
        
        HTML_STR = generate_todo_ack_email(title=item[0]["title"],description=item[0]["description"])
        return HTML_STR
    else:
        return generate_todo_not_found_email()
