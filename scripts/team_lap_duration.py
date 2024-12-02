import json

# Données de lap times
# Get this From the cloud
with open('team_duration.json', 'r') as pos_file:
    lap_times = json.load(pos_file)

# Dictionnaire pour accumuler les durées des tours et les comptes pour chaque équipe
team_lap_durations = {}

# Parcours des données des pilotes pour accumuler les durées des tours par équipe
for driver_number, times in lap_times.items():
    team_name = times["team_name"]  # Récupérer le nom de l'équipe
    lap_duration = times["average_lap_duration"]
    
    # Si lap_duration est valide (supérieur à zéro)
    if lap_duration > 0:
        if team_name not in team_lap_durations:
            team_lap_durations[team_name] = {"total_duration": 0, "count": 0}
        
        # Ajouter la durée du tour et augmenter le compteur pour cette équipe
        team_lap_durations[team_name]["total_duration"] += lap_duration
        team_lap_durations[team_name]["count"] += 1

# Calcul de la moyenne des durées des tours pour chaque équipe
team_average_lap_durations = {}
for team, data in team_lap_durations.items():
    if data["count"] > 0:
        average_duration = data["total_duration"] / data["count"]
        team_average_lap_durations[team] = average_duration

#tri croissant
sorted_team_average_lap_durations = dict(sorted(team_average_lap_durations.items(), key=lambda item: item[1]))

# Affichage des résultats
with open("team_lap_duration.json", "w") as json_file:
    json.dump(sorted_team_average_lap_durations, json_file, indent=4)
