import azure.functions as func
import os
import datetime
import json
import logging
from smtp_email_sender import EmailSender, email_text
from config import EMAIL_SENDER, EMAIL_PASSWORD
from azure_blob_utils import emptyCosmosDB,generateEmailContent

import os

# from dotenv import load_dotenv

# Load environment variables from .env file
# load_dotenv()


app = func.FunctionApp()


@app.route(route="hellowworld", auth_level=func.AuthLevel.ANONYMOUS)
def hellowworld(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")
    try:
        result = emptyCosmosDB()
        logging.info(result)
        return func.HttpResponse(
            "This function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
            status_code=200,
        )
    except Exception as e:
        logging.error(e)
        return func.HttpResponse(
            "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
            status_code=500,
        )


@app.route(route="health", auth_level=func.AuthLevel.ANONYMOUS)
def healthFunc(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")
    try:
        # result = emptyCosmosDB()
        # logging.info(result)
        return func.HttpResponse(
            "This function executed successfully.",
            status_code=200,
        )
    except Exception as e:
        logging.error(e)
        return func.HttpResponse(
            "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
            status_code=500,
        )


@app.route(route="emailtrigger", auth_level=func.AuthLevel.ANONYMOUS)
def emailtrigger(req: func.HttpRequest) -> func.HttpResponse:
    print(EMAIL_SENDER, EMAIL_PASSWORD)
    logging.info(os.getenv("SENDER_EMAIL"))
    logging.info("Python HTTP trigger function processed a request.")
    todo_id = req.params.get("todo_id")
    email_str = generateEmailContent(todo_id) 
    logging.info(email_str)
    sender = EmailSender(
        sender=EMAIL_SENDER,
        password=EMAIL_PASSWORD,
        smtp_server="smtp.gmail.com",
        smtp_port=587,
        use_tls=True,
        debug=False,  # Set to False to actually send the email.
    )
    sender.create_message(
        receiver="ashece9@gmail.com", subject="Hello from SMTP-Email-Sender"
    ).attach(
        email_text(email_str, "html")
    ).sendmail()
    sender.finish()
    return func.HttpResponse(
            "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
            status_code=200,
        )
    
        


@app.timer_trigger(
    schedule="0 0 20 * * *",
    arg_name="myTimer",
    run_on_startup=False,
    use_monitor=True,
)
def deletion_trigger(myTimer: func.TimerRequest) -> None:
    # Note: Do NOT return HttpResponse in a timer trigger.
    if myTimer.past_due:
        logging.info("The timer is past due!")

    logging.info("Timer trigger fired ")

    try:
        # TODO: call your work here, e.g.:
        result = emptyCosmosDB()
        logging.info("Cleanup result: %s", result)
        pass
    except Exception as e:
        logging.exception("Timer job failed: %s", str(e))
