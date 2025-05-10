import ast
import json
import requests
import snowflake.connector
import os

SNOWFLAKE_CLIENT_ID = os.environ.get("SNOWFLAKE_CLIENT_ID")
SNOWFLAKE_CLIENT_SECRET = os.environ.get("SNOWFLAKE_CLIENT_SECRET")
snowflake.connector.paramstyle = 'qmark'


def generate_token(clients, client_secret):
    auth_response = requests.post(
        "https://oauth.cimpress.io/v2/token",
        data={
            "grant_type": "client_credentials",
            "client_id": clients,
            "client_secret": client_secret,
            "audience": "https://api.cimpress.io/",
        },
    )
    auth_response = json.loads(auth_response.content)
    access_token = "Bearer " + auth_response["access_token"]
    return access_token


def get_snowflake_connection():
    snowflake_api = (
        "https://access.pdw.cimpress.io/v0/accounts/cimpress/users/{client_id}%40clients/credentials".format(
            client_id=SNOWFLAKE_CLIENT_ID
        )
    )
    snowflake_header = {
        "Authorization": generate_token(SNOWFLAKE_CLIENT_ID, SNOWFLAKE_CLIENT_SECRET),
        "Content-Type": "application/json",
    }
    snowflake_response = requests.post(url=snowflake_api, headers=snowflake_header)
    credentials = ast.literal_eval(snowflake_response.content.decode("utf-8"))
    snow_flake_engine = snowflake.connector.connect(
        user=credentials["snowflake"]["username"],
        password=credentials["snowflake"]["password"],
        account=credentials["snowflake"]["account"],
        region=credentials["snowflake"]["region"],
        warehouse="LOOKER_MAT_WH_QUERY",
        database="MARKETING_AUTOMATION",
        schema="CUSTOMER_DATA_PLATFORM",
        role="MARKETING_TECHNOLOGY",
    )
    return snow_flake_engine
