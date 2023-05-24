#Grafo ALEMANIA"
import networkx as nx

A=nx.DiGraph(Equipo="Alemania")  #creacion de grafo

A.clear() #borrar grafo anterior

#Nodos con nombre
A.add_node(0, nom='M NEUER')  #creado de nodos en el grafo A
A.add_node(1, nom='B. HOEWEDES')
A.add_node(2, nom='M. HUMMELS')
A.add_node(3, nom='S. KHEDIRA')
A.add_node(4, nom='M. OEZIL')
A.add_node(5, nom='T. MUELLER')
A.add_node(6, nom='P. LAHM')
A.add_node(7, nom='P. MERTESACKER')
A.add_node(8, nom='T. KROOS')
A.add_node(9, nom='M. GOETZE')
A.add_node(10, nom='J. BOATENG')

#MDP- Matriz de Pases
MDP=(
    [0, 2, 8, 0, 1, 1, 3, 2, 1, 0, 6],
    [1, 0, 7, 1, 3, 2, 6, 0, 13, 6, 2],
    [3, 8, 0, 5, 2, 1, 8, 9, 11, 0, 0],
    [1, 6, 1, 0, 6, 6, 8, 1, 3, 3, 6],
    [1, 1, 1, 7, 0, 4, 4, 1, 3, 3, 2],
    [0, 0, 0, 4, 1, 0, 2, 0, 5, 6, 3],
    [0, 6, 10, 6, 4, 4, 0, 1, 15, 9, 5],
    [4, 0, 10, 4, 3, 0, 2, 0, 1, 1, 4],
    [0, 4, 8, 8, 6, 6, 18, 2, 0, 13, 0],
    [0, 8, 2, 1, 4, 3, 5, 0, 7, 0, 3],
    [6, 2, 1, 4, 5, 5, 2, 7, 4, 3, 0]

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
nx.write_gexf(A,'ALEvsPOR_J1.gexf')




