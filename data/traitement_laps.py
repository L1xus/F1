import json

with open("laps.json", "r") as file:
    data = json.load(file)


new_data = [
    {"date_start": item["date_start"], "driver_number": item["driver_number"] , "duration_sector_1": item["duration_sector_1"] , "duration_sector_2": item["duration_sector_2"] , "duration_sector_3": item["duration_sector_3"] , "i1_speed": item["i1_speed"] , "i2_speed": item["i2_speed"] , "is_pit_out_lap": item["is_pit_out_lap"] , "lap_duration": item["lap_duration"] , "lap_number": item["lap_number"] , "meeting_key": item["meeting_key"] , "session_key": item["session_key"] , "st_speed": item["st_speed"] }
    for item in data 
]

with open("lapss.json", "w") as file:
    json.dump(new_data, file, indent=4)
