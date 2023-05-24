#DATOS SE OBTUVIERON DE LA PAGINA DE FIFA--> MUNDIALES---->ESTADISTICAS---> PARTIDO (QUE SE QUIERA ANALIZAR)---->ESTADISTICAS HASTA ABAJO DE LA PAGINA

import networkx as nx
#Grafo Chile"

G=nx.DiGraph(Equipo="Chile")  #creacion de grafo

G.clear()
#Nodos con nombre
G.add_node(0, name='C. BRAVO')
G.add_node(1, name='E. MENA')
G.add_node(2, name='M. ISLA')
G.add_node(3, name='F. SILVA')
G.add_node(4, name='A. SANCHEZ')
G.add_node(5, name='E. VARGAS')
G.add_node(6, name='F. GUTIERREZ')
G.add_node(7, name='G. MEDEL')
G.add_node(8, name='G. JARA')
G.add_node(9, name='C. ARANGUIZ')
G.add_node(10, name='M. DIAZ')

#MDP- Matriz de Pases
MDP=(
[0,	0,	3,	3,	0,	0,	1,	19,	5,	0,	1],
[0,	0,	0,	1,	1,	3,	1,	0,	11,	4,	1],
[2,	0,	0,	7,	18,	0,	2,	8,	0,	2,	3],
[2,	1,	8,	0,	9,	1,	3,	20,	4,	6,	3],
[0,	3,	7,	4,	0,	2,	1,	1,	4,	1,	1],
[0,	1,	1,	1,	0,	0,	0,	0,	0,	2,	1],
[0,	3,	0,	2,	2,	0,	0,	5,	3,	3,	1],
[7,	4,	8,	34,	9,	2,	3,	0,	13,	10,	14],
[2,	9,	2,	0,	3,	1,	1,	21,	0,	6,	6],
[0,	3,	5,	3,	4,	3,	3,	7,	1,	0,	4],
[0,	3,	6,	5,	2,	1,	2,	10,	6,	4,	0]
)

#empieza el rango desde cero ya que tiene que coincidir con el valor de la matriz
for x in range (0,11):
    for y in range (0,11):
      G.add_weighted_edges_from([(x,y,MDP[x][y])])  #Creador de enlaces con peso
      if MDP[x][y] == 0:
          G.remove_edge(x, y)          #elimina los enlaces que no existen, es decir, con peso = 0 o numero de pases = 0
      else:
          pass

#DATOS EN GEXF PARA GePHI
nx.write_gexf(G,'CHIvsHOL_J3.gexf')