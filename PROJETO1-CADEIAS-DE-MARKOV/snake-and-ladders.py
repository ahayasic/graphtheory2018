import networkx as nx
import numpy    as np
import matplotlib.pyplot as plt

np.random.seed(1)
np.set_printoptions(threshold=np.nan)

def printResults(probs):
    for i in probs: 
        print('vértice: {:d}\t prob: {:.2E}'.format(i, probs[i]))

    print('Probabilidade de se atingir o estado 36:  {:.2e}'.format(probs[36]))

    sorted_probs = sorted(probs, key=probs.__getitem__, reverse=True)
    print('Estados mais provaveis de serem acessados:', sorted_probs[0], sorted_probs[1], 
                                                        sorted_probs[2], sorted_probs[3], 
                                                        sorted_probs[4])
    

def setGraph():
    G = nx.DiGraph()
    G.add_edges_from([(x, y) for x in range(1,36) for y in range(x+1,x+3) if y!= 37])

    G.add_edge(5, 7)
    G.add_edge(2, 15)
    G.add_edge(9, 27)
    G.add_edge(18, 29)
    G.add_edge(25, 35)

    G.add_edge(34, 12)
    G.add_edge(32, 30)
    G.add_edge(24, 16)
    G.add_edge(26, 6)
    G.add_edge(17, 4)

    return G


def powerMethod(P):
    w =  np.zeros(36)
    w[0] = 1

    for i in range(100):
        w = np.dot(w, P)

    probs = {}
    w = w.tolist()
    w = w[0]
    for i in range(0, len(w)):
        probs[i+1] = w[i]

    return probs


def pageRank(P):
    U = np.ones((36,36))
    P_barra = np.dot((1-0.1), P)+ np.dot((0.1*(1/36)), U)

    return powerMethod(P_barra)

def main():
    G = setGraph()

    A = nx.to_numpy_matrix(G)
    delta = np.zeros((36, 36))
    np.fill_diagonal(delta, [1/float(G.degree(i)) for i in range(1, 37) \
                         if G.degree(i) != 0])

    P = np.dot(delta, A)
    probs = powerMethod(P)
    print('Resultados para Cadeia de Markov Tradicional com Power Method')
    printResults(probs)
    probs = pageRank(P)
    print('\n\n')
    print('Resultados para Pagerank com Power Method')
    printResults(probs)

if __name__ == "__main__":
    main()