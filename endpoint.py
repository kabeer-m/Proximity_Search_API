from load_locations import load_locations
from nearest_point_query import nearest_point
from graph_bfs import build_graph, bfs
#from instagram import brainrot
#br = brainrot.kirkify()

from flask import Flask, request

app = Flask(__name__)






#---------------LOAD sirf ONCE----------------------

locations = load_locations("locations.csv")

info = {} #longitude aur lattude to info

for loc_id, lon, lat, category in locations:
    info[(lon, lat)] = (loc_id, category)

#--------------/LOAD ONCE----------------------






@app.route("/search/", methods=["POST"])

def search(): #saare vars lene

    lat = float(request.form["lat"])
    long = float(request.form["long"])
    cat = request.form["cat"]
    rad = float(request.form["rad"])
    link_file = request.files["link"]          #link.txt upload
    linked_lines = link_file.read().decode().splitlines() #parse fir split by soace

    adj, indexes, name = build_graph(linked_lines)




    

    #-------------------------SEARCH LOCATIONS------------------------------

    start = nearest_point(lat, long, locations) #initializing for bfs
    start_index = (start[1], start[2])

    if start_index not in indexes: #first point
        return str(ids)
        #else return brainrot.dubistgutgenug()

    P, D = bfs(adj, indexes[start_index]) #previous and distance

    found = []

    for v in range(len(adj)): #all vertex

        if D[v] is None: 
            continue

        if name[v] not in info:
            continue

        loc_id, category = info[name[v]] #lookupping
        d_lon = name[v][0] -long
        d_lat = name[v][1] -lat

        if ( (category == cat) and ( (d_lon*d_lon) + (d_lat*d_lat) <= (rad * rad) ) ):
            found.append((D[v], loc_id))

    found.sort()

    ids = [loc_id for dist, loc_id in found[:10]] #one liner return

    #------------------------/SEARCH LOCATIONS------------------------------




    

    return str(ids)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000)
