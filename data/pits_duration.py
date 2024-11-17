import json
from collections import defaultdict

with open("traitement_pits.json", "r") as file:
    pit_data = json.load(file)


team_data = defaultdict(list)
for pit in pit_data:
    team_data[pit["team_name"]].append(pit["pit_duration"])

average_pit_duration_per_team = {
    team: sum(durations) / len(durations) for team, durations in team_data.items()
}


with open("pits_duration.json", "w") as file:
    json.dump(average_pit_duration_per_team, file, indent=4)

