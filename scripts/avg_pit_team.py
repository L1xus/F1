import json


def avg_pit_team(pits):
    with open('data/drivers.json', 'r') as pos_file:
        drivers_data = json.load(pos_file)

    # Création d'un dictionnaire associant chaque driver_number à son team_name
    driver_team_mapping = {driver['driver_number']: driver['team_name'] for driver in drivers_data}

    # Création d'un dictionnaire pour stocker les durées par équipe
    team_pit_durations = {}

    # Ajout du team_name aux lap_times et agrégation par équipe
    for driver_number, times in pits.items():
        driver_number_int = int(driver_number)  # Convertir la clé en entier pour correspondre au driver_number
        team_name = driver_team_mapping.get(driver_number_int, "Unknown Team")  # Récupérer le nom de l'équipe
        pit_duration = times["average_pit_duration"]  # Récupérer la durée moyenne

        # Ajouter les durées dans le dictionnaire d'agrégation
        if team_name not in team_pit_durations:
            team_pit_durations[team_name] = []
        team_pit_durations[team_name].append(pit_duration)

    # Calcul de la moyenne pour chaque équipe
    team_pit_average = {
        team: sum(durations) / len(durations) for team, durations in team_pit_durations.items()
    }

    return team_pit_average
