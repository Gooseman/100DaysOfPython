from iss.location_requester import get_iss_location

def iss_location():
    latitude, longitude = get_iss_location()

    if float("nan") in (latitude, longitude):
        print("Failed to retrieve ISS location.")
        return

    print(f"Current ISS Location: Latitude: {latitude}, Longitude: {longitude}")

if __name__ == "__main__":
    iss_location()
