import json


with open('position.json', 'r') as pos_file:
    position_data = json.load(pos_file)


with open('fdrivers.json', 'r') as drivers_file:
    drivers_data = json.load(drivers_file)


team_mapping = {driver['driver_number']: driver['team_name'] for driver in drivers_data}


for event in position_data:
    driver_number = event['driver_number']
    event['team_name'] = team_mapping.get(driver_number, 'Unknown')  # 'Unknown' si le driver_number n'est pas trouvé


with open('positions.json', 'w') as output_file:
    json.dump(position_data, output_file, indent=4)

