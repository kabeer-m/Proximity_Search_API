def nearest_point(lat, lon, locations):
    best = None
    best_dist = None

    for loc in locations:
        loc_id, loc_lon, loc_lat, category = loc

        d_lat = loc_lat - lat
        d_lon = loc_lon - lon
        dist = d_lat * d_lat + d_lon * d_lon   # squared distance, no sqrt needed

        if best_dist is None or dist < best_dist:
            best = loc
            best_dist = dist

    return best