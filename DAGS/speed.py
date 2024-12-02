import json

# Exemple de données JSON
with open('laplap.json', 'r') as pos_file:
    data = json.load(pos_file)

# Dictionnaire pour stocker les données agrégées
driver_speeds = {}

# Parcourir les sessions
for session_key, drivers in data.items():
    for driver_number, laps in drivers.items():
        # Initialiser les listes si le conducteur n'est pas encore enregistré
        if driver_number not in driver_speeds:
            driver_speeds[driver_number] = {"i1_i2_speeds": [], "st_speeds": []}
        
        # Ajouter les valeurs de i1_speed + i2_speed et de st_speed
        for lap in laps:
            if "i1_speed" in lap and "i2_speed" in lap and lap["i1_speed"] is not None and lap["i2_speed"] is not None:
                driver_speeds[driver_number]["i1_i2_speeds"].append(lap["i1_speed"] + lap["i2_speed"])
            if "st_speed" in lap and lap["st_speed"] is not None:
                driver_speeds[driver_number]["st_speeds"].append(lap["st_speed"])

# Calculer les moyennes pour chaque conducteur
driver_speed_averages = {
    driver: {
        "average_i1_i2_speed": sum(speeds["i1_i2_speeds"]) / len(speeds["i1_i2_speeds"]) if speeds["i1_i2_speeds"] else 0,
        "average_st_speed": sum(speeds["st_speeds"]) / len(speeds["st_speeds"]) if speeds["st_speeds"] else 0
    }
    for driver, speeds in driver_speeds.items()
}



with open("result.json", "w") as json_file:
    json.dump(driver_speed_averages, json_file, indent=4)

print(f"Les moyennes des vitesses ont été enregistrées dans ")
