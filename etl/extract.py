from etl.utils import fetch_data, save_to_json

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


# Get and store all data in json files
def extract_data():
    session_keys = get_last_season_races()
    drivers_numbers = get_drivers()
    
    all_cars = {}
    all_laps = {}
    all_pits = {}
    all_positions = {}
    all_stints = {}

    for session in session_keys:
        all_cars[session] = {}
        all_laps[session] = {}
        all_pits[session] = {}
        all_positions[session] = {}
        all_stints[session] = {}
        
        for driver in drivers_numbers:
            # Fetch and store cars data
            cars_url = f"https://api.openf1.org/v1/car_data?session_key={session}&driver_number={driver}"
            cars_data = fetch_data(cars_url)
            if cars_data:
                all_cars[session][driver] = cars_data

            # Fetch and store laps data
            laps_url = f"https://api.openf1.org/v1/laps?session_key={session}&driver_number={driver}"
            laps_data = fetch_data(laps_url)
            if laps_data:
                all_laps[session][driver] = laps_data
            
            # Fetch and store pits data
            pit_url = f"https://api.openf1.org/v1/pit?session_key={session}&driver_number={driver}"
            pit_data = fetch_data(pit_url)
            if pit_data:
                all_pits[session][driver] = pit_data
            
            # Fetch and store positions data
            position_url = f"https://api.openf1.org/v1/positions?session_key={session}&driver_number={driver}"
            position_data = fetch_data(position_url)
            if position_data:
                all_positions[session][driver] = position_data
            
            # Fetch and store stints data
            stints_url = f"https://api.openf1.org/v1/stints?session_key={session}&driver_number={driver}"
            stints_data = fetch_data(stints_url)
            if stints_data:
                all_stints[session][driver] = stints_data

    # Save data to JSON files
    save_to_json("cars.json", all_cars)
    save_to_json("laps.json", all_laps)
    save_to_json("pits.json", all_pits)
    save_to_json("positions.json", all_positions)
    save_to_json("stints.json", all_stints)
