import json

with open("names_laps.json", "r") as file:
    data = json.load(file)


new_data = [
    {
        "driver_number": item["driver_number"],
        "full_name": item["full_name"],
        "team_name": item["team_name"],
        "i1_speed": item["i1_speed"],
        "i2_speed": item["i2_speed"],
        "avg_speed": (item["i1_speed"] + item["i2_speed"]) / 2 ,
        "st_speed": item["st_speed"]
    }
    for item in data
]

with open("st_speed.json", "w") as file:
    json.dump(new_data, file, indent=4)
