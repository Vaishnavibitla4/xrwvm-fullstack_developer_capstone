import requests
import os
from dotenv import load_dotenv
from urllib.parse import quote

load_dotenv()

backend_url = os.getenv(
    "backend_url", default="http://localhost:3030"
)
sentiment_analyzer_url = os.getenv(
    "sentiment_analyzer_url",
    default=(
        "https://sentianalyzer.26xwg9zg3t0u.us-south."
        "codeengine.appdomain.cloud"
    ),
)


def get_request(endpoint, **kwargs):
    """
    Perform a GET request to the backend API with optional parameters.
    """
    params = ""
    if kwargs:
        for key, value in kwargs.items():
            params += key + "=" + value + "&"

    request_url = backend_url + endpoint
    if params:
        request_url += "?" + params

    print(f"GET from {request_url}")
    try:
        response = requests.get(request_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Network exception occurred: {err}")
        return None


def analyze_review_sentiments(text):
    """
    Analyze the sentiment of a given review text using the sentiment analyzer.
    Returns JSON with sentiment info or None if failed.
    """
    encoded_text = quote(text)
    request_url = f"{sentiment_analyzer_url}/analyze/{encoded_text}"
    try:
        response = requests.get(request_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")
        return None


def post_review(data_dict):
    """
    Post a review dictionary to the backend.
    """
    request_url = backend_url + "/insert_review"
    try:
        response = requests.post(request_url, json=data_dict)
        response.raise_for_status()
        print(response.json())
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Network exception occurred: {err}")
        return None
