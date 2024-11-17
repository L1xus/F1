import json


with open('positions.json', 'r') as drivers_file:
    data = json.load(drivers_file)

for event in data:
    if event['position'] == 1:
        event['points'] = 25
    elif event['position'] == 2:
        event['points'] = 18
    elif event['position'] == 3:
        event['points'] = 15
    else:
        event['points'] = 0  


with open('position_points.json', 'w') as output_file:
    json.dump(data, output_file, indent=4)
