import azure.functions as func
import datetime
import json
import logging
# from openai import AzureOpenAI
# from azure.identity import DefaultAzureCredential
# from azure.keyvault.secrets import SecretClientpython 
app = func.FunctionApp()

@app.route(route="dockerized_openai", auth_level=func.AuthLevel.ANONYMOUS)
def dockerized_openai(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )