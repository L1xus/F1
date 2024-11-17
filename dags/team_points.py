import json
from collections import defaultdict


with open("position_points.json", "r") as json_file:
    data = json.load(json_file)


team_points = defaultdict(int)


for entry in data:
    team_name = entry["team_name"]
    points = entry["points"]
    team_points[team_name] += points


result = dict(team_points)


with open("team_points.json", "w") as output_file:
    json.dump(result, output_file, indent=4)