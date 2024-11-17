import json

with open("drivers.json", "r") as file:
    data = json.load(file)


new_data = [
    {"driver_number": item["driver_number"], "team_name": item["team_name"]}
    for item in data 
]

with open("fdrivers.json", "w") as file:
    json.dump(new_data, file, indent=4)
