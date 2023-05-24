#DATOS SE OBTUVIERON DE LA PAGINA DE FIFA--> MUNDIALES---->ESTADISTICAS---> PARTIDO (QUE SE QUIERA ANALIZAR)---->ESTADISTICAS HASTA ABAJO DE LA PAGINA
import networkx as nx
#GrafoCOLOMBIA"

G=nx.DiGraph(Equipo="COLOMBIA")  #creacion de grafo

G.clear()
#Nodos con nombre
G.add_node(0, name='D. OSPINA')
G.add_node(1, name='C. ZAPATA')
G.add_node(2, name='M. YEPES')
G.add_node(3, name='C. SANCHEZ')
G.add_node(4, name='P. ARMERO')
G.add_node(5, name='A. AGUILAR')
G.add_node(6, name='T. GUTIERREZ')
G.add_node(7, name='J. RODRIGUEZ')
G.add_node(8, name='J. CUADRADO')
G.add_node(9, name='J. ZUNIGA')
G.add_node(10, name='J. MARTINEZ')


#MDP - Matriz de Pases
MDP = ([0,5,3,2,1,1,0,0,0,1,9],[1,0,10,0,1,3,1,4,2,14,4],[2,9,0,4,7,3,2,1,2,1,0],
       [1,3,3,0,3,4,2,0,2,5,0],[2,1,1,3,0,8,2,11,9,1,5],[0,4,1,4,6,0,3,12,8,8,2],
       [0,0,1,1,0,3,0,2,2,2,4],[0,1,4,1,5,7,1,0,3,4,2],[1,1,2,3,5,7,4,0,0,6,0],
       [1,6,0,3,0,7,1,4,8,0,3],[0,0,0,0,4,1,3,4,1,0,0])


#empieza el rango desde cero ya que tiene que coincidir con el valor de la matriz
for x in range (0,11):
    for y in range (0,11):
      G.add_weighted_edges_from([(x,y,MDP[x][y])])  #Creador de enlaces con peso
      if MDP[x][y] == 0:
          G.remove_edge(x, y)          #elimina los enlaces que no existen, es decir, con peso = 0 o numero de pases = 0
      else:
          pass

#DATOS EN GEXF PARA GePHI
nx.write_gexf(G,'COL_COLvsURU_8VOS.gexf')

#Grafo URUGUAY"

G=nx.DiGraph(Equipo="URUGUAY")  #creacion de grafo

G.clear() #borrar grafo anterior

#Nodos con nombre
G.add_node(0, Label='')
G.add_node(1, Label='')
G.add_node(2, Label='')
G.add_node(3, Label='')
G.add_node(4, Label='')
G.add_node(5, Label='')
G.add_node(6, Label='')
G.add_node(7, Label='')
G.add_node(8, Label='')
G.add_node(9, Label='')
G.add_node(10, Label='')

#MDP- Matriz de Pases
MDP = ([0,1,4,2,0,3,0,0,1,1,1],[0,0,0,4,0,5,2,1,1,1,13],[0,0,0,6,2,0,0,0,0,4,5],
       [0,0,5,0,3,0,2,1,0,3,5],[0,0,1,1,0,1,2,2,2,5,0],[0,4,0,0,3,0,7,1,2,2,2],
       [1,1,2,1,2,5,0,4,4,1,0],[0,4,1,5,1,2,7,0,2,4,4],[1,1,2,4,2,1,7,1,0,1,1],
       [0,1,0,4,2,1,1,3,2,0,7],[4,7,3,5,3,3,2,6,3,10,0])

#empieza el rango desde cero ya que tiene que coincidir con el valor de la matriz
for x in range (0,11):
    for y in range (0,11):
      G.add_weighted_edges_from([(x,y,MDP[x][y])])  #Creador de enlaces con peso
      if MDP[x][y] == 0:
          G.remove_edge(x, y)          #elimina los enlaces que no existen, es decir, con peso = 0 o numero de pases = 0
      else:
          pass

#DATOS EN GEXF PARA GePHI
nx.write_gexf(G,'URU_COLvsURU_8vos.gexf')