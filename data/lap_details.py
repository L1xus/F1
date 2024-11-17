import json

with open("names_laps.json", "r") as file:
    data = json.load(file)


new_data = [
    {
        "date_start": item["date_start"],
        "driver_number": item["driver_number"],
        "full_name": item["full_name"],
        "team_name": item["team_name"],
        "is_pit_out_lap": item["is_pit_out_lap"],
        "lap_duration": item["lap_duration"],
        "lap_number": item["lap_number"]  ,
        "meeting_key": item["meeting_key"]
    }
    for item in data
]

with open("lap_details.json", "w") as file:
    json.dump(new_data, file, indent=4)
