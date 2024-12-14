import requests
import json
from pathlib import Path

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WebKit /537.36 (KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36"
}

output_dir = Path("F1/data")
output_dir.mkdir(exist_ok=True)

def fetch_data(url):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print("Failed to fetch data:", e)
        return None

def save_to_json(filename, data):
    with open(output_dir / filename, "w") as f:
        json.dump(data, f, indent=4)
