from datetime import datetime, timezone
import sched
import sys

from iss.iss_location_requester import get_iss_location
from iss.sunrise_requester import get_sunrise_sunset

LONDON_LATITUDE = 51.507351
LONDON_LONGITUDE = -0.127758

def iss_location():
    latitude, longitude = get_iss_location()

    if float("nan") in (latitude, longitude):
        print("Failed to retrieve ISS location.")
        return

    print(f"Current ISS Location: Latitude: {latitude}, Longitude: {longitude}")

def get_sunrise_sunset_time(latitude, longitude):
    if float("nan") in (latitude, longitude):
        print("Failed to retrieve ISS location for sunrise calculation.")
        return

    sunrise_at, sunset_at = get_sunrise_sunset(latitude, longitude)

    print(f"Sunrise time at location (Latitude: {latitude}, Longitude: {longitude}): {sunrise_at}")
    print(f"Sunset time at location (Latitude: {latitude}, Longitude: {longitude}): {sunset_at}")
    return sunrise_at, sunset_at

def is_sun_down(sunrise_time, sunset_time, current_time):
    if sunrise_time is None or sunset_time is None:
        print("Sunrise or sunset time is None, cannot determine if the sun is down.")
        return False

    try:
        sunrise = datetime.fromisoformat(sunrise_time)
        sunset = datetime.fromisoformat(sunset_time)
        current = datetime.fromisoformat(current_time)

        return sunset < current < sunrise
    except ValueError as e:
        print(f"Error parsing datetime: {e}")
        return False

def is_iss_overhead(iss_latitude, iss_longitude, target_latitude, target_longitude, threshold=5.0):
    if float("nan") in (iss_latitude, iss_longitude):
        print("Failed to retrieve ISS location for overhead calculation.")
        return False

    lat_diff = abs(iss_latitude - target_latitude)
    lon_diff = abs(iss_longitude - target_longitude)

    return lat_diff <= threshold and lon_diff <= threshold

def is_iss_visible():
    iss_latitude, iss_longitude = get_iss_location()
    sunrise_at, sunset_at = get_sunrise_sunset_time(LONDON_LATITUDE, LONDON_LONGITUDE)
    current_time = datetime.now(timezone.utc).isoformat()

    sun_is_down = is_sun_down(sunrise_at, sunset_at, current_time)
    iss_overhead = is_iss_overhead(iss_latitude, iss_longitude, LONDON_LATITUDE, LONDON_LONGITUDE)

    print(f"Current UTC time: {current_time}")
    print(f"Is the sun down at the current location? {'Yes' if sun_is_down else 'No'}")

    iss_overhead = is_iss_overhead(iss_latitude, iss_longitude, LONDON_LATITUDE, LONDON_LONGITUDE)
    is_visible = sun_is_down and iss_overhead

    print(f"Is the ISS overhead at the current location? {'Yes' if iss_overhead else 'No'}")

    return is_visible

def periodic_check_for_visible_iss():
    def execute_check():
        scheduler.enter(60, 1, execute_check)

        now = datetime.now().isoformat()
        print(f"Checking ISS visibility at {now}...")

        is_visible = is_iss_visible()

        if is_visible:
            print("The ISS is currently visible in the sky!")
        else:
            print("The ISS is not visible at the moment.")

    scheduler = sched.scheduler()

    scheduler.enter(0, 1, execute_check)
    scheduler.run()
    return scheduler

if __name__ == "__main__":
    try:
        periodic_check_for_visible_iss()
    except KeyboardInterrupt:
        print("Program terminated by user.")
        # scheduler.stop()
        sys.exit(0)
