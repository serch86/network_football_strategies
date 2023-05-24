#DATOS SE OBTUVIERON DE LA PAGINA DE FIFA--> MUNDIALES---->ESTADISTICAS---> PARTIDO (QUE SE QUIERA ANALIZAR)---->ESTADISTICAS HASTA ABAJO DE LA PAGINA

import networkx as nx
#Grafo Mexico"

M = nx.DiGraph(Equipo="Mexico")  #creacion de grafo

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
MDPMx = ([0,6,6,1,1,1,2,0,0,1,0],[2,0,17,7,1,3,12,1,2,9,16],[2,19,0,5,4,2,12,4,2,0,6],
       [0,7,2,0,3,4,1,2,6,10,2],[1,1,1,4,0,1,13,4,1,0,6],[0,3,2,6,2,0,1,1,4,4,4],
       [1,9,14,3,9,3,0,9,1,1,10],[1,3,0,2,7,4,5,0,0,1,5],[0,1,0,2,0,5,0,3,0,1,2],
       [0,10,2,10,0,7,5,1,0,0,2],[0,11,6,11,4,3,14,7,0,1,0])

#empieza el rango desde cero ya que tiene que coincidir con el valor de la matriz
for x in range (0,11):
    for y in range (0,11):
      M.add_weighted_edges_from([(x,y,MDPMx[x][y])])  #Creador de enlaces con peso
      if MDPMx[x][y] == 0:
          M.remove_edge(x, y)          #elimina los enlaces que no existen, es decir, con peso = 0 o numero de pases = 0
      else:
          pass

#DATOS EN GEXF PARA GePHI
nx.write_gexf(M,'MX_MEXvsCAM.gexf')

#Grafo Camerun"

C=nx.DiGraph(Equipo="Camerun")  #creacion de grafo

C.clear() #borrar grafo anterior

#Nodos con nombre
C.add_node(0, nom='C. Itandje')  #creado de nodos en el grafo C
C.add_node(1, nom='B. Assou Ekotto')
C.add_node(2, nom='N. NKOULOU')
C.add_node(3, nom='C. Djeudoue')
C.add_node(4, nom='A. Song')
C.add_node(5, nom='B. Moukandjo')
C.add_node(6, nom='S. Etoo')
C.add_node(7, nom='E. Choupo Moting')
C.add_node(8, nom='A. Chedjou')
C.add_node(9, nom='S. Mbia')
C.add_node(10, nom='E. Enoh')

#MDP- Matriz de Pases
MDPCam=([0,2,0,0,0,2,0,1,1,5,2],[0,0,2,0,5,0,5,9,6,4,5],[1,2,0,2,3,1,1,1,4,3,0],
        [0,0,0,0,3,2,1,1,1,1,0],[0,7,0,1,0,4,2,2,2,5,4],[0,0,2,2,2,0,1,1,0,3,0],
        [0,1,0,0,1,3,0,1,1,5,1],[0,7,0,0,1,1,5,0,1,1,2],[3,10,5,0,3,1,1,2,0,4,0],
        [0,3,0,2,3,6,7,2,3,5,0,5],[0,3,0,1,5,1,5,4,2,2,0])

#empieza el rango desde cero ya que tiene que coincidir con el valor de la matriz
for x in range (0,11):
    for y in range (0,11):
      C.add_weighted_edges_from([(x,y,MDPCam[x][y])])  #Creador de enlaces con peso
      if MDPCam[x][y] == 0:
          C.remove_edge(x, y)          #elimina los enlaces que no existen, es decir, con peso = 0 o numero de pases = 0
      else:
          pass

#DATOS EN GEXF PARA GePHI
nx.write_gexf(C,'CAM_MEXvsCAM.gexf')