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
    [0, 3, 5, 3, 2, 2, 1, 4, 2, 4, 8],
    [0, 0, 1, 1, 7, 6, 3, 0, 0, 7, 6],
    [0, 1, 0, 2, 5, 1, 0, 0, 0, 4, 1],
    [0, 1, 0, 0, 3, 3, 2, 12, 8, 6, 3],
    [3, 8, 1, 9, 0, 11, 0, 3, 4, 7, 11],
    [0, 4, 0, 6, 5, 0, 2, 4, 4, 9, 2],
    [0, 0, 0, 1, 1, 2, 0, 2, 0, 4, 2],
    [0, 0, 2, 4, 2, 5, 4, 0, 8, 4, 1],
    [7, 1, 2, 6, 5, 3, 1, 9, 0, 4, 5],
    [0, 3, 0, 6, 13, 7, 3, 12, 7, 0, 4],
    [7, 2, 2, 5, 7, 1, 3, 3, 2, 9, 0]
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
nx.write_gexf(A,'ALEvsBra_Semi.gexf')




