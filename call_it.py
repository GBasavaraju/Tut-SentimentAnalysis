import requests

# Set the URL of your FastAPI endpoint
url = "http://127.0.0.1:8001/analyze"


messages = ["I got no use of this", "I had good nap, happy now"]


for message in messages:

    # Define the input data as a dictionary
    data = {"input_string": message}

    try:
        
        # Make a POST request to the endpoint
        response = requests.post(url, json=data)
        print(f"The sentiment is {response.json()["result"]["sentiment"]} with a score of {round(response.json()["result"]["score"], 3)}")

    except Exception as err:

        # Print an error message if the request was not successful
        print(f"Error: {response.status_code} - {err}")