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
MDPMx=([0,2,4,1,1,0,1,0,1,3,0],[1,0,7,7,1,1,3,0,0,5,1],[2,6,0,4,2,1,3,4,3,1,1],
       [1,2,1,0,1,8,1,6,3,13,5],[1,0,0,1,0,3,1,12,0,1,4],[0,0,2,3,1,0,0,1,2,2,6],
       [2,1,0,2,6,1,0,4,2,1,6],[0,1,1,4,8,1,4,0,4,1,3],[0,1,0,6,1,2,0,2,0,1,2],
       [1,3,3,10,1,2,1,1,0,0,3],[0,3,4,7,3,5,4,5,3,3,0])

#empieza el rango desde cero ya que tiene que coincidir con el valor de la matriz
for x in range (0,11):
    for y in range (0,11):
      M.add_weighted_edges_from([(x,y,MDPMx[x][y])])  #Creador de enlaces con peso
      if MDPMx[x][y] == 0:
          M.remove_edge(x, y)          #elimina los enlaces que no existen, es decir, con peso = 0 o numero de pases = 0
      else:
          pass

#DATOS EN GEXF PARA GePHI
nx.write_gexf(M,'MX_MEXvsBRA.gexf')

#Grafo BRAZIL"

G=nx.DiGraph(Equipo="BRAZIL")  #creacion de grafo

G.clear() #borrar grafo anterior

#Nodos con nombre
G.add_node(0, Label='J.Cesar')
G.add_node(1, Label='D. Alves')
G.add_node(2, Label='T. Silva')
G.add_node(3, Label='D. Luiz')
G.add_node(4, Label='Marcelo')
G.add_node(5, Label='Paulinho')
G.add_node(7, Label='Fred')
G.add_node(8, Label='Neymar')
G.add_node(9, Label='Oscar')
G.add_node(10, Label='Bernard')
G.add_node(11, Label='L. Gustavo')

#MDP- Matriz de Pases
MDP=([0,2,2,1,1,2,4,1,0,0,0],[0,0,5,0,4,9,2,3,7,5,5],[1,14,0,10,4,2,1,0,2,0,5],
     [3,1,13,0,12,1,1,0,4,0,1],[0,3,1,8,0,3,1,15,14,7,2],
     [0,7,1,2,0,0,0,5,1,0,2],[0,0,0,0,0,2,0,1,3,0,0],[0,3,0,2,4,2,3,0,5,5,3],
     [0,8,2,4,8,2,1,6,0,0,3],[0,3,0,1,4,0,0,2,2,0,1],[1,3,6,4,8,1,1,2,7,1,0])

#empieza el rango desde cero ya que tiene que coincidir con el valor de la matriz
for x in range (0,11):
    for y in range (0,11):
      G.add_weighted_edges_from([(x,y,MDP[x][y])])  #Creador de enlaces con peso
      if MDP[x][y] == 0:
          G.remove_edge(x, y)          #elimina los enlaces que no existen, es decir, con peso = 0 o numero de pases = 0
      else:
          pass

#DATOS EN GEXF PARA GePHI
nx.write_gexf(G,'BRA_MEXvsBRA.gexf')