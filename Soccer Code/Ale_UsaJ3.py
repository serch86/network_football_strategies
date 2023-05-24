# DATOS SE OBTUVIERON DE LA PAGINA DE FIFA--> MUNDIALES---->ESTADISTICAS---> PARTIDO (QUE SE QUIERA ANALIZAR)---->ESTADISTICAS HASTA ABAJO DE LA PAGINA

import networkx as nx
#Grafo ALEMANIA"

A=nx.DiGraph(Equipo="Alemania")  #creacion de grafo

A.clear() #borrar grafo anterior

#Nodos con nombre
A.add_node(0, nom='M NEUER')  #creado de nodos en el grafo A
A.add_node(1, nom='B. HOEWEDES')
A.add_node(2, nom='M. HUMMELS')
A.add_node(3, nom='B. SCHWEINSTEIGER')
A.add_node(4, nom='M. OEZIL')
A.add_node(5, nom='L. PODOLSKI')
A.add_node(6, nom='T. MUELLER')
A.add_node(7, nom='P. LAHM')
A.add_node(8, nom='P. MERTESACKER')
A.add_node(9, nom='T. KROOS')
A.add_node(10, nom='J. BOATENG')

#MDP- Matriz de Pases
MDP=(
    [0, 3, 10, 0, 2, 0, 0, 6, 8, 2, 0],
    [1, 0, 9, 9, 7, 5, 1, 4, 0, 11, 1],
    [5, 7, 0, 6, 5, 1, 0, 12, 10, 16, 1],
    [0, 7, 6, 0, 9, 7, 4, 10, 8, 16, 7],
    [0, 6, 0, 9, 0, 4, 3, 9, 3, 12, 4],
    [0, 4, 0, 10, 3, 0, 0, 0, 0, 3, 0],
    [0, 0, 0, 4, 8, 1, 0, 4, 1, 2, 6],
    [3, 5, 12, 11, 7, 1, 9, 0, 27, 22, 10],
    [13, 1, 7, 11, 7, 0, 3, 32, 0, 15, 18],
    [0, 8, 5, 17, 10, 6, 5, 23, 13, 0, 10],
    [1, 0, 3, 7, 4, 2, 8, 7, 25, 1, 0]
)

#empieza el rango desde cero ya que tiene que coincidir con el valor de la matriz
for x in range (0,11):
    for y in range (0,11):
      A.add_weighted_edges_from([(x,y,MDP[x][y])])  #Creador de enlaces con peso
      if MDP[x][y] == 0:
          A.remove_edge(x, y)          #elimina los enlaces que no existen, es decir, con peso = 0 o numero de pases = 0
      else:
          pass

#DATOS EN GEXF PARA GePHI
nx.write_gexf(A,'ALEvsUSAJ3.gexf')

