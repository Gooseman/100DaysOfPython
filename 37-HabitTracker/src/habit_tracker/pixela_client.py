import os

from habit_tracker.requester import get_request, post_request

PIXELA_BASE_URL = "https://pixe.la"
PIXELA_USERS_URL = f"{PIXELA_BASE_URL}/v1/users"
PIXELA_TOKEN = os.environ.get("PIXELA_TOKEN")

def get_user(username: str) -> dict:
    def handle_user_profile(profile):
        if profile:
            return {"isSuccess": True, "data": profile}

        return {"isSuccess": False, "data": {}}

    user_profile = get_request(f"{PIXELA_BASE_URL}/@{username}", handle_response = handle_user_profile)

    print(user_profile)

    if user_profile:
        return {"isSuccess": True, "data": user_profile}

    return {"isSuccess": False, "data": {}}

def create_user(username: str) -> bool:
    def on_error(status: int, message: str):
        print(f"Error occurred: {message}")

        if 409 == status:
            print("User already exists.")
            return {"isSuccess": True, "status": 200, "message": "User already exists."}

        return {"isSuccess": False, "status": status, "message": message}

    data = {
        "token": PIXELA_TOKEN,
        "username": username,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }

    return post_request(PIXELA_USERS_URL, data, on_error = on_error)
