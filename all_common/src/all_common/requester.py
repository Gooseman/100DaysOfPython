import requests

def default_handle_response(response):
    # What if the response is not JSON? This will raise an exception.
    return response.json()

def default_on_error(status, message):
    print(f"Error occurred with status {status}: {message}")
    return {}

def get_request(
        url,
        params: dict = None,
        handle_response = default_handle_response,
        on_error = default_on_error) -> dict:
    """
    Makes a GET request to the specified URL and returns the response.

    Args:
        url (str): The URL to send the GET request to.

    Returns:
        dict: The JSON response as a dictionary if the request is successful, otherwise an empty dictionary.
    """
    def make_get():
        print(f"Making GET request to URL: {url}")
        return requests.get(url, params=params, timeout=15)

    return try_send_request(make_get, handle_response, on_error)

def try_send_request(
        request_func,
        handle_response = default_handle_response,
        on_error = default_on_error) -> dict:
    """
    Tries to send a request using the specified request function and returns the response.

    Args:
        request_func (callable): The request function to call (e.g., get_request or post_request).
    Returns:
        dict: The JSON response as a dictionary if the request is successful, otherwise an empty dictionary.
    """
    try:
        response = request_func()

        print(f"Response status code: {response.status_code}")
        # Raise an exception for HTTP errors
        response.raise_for_status()
        return handle_response(response)
    except requests.ConnectTimeout as timeout_err:
        print(f"The request timed out: {timeout_err}")
        return on_error(-1, f"The request timed out: {timeout_err}")
    except requests.ConnectionError as conn_err:
        print(f"Failed to connect to the server: {conn_err}")
        return on_error(-1, f"Failed to connect to the server: {conn_err}")
    except requests.Timeout as timeout_err:
        print(f"The request timed out: {timeout_err}")
        return on_error(-1, f"The request timed out: {timeout_err}")
    except requests.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return on_error(response.status_code, http_err.response.text if http_err.response else str(http_err))
    except requests.RequestException as req_err:
        print(f"An error occurred: {req_err}")
        return on_error(-1, f"An error occurred: {req_err}")

def post_request(url, data: dict, handle_response = default_handle_response, on_error = default_on_error) -> dict:
    """
    Makes a POST request to the specified URL and returns the response.

    Args:
        url (str): The URL to send the POST request to.
        data (dict): The data to include in the POST request body. Defaults to None.

    Returns:
        dict: The JSON response as a dictionary if the request is successful, otherwise an empty dictionary.
    """
    def make_post():
        print(f"Making POST request to URL: {url}")
        return requests.post(url, json=data, timeout=15)

    return try_send_request(make_post, handle_response, on_error)
