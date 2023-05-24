#Grafo ALEMANIA"
import networkx as nx

A=nx.DiGraph(Equipo="Alemania")  #creacion de grafo

A.clear() #borrar grafo anterior

#Nodos con nombre
A.add_node(0, nom='M NEUER')  #creado de nodos en el grafo A
A.add_node(1, nom='B. HOEWEDES')
A.add_node(2, nom='M. HUMMELS')
A.add_node(3, nom='S. KHEDIRA')
A.add_node(4, nom='B. SCHWEINSTEIGER')
A.add_node(5, nom='M. OEZIL')
A.add_node(6, nom='M. KLOSE')
A.add_node(7, nom='T. MUELLER')
A.add_node(8, nom='P. LAHM')
A.add_node(9, nom='T. KROOS')
A.add_node(10, nom='J. BOATENG')

#MDP- Matriz de Pases
MDP=(
    [0, 1, 5, 2, 3, 0, 2, 3, 6, 0, 7],
    [1, 0, 2, 4, 5, 3, 4, 1, 1, 4, 1],
    [3, 4, 0, 4, 7, 2, 1, 1, 2, 4, 10],
    [0, 0, 3, 0, 5, 5, 0, 6, 6, 3, 2],
    [3, 3, 8, 10, 0, 5, 1, 1, 5, 6, 4],
    [0, 5, 0, 2, 4, 0, 3, 4, 4, 4, 0],
    [0, 1, 0, 4, 2, 2, 0, 3, 1, 1, 0],
    [0, 0, 0, 3, 2, 2, 2, 0, 7, 3, 1],
    [7, 0, 3, 6, 8, 4, 9, 11, 0, 4, 10],
    [0, 1, 4, 0, 5, 6, 2, 3, 4, 0, 1],
    [6, 1, 8, 3, 5, 1, 4, 3, 9, 0, 0]
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
nx.write_gexf(A,'ALEvsFRA_4TOS.gexf')


