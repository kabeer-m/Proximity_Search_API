import csv

# CSV file se locations read krna
def load_locations(path):
    locations = []

    with open(path, newline="") as f:
        #class 11 ki yaad aa gayi
        reader = csv.DictReader(f)   
        for row in reader:
            
            loc_id = int(row["ID"])
            lon = float(row["Longitude"])
            lat = float(row["Latitude"])
            category = row["Category"]
            
            locations.append((loc_id, lon, lat, category))
    #ye AI nhi hai maine khud likha pakka pakka promise sacchi me T-T
    return locations
