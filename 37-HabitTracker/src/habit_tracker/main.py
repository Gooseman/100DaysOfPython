from habit_tracker.pixela_client import create_user, get_user

def get_user_data(username: str) -> dict:
    the_user_data = get_user(username)

    if the_user_data.get("isSuccess"):
        return the_user_data.get("data")

    user_created = create_user_data(username)

    if user_created.get("isSuccess"):
        return get_user(username)

    return {"message": user_created.get("message")}


def create_user_data(username: str) -> dict:
    return create_user(username)

if __name__ == "__main__":

    user_data = get_user_data("qswitch")

    if not user_data.get("isSuccess"):
        print(f"Failed to create user: {user_data.get('message')}")
