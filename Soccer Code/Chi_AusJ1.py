#DATOS SE OBTUVIERON DE LA PAGINA DE FIFA--> MUNDIALES---->ESTADISTICAS---> PARTIDO (QUE SE QUIERA ANALIZAR)---->ESTADISTICAS HASTA ABAJO DE LA PAGINA

import networkx as nx
#Grafo Chile"

G=nx.DiGraph(Equipo="Chile")  #creacion de grafo

G.clear()
#Nodos con nombre
G.add_node(0, name='C. Bravo')
G.add_node(1, name='E. Mena')
G.add_node(2, name='M. Isla')
G.add_node(3, name='A. Sanchez')
G.add_node(4, name='A. Vidal')
G.add_node(5, name='J. Valdivia')
G.add_node(6, name='E. Vargas')
G.add_node(7, name='G. Medel')
G.add_node(8, name='G. Jara')
G.add_node(9, name='C. Aranguiz')
G.add_node(10, name='M. DIAZ')

#MDP- Matriz de Pases
MDP=([0,5,0,1,0,1,3,7,13,1,4],[0,0,1,4,6,9,10,1,15,4,8],[2,0,0,17,8,3,2,16,6,8,8],
     [0,3,4,0,4,3,3,3,4,4,2],[0,4,7,1,0,7,2,5,3,3,3],[0,4,4,7,3,0,2,1,3,3,4],
     [0,8,2,3,4,4,0,1,0,3,1],[16,2,20,5,0,2,0,0,8,7,13],[12,21,2,0,5,2,2,6,0,9,16],
     [0,4,6,4,3,9,6,9,4,0,8],[0,11,12,5,8,1,3,12,13,8,0])

#empieza el rango desde cero ya que tiene que coincidir con el valor de la matriz
for x in range (0,11):
    for y in range (0,11):
      G.add_weighted_edges_from([(x,y,MDP[x][y])])  #Creador de enlaces con peso
      if MDP[x][y] == 0:
          G.remove_edge(x, y)          #elimina los enlaces que no existen, es decir, con peso = 0 o numero de pases = 0
      else:
          pass

#DATOS EN GEXF PARA GePHI
nx.write_gexf(G,'CH_CHIvsAUS.gexf')

'''

#Grafo Camerun"

G=nx.DiGraph(Equipo="Australia")  #creacion de grafo

G.clear() #borrar grafo anterior

#Nodos con nombre
G.add_node(0, name='M. RYAN')
G.add_node(1, name='I. FRANJIC')
G.add_node(2, name='J. DAVIDSON')
G.add_node(3, name='T. CAHILL')
G.add_node(4, name='M. MILLIGAN')
G.add_node(5, name='M. SPIRANOVIC')
G.add_node(6, name='M. LECKIE')
G.add_node(7, name='T. OAR')
G.add_node(8, name='M. JEDINAK')
G.add_node(9, name='A. WILKINSON')
G.add_node(10, name='M. BRESCIANO')

#MDP- Matriz de Pases
MDP=([0,3,9,2,2,5,0,2,1,2,1],[1,0,0,3,1,0,5,0,0,3,5],[1,0,0,1,5,7,3,6,4,0,5],
     [0,2,0,0,0,0,7,1,2,0,6],[0,0,4,2,0,3,5,3,6,2,3],[4,0,3,3,4,0,2,0,4,7,2],
     [2,6,3,4,2,1,0,2,4,1,8],[0,0,6,3,0,0,2,0,0,1,0],[2,2,3,0,0,2,0,0,1,0,0],
     [4,4,0,1,0,2,0,0,4,0,4],[0,2,5,5,5,0,7,4,1,2,0])

#empieza el rango desde cero ya que tiene que coincidir con el valor de la matriz
for x in range (0,11):
    for y in range (0,11):
      G.add_weighted_edges_from([(x,y,MDP[x][y])])  #Creador de enlaces con peso
      if MDP[x][y] == 0:
          G.remove_edge(x, y)          #elimina los enlaces que no existen, es decir, con peso = 0 o numero de pases = 0
      else:
          pass

#DATOS EN GEXF PARA GePHI
nx.write_gexf(G,'AUS_CHIvsAUS.gexf')
'''
