import json
from collections import defaultdict

# Charger les données du fichier JSON
with open("names_laps.json", "r") as file:
    data = json.load(file)

team_data = defaultdict(list)

for item in data:
    team_data[item["team_name"]].append(item["lap_duration"])


average_lap_duration_per_team = {
    team: sum(durations) / len(durations) for team, durations in team_data.items()
}


with open("duration_team.json", "w") as file:
    json.dump(average_lap_duration_per_team, file, indent=4)
