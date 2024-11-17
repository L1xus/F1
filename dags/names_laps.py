import json

with open("drivers.json", "r") as f1, open("lapss.json", "r") as f2:
    pilotes = json.load(f1)
    tours = json.load(f2)

pilotes_dict = {p['driver_number']: p for p in pilotes}


for lap in tours:
    driver_number = lap.get('driver_number')
    if driver_number in pilotes_dict:
        pilote_info = pilotes_dict[driver_number]
        lap['team_name'] = pilote_info['team_name']
        lap['full_name'] = pilote_info['full_name']


with open("names_laps.json", "w") as f:
    json.dump(tours, f, indent=4)
