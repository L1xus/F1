import json

def avg_driver_tyre():
    # Exemple de données JSON
    with open('F1/data/stints.json', 'r') as pos_file:
        data = json.load(pos_file)


    # Dictionnaire pour stocker les données agrégées
    driver_durations = {}

    # Parcourir les sessions
    for session_key, drivers in data.items():
        for driver_number, laps in drivers.items():
            # Initialiser les listes pour chaque conducteur si elles n'existent pas encore
            if driver_number not in driver_durations:
                driver_durations[driver_number] = {
                    "tyre_age_at_start": []
                }
            
            # Ajouter les durées des secteurs et des tours
            for lap in laps:
                if "tyre_age_at_start" in lap and lap["tyre_age_at_start"] is not None:
                    driver_durations[driver_number]["tyre_age_at_start"].append(lap["tyre_age_at_start"])


    # Calculer les moyennes pour chaque conducteur
    driver_tyre_age_avg = {
        driver: {
            "tyre_age": sum(durations["tyre_age_at_start"]) / len(durations["tyre_age_at_start"]) if durations["tyre_age_at_start"] else 0
        }
        for driver, durations in driver_durations.items()
    }

    return driver_tyre_age_avg
