import json
# Liste des informations des pilotes
with open('data/drivers.json', 'r') as pos_file:
    drivers_data = json.load(pos_file)


# Données de lap times
# Get This from the Cloud
with open('avrg_durations.json', 'r') as pos_file:
    lap_times = json.load(pos_file)



# Création d'un dictionnaire associant chaque driver_number à son team_name
driver_team_mapping = {driver['driver_number']: driver['team_name'] for driver in drivers_data}

# Ajout du team_name aux lap_times
for driver_number, times in lap_times.items():
    driver_number_int = int(driver_number)  # Convertir la clé en entier pour correspondre au driver_number
    team_name = driver_team_mapping.get(driver_number_int, "Unknown Team")  # Récupérer le nom de l'équipe
    times["team_name"] = team_name  # Ajouter le nom de l'équipe dans les données

# Affichage des résultats
with open("team_duration.json", "w") as json_file:
    json.dump(lap_times, json_file, indent=4)

