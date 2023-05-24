#DATOS SE OBTUVIERON DE LA PAGINA DE FIFA--> MUNDIALES---->ESTADISTICAS---> PARTIDO (QUE SE QUIERA ANALIZAR)---->ESTADISTICAS HASTA ABAJO DE LA PAGINA

import networkx as nx
#Grafo COLOMBIA"

G=nx.DiGraph(Equipo="COLOMBIA")  #creacion de grafo

G.clear()
#Nodos con nombre
G.add_nodes(0, name='D. OSPINA')
G.add_nodes(1, name='C. ZAPATA')
G.add_nodes(2, name='M. YEPES')
G.add_nodes(3, name='C. Sanchez')
G.add_nodes(4, name='P. ARMERO')
G.add_nodes(5, name='A. AGUILAR')
G.add_nodes(6, name='T. GUITIERREZ')
G.add_nodes(7, name='J. RODRIGUEZ')
G.add_nodes(8, name='J. CUADRADO')
G.add_nodes(9, name='V. IBARBO')
G.add_nodes(10, name='J. ZINIGA')


#MDP- Matriz de Pases
MDP=([0,8,0,0,2,2,1,1,1,2,4],[1,0,5,1,1,3,0,0,0,0,12],[3,7,0,1,3,2,0,3,0,1,1],[0,1,1,0,5,0,1,5,0,2,1],[1,0,3,2,0,2,3,5,0,2,0],[0,0,4,2,1,0,2,6,2,0,4],[0,1,0,0,2,1,0,7,5,1,2],[0,1,0,3,5,4,9,0,6,6,5],[0,0,0,1,1,3,1,9,0,6,5],[0,0,0,3,0,1,2,3,3,0,4],[0,5,1,3,0,3,9,11,13,8,0])

#empieza el rango desde cero ya que tiene que coincidir con el valor de la matriz
for x in range (0,11):
    for y in range (0,11):
      G.add_weighted_edges_from([(x,y,MDP[x][y])])  #Creador de enlaces con peso
      if MDP[x][y] == 0:
          G.remove_edge(x, y)          #elimina los enlaces que no existen, es decir, con peso = 0 o numero de pases = 0
      else:
          pass

#DATOS EN GEXF PARA GePHI
nx.write_gexf(G,'COL_COLvsGRE.gexf')

#Grafo GRECIA"

G=nx.DiGraph(Equipo="GRECIA")  #creacion de grafo

G.clear() #borrar grafo anterior

#Nodos con nombre
G.add_nodes(0, name='O. KARNEZIS')
G.add_nodes(1, name='I. MANIATIS')
G.add_nodes(2, name='K. MANOLAS')
G.add_nodes(3, name='G. SAMARAS')
G.add_nodes(4, name='P. KONE')
G.add_nodes(5, name='D. SALPINGIDIS')
G.add_nodes(6, name='V. TOROSIDIS')
G.add_nodes(7, name='T. GEKAS')
G.add_nodes(8, name='S. PAPASTHAHOPOLUS')
G.add_nodes(9, name='J. CHOLEVAS')
G.add_nodes(10, name='K. KATSOURANIS')

#MDP- Matriz de Pases
MDP=([0,3,4,0,0,0,2,0,4,1,1],[0,0,4,3,2,4,14,1,4,2,4],[3,3,0,0,2,1,6,0,6,0,10],[0,4,0,0,3,1,1,0,1,10,8],[0,6,2,1,0,0,3,0,1,7,6],[0,4,0,0,0,0,1,0,0,0,4],[0,13,8,1,2,7,0,5,3,0,3],[0,0,0,3,1,2,2,0,0,0,0],[3,1,2,5,5,0,2,0,0,5,10],[0,3,5,10,7,0,3,0,4,0,7],[0,14,4,6,6,3,12,1,5,7,0])

#empieza el rango desde cero ya que tiene que coincidir con el valor de la matriz
for x in range (0,11):
    for y in range (0,11):
      G.add_weighted_edges_from([(x,y,MDP[x][y])])  #Creador de enlaces con peso
      if MDP[x][y] == 0:
          G.remove_edge(x, y)          #elimina los enlaces que no existen, es decir, con peso = 0 o numero de pases = 0
      else:
          pass

#DATOS EN GEXF PARA GePHI
nx.write_gexf(G,'GRE_COLvsGRE.gexf')