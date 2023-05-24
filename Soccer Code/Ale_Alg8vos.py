#Grafo ALEMANIA"
import networkx as nx

A=nx.DiGraph(Equipo="Alemania")  #creacion de grafo

A.clear() #borrar grafo anterior

#Nodos con nombre
A.add_node(0, nom='M NEUER')  #creado de nodos en el grafo A
A.add_node(1, nom='B. HOEWEDES')
A.add_node(2, nom='B. SCHWEINSTEIGER')
A.add_node(3, nom='M. OEZIL')
A.add_node(4, nom='T. MUELLER')
A.add_node(5, nom='P. LAHM')
A.add_node(6, nom='P. MERTESACKER')
A.add_node(7, nom='T. KROOS')
A.add_node(8, nom='M. GOETZE')
A.add_node(9, nom='J. BOATENG')
A.add_node(10, nom='S. MUSTAFI')

#MDP- Matriz de Pases
MDP=(
    [0, 0, 2, 1, 2, 1, 10, 2, 1, 14, 0],
    [3, 0, 9, 9, 8, 2, 1, 7, 3, 11, 0],
    [0, 0, 0, 16, 8, 16, 7, 12, 7, 13, 3],
    [0, 2, 9, 0, 13, 6, 3, 7, 3, 7, 3],
    [0, 2, 3, 7, 0, 0, 0, 7, 2, 1, 1],
    [1, 4, 16, 3, 4, 0, 18, 18, 1, 11, 4],
    [6, 3, 14, 7, 3, 20, 0, 15, 2, 9, 4],
    [3, 5, 17, 18, 8, 15, 6, 0, 2, 11, 4],
    [1, 4, 4, 2, 1, 0, 2, 4, 0, 2, 0],
    [8, 7, 16, 9, 2, 12, 14, 15, 3, 0, 2],
    [3, 0, 4, 2, 1, 0, 9, 2, 0, 0, 0]
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
nx.write_gexf(A,'ALEvsAlg8vos.gexf')

