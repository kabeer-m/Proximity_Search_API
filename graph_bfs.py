# Source: https://www.inf.usi.ch/faculty/carzaniga/edu/algo/bfs.py
#adapted for assignment

def bfs(G, src):                # G: adjacency list, src: source node
    n = len(G)
    D = [None] * n              # D[v]: hop-distance from src to v
    P = [None] * n              # P[v]: previous node

    Q = [None] * n
    Q_tail = 0
    Q_head = 0

    Q[Q_tail] = src
    Q_tail = Q_tail + 1
    D[src] = 0
    P[src] = src

    while Q_tail > Q_head:
        u = Q[Q_head]
        Q_head = Q_head + 1
        for v in G[u]:
            if D[v] == None:
                D[v] = D[u] + 1
                P[v] = u
                Q[Q_tail] = v
                Q_tail = Q_tail + 1

    return P, D


def build_graph(lines):
    Adj = []                    # adjacency list
    Idx = {}                    # node name (lon, lat) -> index in Adj
    Name = []                   # Name[v] is the (lon, lat) of node v

    def add_vertex(u_name):
        if u_name in Idx:
            u = Idx[u_name]
        else:
            u = len(Adj)
            Idx[u_name] = u
            Adj.append([])
            Name.append(u_name)
        return u

    for line in lines:
        ax, ay, bx, by = line.strip().split()
        u = add_vertex((float(ax), float(ay)))
        v = add_vertex((float(bx), float(by)))
        Adj[u].append(v)
        Adj[v].append(u)

    return Adj, Idx, Name
