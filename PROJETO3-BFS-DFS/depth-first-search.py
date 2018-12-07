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


def dfs(G, r):
    for v in G:
        attrs = {v: {'color': 'white', 'p': None, 'd': None, 'f':None}}
        nx.set_node_attributes(G, attrs)
        
    global time
    time = 0
    dfs_visit(G, r)
    
    dfs_tree = nx.Graph() 
    dfs_tree.add_node(r)
    
    for v in G:
        if G.nodes[v]['p'] != None: 
            dfs_tree.add_edge(G.nodes[v]['p'], v) 

    return dfs_tree


def dfs_visit(G, u):
    global time
    time += 1
    G.nodes[u]['d'] = time
    G.nodes[u]['color'] = 'gray'
    
    for v in G.neighbors(u):
        if G.nodes[v]['color'] == 'white':
            G.nodes[v]['p'] = u
            dfs_visit(G, v)
            
    G.nodes[u]['color'] = 'black'  
    time += 1                      
    G.nodes[u]['f'] = time         


def main():
    G1 = nx.read_pajek('karate.paj')
    G2 = nx.read_pajek('dolphins.paj')
    dfs_tree1 = dfs(G1.copy(), '1')
    dfs_tree2 = dfs(G2.copy(), '1')

    print('numero de vertices de G1: {:d}\n'
          'numero de arestas  de G1: {:d}\n'.format(G1.number_of_nodes(),
                                                    G1.number_of_edges()))
    
    print('numero de vertices da G2: {:d}\n'
          'numero de arestas  da G2: {:d}\n'.format(G2.number_of_nodes(),
                                                    G2.number_of_edges()))

    print('numero de vertices da BFS Karate: {:d}\n'
          'numero de arestas  da BFS Karate: {:d}\n'.format(dfs_tree1.number_of_nodes(),
                                                            dfs_tree1.number_of_edges()))

    print('numero de vertices da BFS Dolphins: {:d}\n'
          'numero de arestas  da BFS Dolphins: {:d}\n'.format(dfs_tree2.number_of_nodes(),
                                                              dfs_tree2.number_of_edges()))

    draw(dfs_tree1)
    draw(dfs_tree2)


if __name__ == "__main__":
    main()