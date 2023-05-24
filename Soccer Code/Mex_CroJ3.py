# DATOS SE OBTUVIERON DE LA PAGINA DE FIFA--> MUNDIALES---->ESTADISTICAS---> PARTIDO (QUE SE QUIERA ANALIZAR)---->ESTADISTICAS HASTA ABAJO DE LA PAGINA

import networkx as nx
#Grafo Mexico"

M=nx.DiGraph(Equipo="Mexico")  #creacion de grafo

M.clear() #borrar grafo anterior

#Nodos con nombre
M.add_node(0, nom='G. Ochoa')  #creado de nodos en el grafo M
M.add_node(1, nom='F. Rodriguez')
M.add_node(2, nom='R. Marquez')
M.add_node(3, nom='H. Herrera')
M.add_node(4, nom='M. Layun')
M.add_node(5, nom='G. Dos Santos')
M.add_node(6, nom='H. Moreno')
M.add_node(7, nom='A. Guardado')
M.add_node(8, nom='O. Peralta')
M.add_node(9, nom='P. Aguilar')
M.add_node(10, nom='J. Vazquez')

#MDP- Matriz de Pases
MDPMx=([0,3,2,3,1,0,0,1,1,3,0],[4,0,6,3,1,0,2,1,0,4,2],[4,3,0,6,3,1,3,2,1,6,6],
       [0,1,3,0,3,7,1,7,6,6,8],[1,0,3,2,0,0,3,7,2,1,5],[0,0,3,3,1,0,0,0,1,2,1],
       [0,2,8,1,6,0,0,3,4,1,2],[1,2,5,6,7,2,0,0,1,1,2],[0,0,0,3,1,3,1,2,0,0,2],
       [0,4,5,12,1,1,1,3,0,0,4],[0,2,1,5,2,1,5,5,2,5,0])

#empieza el rango desde cero ya que tiene que coincidir con el valor de la matriz
for x in range (0,11):
    for y in range (0,11):
      M.add_weighted_edges_from([(x,y,MDPMx[x][y])])  #Creador de enlaces con peso
      if MDPMx[x][y] == 0:
          M.remove_edge(x, y)          #elimina los enlaces que no existen, es decir, con peso = 0 o numero de pases = 0
      else:
          pass

#DATOS EN GEXF PARA GePHI
nx.write_gexf(M,'MX_MEXvsCRO.gexf')

#Grafo CROACIA"

C=nx.DiGraph(Equipo="Croatia")  #creacion de grafo

C.clear() #borrar grafo anterior

#Nodos con nombre
C.add_node(0, nom='S. Pletikosa')  #creado de nodos en el grafo C
C.add_node(1, nom='S. Vrsaljko')
C.add_node(2, nom='D. PRANJIC')
C.add_node(3, nom='I. Perisic')
C.add_node(4, nom='V. Corluka')
C.add_node(5, nom='D. Lovren')
C.add_node(6, nom='I. Rakitic')
C.add_node(7, nom='L. Modric')
C.add_node(8, nom='D. Srna')
C.add_node(9, nom='M. MANDZUKIC')
C.add_node(10, nom='I. OLIC')

#MDP- Matriz de Pases
MDP=([0,2,0,1,5,3,1,1,0,4,1],[2,0,8,0,0,3,3,5,1,2,5],[0,4,0,0,0,4,5,5,1,1,2],
     [0,0,0,0,0,1,4,3,5,1,4],[2,1,0,3,0,13,10,6,4,2,0],[6,8,4,6,4,0,8,2,3,0,3],
     [0,8,3,4,7,9,0,9,6,1,3],[0,5,5,4,9,3,3,0,4,0,1],[1,0,1,8,8,1,5,7,0,2,4],
     [0,0,1,6,0,1,1,1,1,0,0],[0,2,2,1,1,0,2,3,3,1,0])

#empieza el rango desde cero ya que tiene que coincidir con el valor de la matriz
for x in range (0,11):
    for y in range (0,11):
      C.add_weighted_edges_from([(x,y,MDP[x][y])])  #Creador de enlaces con peso
      if MDP[x][y] == 0:
          C.remove_edge(x, y)          #elimina los enlaces que no existen, es decir, con peso = 0 o numero de pases = 0
      else:
          pass

#DATOS EN GEXF PARA GePHI
nx.write_gexf(C,'CRO_MEXvsCRO.gexf')