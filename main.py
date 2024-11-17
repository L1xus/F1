import requests
import json
from pathlib import Path

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36"
}

output_dir = Path("./data")
output_dir.mkdir(exist_ok=True)
def save_to_json(filename, data):
    with open(output_dir / filename, "w") as f:
        json.dump(data, f, indent=4)

def fetch_data(url):
    try:
        print(url)
        print(headers)
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print("Failed to fetch data:", e)
        return None


# Get races of the last season
def get_last_season_races():
    session_url = "https://api.openf1.org/v1/sessions?session_name=Race&date_start%3E%3D2024-02-29"
    sessions = fetch_data(session_url)
    return [session["session_key"] for session in sessions] if sessions else []

# Get and save drivers of the last race!
def get_drivers():
    drivers_url = "https://api.openf1.org/v1/drivers?session_key=latest"
    drivers = fetch_data(drivers_url)
    if drivers:
        save_to_json("drivers.json", drivers)
        return [driver["driver_number"] for driver in drivers]
    return []


def get_data():
    print("HELLO!")
    session_keys = get_last_season_races()
    print(session_keys)
    drivers_numbers = get_drivers()
    print(drivers_numbers)

    #all_cars = {}
    all_laps = {}
    all_pits = {}
    all_positions = {}
    all_stints = {}

    for session in session_keys:
        #all_cars[session] = {}
        all_laps[session] = {}
        all_pits[session] = {}
        all_positions[session] = {}
        all_stints[session] = {}

        for driver in drivers_numbers:
            print(driver)
            # # Fetch and store laps data
            laps_url = f"https://api.openf1.org/v1/laps?session_key={session}&driver_number={driver}"
            laps_data = fetch_data(laps_url)
            if laps_data:
                all_laps[session][driver] = laps_data

             # # Fetch and store pits data
            pit_url = f"https://api.openf1.org/v1/pit?session_key={session}&driver_number={driver}"
            pit_data = fetch_data(pit_url)
            if pit_data:
                all_pits[session][driver] = pit_data
             #
             # # Fetch and store positions data
            position_url = f"https://api.openf1.org/v1/positions?session_key={session}&driver_number={driver}"
            position_data = fetch_data(position_url)
            if position_data:
                all_positions[session][driver] = position_data
             #
             # # Fetch and store stints data
            stints_url = f"https://api.openf1.org/v1/stints?session_key={session}&driver_number={driver}"
            stints_data = fetch_data(stints_url)
            if stints_data:
                all_stints[session][driver] = stints_data
             
     # Save data to JSON files
    #save_to_json("cars.json", all_cars)
    save_to_json("laps.json", all_laps)
    save_to_json("pits.json", all_pits)
    save_to_json("positions.json", all_positions)
    save_to_json("stints.json", all_stints)

get_data()
