#DATOS SE OBTUVIERON DE LA PAGINA DE FIFA--> MUNDIALES---->ESTADISTICAS---> PARTIDO (QUE SE QUIERA ANALIZAR)---->ESTADISTICAS HASTA ABAJO DE LA PAGINA

import networkx as nx
#Grafo Brazil"

BR=nx.DiGraph(Equipo="Brazil")  #creacion de grafo

BR.clear()
#Nodos con nombre
BR.add_node(0, Label='J.Cesar')
BR.add_node(1, Label='D. Alves')
BR.add_node(2, Label='T. Silva')
BR.add_node(3, Label='D. Luiz')
BR.add_node(4, Label='Marcelo')
BR.add_node(5, Label='Hulk')
BR.add_node(6, Label='Paulinho')
BR.add_node(7, Label='Fred')
BR.add_node(8, Label='Neymar')
BR.add_node(9, Label='Oscar')
BR.add_node(10, Label='L. Gustavo')

#MDP- Matriz de Pases
MDPBr = ([0,2,6,2,2,0,0,2,2,0,0],[1,0,14,2,0,3,8,1,10,22,7],[1,20,0,15,2,1,2,1,3,7,13],
       [2,6,13,0,13,2,2,0,1,2,9],[0,1,5,10,0,6,2,1,14,5,8],[0,2,1,0,6,0,1,1,1,2,0],
       [0,6,2,3,4,0,0,1,3,1,1],[0,1,0,1,0,0,1,0,1,1,1],[0,4,3,4,7,5,1,1,0,2,3],
       [0,11,2,2,0,3,3,0,5,0,3],[1,10,13,10,8,3,5,1,3,2,0])

#empieza el rango desde cero ya que tiene que coincidir con el valor de la matriz
for x in range (0,11):
    for y in range (0,11):
      BR.add_weighted_edges_from([(x,y,MDPBr[x][y])])  #Creador de enlaces con peso
      if MDPBr[x][y] == 0:
          BR.remove_edge(x, y)          #elimina los enlaces que no existen, es decir, con peso = 0 o numero de pases = 0
      else:
          pass

#DATOS EN GEXF PARA GePHI
nx.write_gexf(BR,'BR_BRAvsCRO.gexf')

#Grafo CROACIA"

C=nx.DiGraph(Equipo="Croatia")  #creacion de grafo

C.clear() #borrar grafo anterior

#Nodos con nombre
C.add_node(0, nom='S. Pletikosa')  #creado de nodos en el grafo C
C.add_node(1, nom='S. Vrsaljko')
C.add_node(2, nom='I. Perisic')
C.add_node(3, nom='V. Corluka')
C.add_node(4, nom='D. Lovren')
C.add_node(5, nom='I. Rakitic')
C.add_node(6, nom='N. Jelavic')
C.add_node(7, nom='L. Modric')
C.add_node(8, nom='D. Srna')
C.add_node(9, nom='I. Olic')
C.add_node(10, nom='M. Kovacic')

#MDP- Matriz de Pases
MDP=([0,1,3,2,0,0,5,1,1,1,2],[2,0,0,2,1,7,0,1,1,0,12,3],[0,1,0,0,2,0,0,5,1,2,0],
     [1,3,1,0,2,4,1,7,4,1,0],[2,2,2,1,0,2,0,1,1,2,2],[1,5,3,4,2,0,1,7,2,5,6],
     [0,0,1,1,0,0,0,2,0,2,2],[0,6,9,8,2,10,4,0,7,0,2],[0,0,3,4,1,2,2,6,0,1,1],
     [0,5,0,0,0,1,1,1,0,0,3],[0,2,0,0,1,4,2,6,0,2,0])

#empieza el rango desde cero ya que tiene que coincidir con el valor de la matriz
for x in range (0,11):
    for y in range (0,11):
      C.add_weighted_edges_from([(x,y,MDP[x][y])])  #Creador de enlaces con peso
      if MDP[x][y] == 0:
          C.remove_edge(x, y)          #elimina los enlaces que no existen, es decir, con peso = 0 o numero de pases = 0
      else:
          pass

#DATOS EN GEXF PARA GePHI
nx.write_gexf(C,'CRO_BRAvsCRO.gexf')