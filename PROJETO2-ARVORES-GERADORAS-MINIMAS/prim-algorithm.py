import networkx as nx
import numpy as np
import matplotlib.pyplot as plt 


def draw(G):
    pos = nx.circular_layout(G)

    labels = nx.get_edge_attributes(G, 'weight')

    plt.figure(figsize=(9,9))
    nx.draw_networkx_labels(G, pos, font_size=10)
    nx.draw_networkx_nodes(G,  pos, node_color='#f39c12', node_size=220, with_labels = True)
    nx.draw_networkx_edges(G,  pos, edge_color='#3498db', width=2.0)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, label_pos=0.3, font_size=9)
    plt.show()


def prim(G, r):
    Q = {}
    for v in G:
        attrs = {v: {'key': np.inf, 'p': None}} 
        nx.set_node_attributes(G, attrs)
        Q[v] = G.nodes[v]

    G.nodes[r]['key'] = 0 
    S = []

    while Q: 
        min_weight = min([Q[i]['key'] for i in Q])
        u = [i for i in Q if Q[i]['key'] == min_weight][0]
        S.append(u) 
        del Q[u]
        for v in G.neighbors(u):
            if v in Q and G.nodes[v]['key'] > G.get_edge_data(u, v)['weight']:
                G.nodes[v]['key'] = G.get_edge_data(u, v)['weight']
                G.nodes[v]['p'] = u 

    mst = nx.Graph() 
    for v in S: 
        if G.nodes[v]['p'] != None: 
            mst.add_edge(v, G.nodes[v]['p'], weight=G.get_edge_data(v, G.nodes[v]['p'])['weight']) 

    return mst


def main():
    A = np.loadtxt('ha30_dist.txt') 
    G = nx.from_numpy_matrix(A)
    mst = prim(G.copy(), 0)
    print('numero de vertices de G: {:d}\n'
          'numero de arestas  de G: {:d}\n'
          'peso de G:  {:.1f}\n'.format(G.number_of_nodes(),
                                        G.number_of_edges(),
                                        G.size(weight='weight')))
    
    print('numero de vertices da MST: {:d}\n'
          'numero de arestas  da MST: {:d}\n'
          'peso da MST gerada: {:.1f}\n'.format(mst.number_of_nodes(),
                                                mst.number_of_edges(),
                                                mst.size(weight='weight')))
    draw(mst)
    

if __name__ == '__main__':
    main()
