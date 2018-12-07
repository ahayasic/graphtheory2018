import networkx as nx
import numpy    as np
import matplotlib.pyplot   as plt


def draw(G, titulo):
    pos = nx.circular_layout(G)

    labels = nx.get_edge_attributes(G, 'weight')

    plt.figure(figsize=(9,9))
    nx.draw_networkx_labels(G, pos, font_size=10)
    nx.draw_networkx_nodes(G,  pos, node_color='#f39c12', node_size=220, with_labels = True)
    nx.draw_networkx_edges(G,  pos, edge_color='#3498db', width=2.0)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, label_pos=0.3, font_size=9)
    plt.title(titulo)
    plt.show()


def dijkstra(G, raizes):
    Q = {}
    for v in G:
        attrs = {v : {'d': np.inf, 'p': None}}
        nx.set_node_attributes(G, attrs)    
        Q[v] = G.nodes[v]
    
    for s in raizes:
        G.nodes[s]['d'] = 0
        
    S = []
    while Q:
        min_weight = min([Q[i]['d'] for i in Q])
        u = [i for i in Q if Q[i]['d'] == min_weight][0]
        S.append(u)
        del Q[u]
        
        for v in G.neighbors(u): 
            aux = G.nodes[u]['d'] + G.get_edge_data(u, v)['weight']
            if  G.nodes[v]['d'] > aux:  
                G.nodes[v]['d'] = aux   
                G.nodes[v]['p'] = u     
                
    dijkstra_tree = nx.Graph()
    for v in S:
        if G.nodes[v]['p'] != None:
            dijkstra_tree.add_edge(G.nodes[v]['p'], v, weight = G.get_edge_data(G.nodes[v]['p'], v)['weight']) 
            
    return dijkstra_tree


def main():
    A = np.loadtxt('wg59_dist.txt')
    G = nx.from_numpy_matrix(A)
    graph1 = dijkstra(G, [0, 28])
    graph2 = dijkstra(G, [0, 28, 58])
    draw(graph1, 'Floresta de Caminhos Mínimos para sementes 0 e 28')
    draw(graph2, 'Floresta de Caminhos Mínimos para sementes 0, 28, 58')


if __name__ == '__main__':
    main()