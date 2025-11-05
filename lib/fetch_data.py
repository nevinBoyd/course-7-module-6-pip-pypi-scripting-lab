import requests

def fetch_data():
    # Send a GET request to the API
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    
    # Check response status code
    if response.status_code == 200:
        # Return response date as a dictionary
        return response.json()
    
    # If request fails, return an empty dictionary
    return {}
