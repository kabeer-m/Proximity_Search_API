import csv

def load_locations(path):
    locations = []

    with open(path, newline="") as f:
        reader = csv.DictReader(f)   # comma is the default delimiter
        for row in reader:
            loc_id = int(row["ID"])
            lon = float(row["Longitude"])
            lat = float(row["Latitude"])
            category = row["Category"]
            locations.append((loc_id, lon, lat, category))

    return locations