import json

# Exemple de données JSON
with open('pitpit.json', 'r') as pos_file:
    data = json.load(pos_file)


# Dictionnaire pour stocker les données agrégées
driver_durations = {}

# Parcourir les sessions
for session_key, drivers in data.items():
    for driver_number, laps in drivers.items():
        # Initialiser les listes pour chaque conducteur si elles n'existent pas encore
        if driver_number not in driver_durations:
            driver_durations[driver_number] = {
                "pit_duration": []
            }
        
        # Ajouter les durées des secteurs et des tours
        for lap in laps:
            if "pit_duration" in lap and lap["pit_duration"] is not None:
                driver_durations[driver_number]["pit_duration"].append(lap["pit_duration"])


# Calculer les moyennes pour chaque conducteur
driver_duration_pit_avrg = {
    driver: {
        "average_pit_duration": sum(durations["pit_duration"]) / len(durations["pit_duration"]) if durations["pit_duration"] else 0
    }
    for driver, durations in driver_durations.items()
}


with open("avrg_pits.json", "w") as json_file:
    json.dump(driver_duration_pit_avrg, json_file, indent=4)

print(f"Les moyennes des durées ont été enregistrées dans ")
