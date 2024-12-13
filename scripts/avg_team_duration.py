import json
from collections import defaultdict

def avg_team_duration(performances):
    # Charger les données
    with open('data/drivers.json', 'r') as f:
        pilotes = json.load(f)

    # Association des pilotes à leurs équipes
    team_data = {}
    for pilote in pilotes:
        driver_number = pilote["driver_number"]
        team_name = pilote["team_name"]
        team_data[driver_number] = team_name

    # Initialisation des structures pour calculer les moyennes
    team_aggregates = defaultdict(lambda: {'sector_1': [], 'sector_2': [], 'sector_3': [], 'lap': []})

    # Ajouter les performances aux équipes
    for driver_number, performance in performances.items():
        driver_number = int(driver_number)  # Conversion en entier pour correspondre
        if driver_number in team_data:  # S'assurer que le pilote existe dans les données d'équipe
            team_name = team_data[driver_number]
            team_aggregates[team_name]['sector_1'].append(performance['average_duration_sector_1'])
            team_aggregates[team_name]['sector_2'].append(performance['average_duration_sector_2'])
            team_aggregates[team_name]['sector_3'].append(performance['average_duration_sector_3'])
            team_aggregates[team_name]['lap'].append(performance['average_lap_duration'])

    # Calculer les moyennes par équipe
    team_averages = {}
    for team, durations in team_aggregates.items():
        team_averages[team] = {
            'average_duration_sector_1': sum(durations['sector_1']) / len(durations['sector_1']) if durations['sector_1'] else 0,
            'average_duration_sector_2': sum(durations['sector_2']) / len(durations['sector_2']) if durations['sector_2'] else 0,
            'average_duration_sector_3': sum(durations['sector_3']) / len(durations['sector_3']) if durations['sector_3'] else 0,
            'average_lap_duration': sum(durations['lap']) / len(durations['lap']) if durations['lap'] else 0,
        }

    return team_averages
