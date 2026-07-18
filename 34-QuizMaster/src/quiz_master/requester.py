import requests

def get_request(url):
    """
    Makes a GET request to the specified URL and returns the response.

    Args:
        url (str): The URL to send the GET request to.

    Returns:
        Response: The response object resulting from the GET request.
    """
    try:
        print(f"Making GET request to URL: {url}")
        response = requests.get(url, timeout=15)

        # Raise an exception for HTTP errors
        response.raise_for_status()
        return response.json()
    except requests.ConnectTimeout as timeout_err:
        print(f"The request timed out: {timeout_err}")
        return None
    except requests.ConnectionError as conn_err:
        print(f"Failed to connect to the server: {conn_err}")
        return None
    except requests.Timeout as timeout_err:
        print(f"The request timed out: {timeout_err}")
        return None
    except requests.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return None
    except requests.RequestException as req_err:
        print(f"An error occurred: {req_err}")
        return None
