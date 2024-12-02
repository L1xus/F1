import json

# Exemple de données JSON
with open('laplap.json', 'r') as pos_file:
    data = json.load(pos_file)


# Dictionnaire pour stocker les données agrégées
driver_durations = {}

# Parcourir les sessions
for session_key, drivers in data.items():
    for driver_number, laps in drivers.items():
        # Initialiser les listes pour chaque conducteur si elles n'existent pas encore
        if driver_number not in driver_durations:
            driver_durations[driver_number] = {
                "duration_sector_1": [],
                "duration_sector_2": [],
                "duration_sector_3": [],
                "lap_duration": []
            }
        
        # Ajouter les durées des secteurs et des tours
        for lap in laps:
            if "duration_sector_1" in lap and lap["duration_sector_1"] is not None:
                driver_durations[driver_number]["duration_sector_1"].append(lap["duration_sector_1"])
            if "duration_sector_2" in lap and lap["duration_sector_2"] is not None:
                driver_durations[driver_number]["duration_sector_2"].append(lap["duration_sector_2"])
            if "duration_sector_3" in lap and lap["duration_sector_3"] is not None:
                driver_durations[driver_number]["duration_sector_3"].append(lap["duration_sector_3"])
            if "lap_duration" in lap and lap["lap_duration"] is not None:
                driver_durations[driver_number]["lap_duration"].append(lap["lap_duration"])

# Calculer les moyennes pour chaque conducteur
driver_duration_averages = {
    driver: {
        "average_duration_sector_1": sum(durations["duration_sector_1"]) / len(durations["duration_sector_1"]) if durations["duration_sector_1"] else 0,
        "average_duration_sector_2": sum(durations["duration_sector_2"]) / len(durations["duration_sector_2"]) if durations["duration_sector_2"] else 0,
        "average_duration_sector_3": sum(durations["duration_sector_3"]) / len(durations["duration_sector_3"]) if durations["duration_sector_3"] else 0,
        "average_lap_duration": sum(durations["lap_duration"]) / len(durations["lap_duration"]) if durations["lap_duration"] else 0
    }
    for driver, durations in driver_durations.items()
}


with open("avrg_durations.json", "w") as json_file:
    json.dump(driver_duration_averages, json_file, indent=4)

print(f"Les moyennes des durées ont été enregistrées dans ")
