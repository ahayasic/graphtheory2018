import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

def draw(G):
    pos = nx.circular_layout(G)
    plt.figure(figsize=(9,9))
    nx.draw_networkx_labels(G, pos, font_size=10)
    nx.draw_networkx_nodes(G,  pos, node_color='#f39c12', node_size=220, with_labels = True)
    nx.draw_networkx_edges(G,  pos, edge_color='#3498db', width=2.0)
    plt.show()


def bfs(G, r):
    for v in G:                             
        attrs = {v: {'color': 'white', 'd': np.inf, 'p': None}}
        nx.set_node_attributes(G, attrs)

    G.nodes[r]['color'] = 'gray'
    G.nodes[r]['d'] = 0
    Q = []             
    Q.append(r)

    while Q:
        u = Q.pop(0)
        for v in G.neighbors(u):
            if G.nodes[v]['color'] == 'white':
                G.nodes[v]['d'] = G.nodes[u]['d'] + 1
                G.nodes[v]['p'] = u
                G.nodes[v]['color'] = 'gray'
                Q.append(v)
        G.nodes[u]['color'] = 'black'
        
    bfs_tree = nx.Graph()   
    for v in G: 
        if G.nodes[v]['p'] != None: 
            bfs_tree.add_edge(G.nodes[v]['p'], v)

    return bfs_tree


def main():
    G1 = nx.read_pajek('karate.paj')
    G2 = nx.read_pajek('dolphins.paj')
    bfs_tree1 = bfs(G1.copy(), '1')
    bfs_tree2 = bfs(G2.copy(), '1')

    print('numero de vertices de G1: {:d}\n'
          'numero de arestas  de G1: {:d}\n'.format(G1.number_of_nodes(),
                                                    G1.number_of_edges()))
    
    print('numero de vertices da G2: {:d}\n'
          'numero de arestas  da G2: {:d}\n'.format(G2.number_of_nodes(),
                                                    G2.number_of_edges()))

    print('numero de vertices da BFS Karate: {:d}\n'
          'numero de arestas  da BFS Karate: {:d}\n'.format(bfs_tree1.number_of_nodes(),
                                                            bfs_tree1.number_of_edges()))

    print('numero de vertices da BFS Dolphins: {:d}\n'
          'numero de arestas  da BFS Dolphins: {:d}\n'.format(bfs_tree2.number_of_nodes(),
                                                              bfs_tree2.number_of_edges()))

    draw(bfs_tree1)
    draw(bfs_tree2)


if __name__ == "__main__":
    main()