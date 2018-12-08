# Bibliotecas usadas
import networkx as nx
import numpy as np



# Imprime o tabuleiro
def imprimeTabuleiro(tabuleiro):
    for i in range(0,9):
        print(tabuleiro[i][0],tabuleiro[i][1],tabuleiro[i][2], "|",
              tabuleiro[i][3], tabuleiro[i][4], tabuleiro[i][5], "|",
              tabuleiro[i][6], tabuleiro[i][7], tabuleiro[i][8],
              sep=" ")
        if (i+1)%3 == 0:
            print("-----------------------")

# Função principal, responsavel por chamar outras funções e resolver o sudoku
def resolveSudoku(tabuleiro, grafo, i=0, j=0):
    add_aresta(tabuleiro, grafo)
    i, j = welshPowell(tabuleiro, grafo)
    if i == -1:
        return True
    for e in range(1, 10):
        # Verifica as restrições do problemas
        if verificaSeValorEValido(tabuleiro, i, j, e):
            tabuleiro[i][j] = e
            if resolveSudoku(tabuleiro, grafo, i, j):
                return True
    return False


# Cria as arestas do grafo
def add_aresta(tabuleiro, grafo):
    for i in range (0,9):
        for j in range (0,9):
            if tabuleiro[i][j] == 0:
                for k in range(0,9):
                    if tabuleiro[i][k] != 0:
                        grafo.add_edge(i+9*j, i+9*k)
                    if tabuleiro[k][j] != 0:
                        grafo.add_edge(i+9*j, k+9*j)

                for k in range(0,3):
                    for l in range(0,3):
                        auxi = i//3
                        auxj = j//3
                        if tabuleiro[auxi+k][auxj+l] != 0:
                            grafo.add_edge(i+9*j,i+k+9*(j+l))
    
                        
# Acha vértice com maior grau
def welshPowell(tabuleiro, grafo):
    maior_grau = 0
    auxi = -1
    auxj = -1
    for i in range(0,9):
        for j in range(0,9):
            if len(list(grafo.neighbors(i+9*j))) > maior_grau and tabuleiro[i][j] == 0:
                maior_grau = len(list(grafo.neighbors(i+9*j)))
                auxi = i
                auxj = j
    return auxi, auxj
    # Se não houver 0s no tabuleiro, retorna -1 -1, assim a função resolveSudoku sabe onde parar
    return -1, -1

# Verifica cada uma das restrições do problema
def verificaSeValorEValido(tabuleiro, i, j, e):
    if verificaLinha(tabuleiro, i, e):
        if verificaColuna(tabuleiro, j, e):
            if verificaBox(tabuleiro, i, j, e):
                return True
        return False
    return False

# Verifica se existe repetição de valores na linhas
def verificaLinha(tabuleiro, i, e):
    linhaOk = all([e != tabuleiro[i][x] for x in range(9)])
    return linhaOk

# Verifica se existe repetição de valores na coluna
def verificaColuna(tabuleiro, j, e):
    colunaOk = all([e != tabuleiro[x][j] for x in range(9)])
    return colunaOk


# Verifica se já existe o valor no Box atual
def verificaBox(tabuleiro, i, j, e):
    boxTopX = 3 * (i // 3) # // retorna apenas a parte inteira da divisão
    boxTopY = 3 * (j // 3)
    for x in range(boxTopX, boxTopX + 3):
        for y in range(boxTopY, boxTopY + 3):
            if tabuleiro[x][y] == e:
                return False
    return True


def main():
    grafo = nx.Graph()


# Exemplo de tabuleiro
    tabuleiro_normal = [[9, 5, 0, 0, 0, 1, 0, 0, 8],
                    [0, 2, 1, 8, 9, 0, 6, 0, 0],
                    [3, 0, 0, 0, 4, 2, 1, 5, 9],
                    [2, 4, 0, 0, 7, 8, 0, 0, 1],
                    [1, 0, 9, 3, 2, 0, 0, 6, 5],
                    [8, 0, 0, 1, 0, 0, 0, 7, 2],
                    [4, 9, 0, 0, 1, 0, 5, 8, 0],
                    [6, 8, 2, 9, 0, 0, 0, 0, 4],
                    [0, 0, 0, 4, 8, 3, 0, 9, 6]]

    # Cria vértices no grafo
    for i in range(0,9):
        for j in range(0,9):
            aux = i+9*j
            grafo.add_node(aux)
    
    print("Estado Inicial:")
    print()
    imprimeTabuleiro(tabuleiro_normal)
    print()
    resolveSudoku(tabuleiro_normal, grafo)
    if resolveSudoku(tabuleiro_normal, grafo):
        print("Problema Resolvido:")
        print()
        imprimeTabuleiro(tabuleiro_normal)
    else:
        print("Não foi possível resolver o Sudoku")


if __name__ == '__main__':
    main()