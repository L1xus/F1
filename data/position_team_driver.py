import json
from itertools import groupby


with open('positions.json', 'r') as file:
    position_data = json.load(file)


position_data_sorted = sorted(position_data, key=lambda x: (x['position'], x['driver_number']))


with open('positionss.json', 'w') as output_file:
    json.dump(position_data_sorted, output_file, indent=4)
