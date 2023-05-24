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
G.add_node(5, name='A. VIDAL')
G.add_node(6, name='E. VARGAS')
G.add_node(7, name='G. MEDEL')
G.add_node(8, name='G. JARA')
G.add_node(9, name='C. ARANGUIZ')
G.add_node(10, name='M. DIAZ')

#MDP- Matriz de Pases
MDP=(
[0,	1,	1,	4,	2,	2,	1,	4,	6,	0,	0],
[0,	0,	0,	1,	2,	7,	6,	1,	9,	3,	1],
[2,	1,	0,	4,	14,	7,	0,	1,	1,	1,	5],
[5,	0,	8,	0,	5,	1,	3,	4,	2,	1,	4],
[0,	2,	4,	2,	0,	6,	1,	1,	2,	1,	0],
[0,	3,	6,	0,	6,	0,	5,	2,	4,	1,	4],
[0,	4,	0,	1,	3,	2,	0,	1,	5,	1,	2],
[8,	2,	1,	8,	1,	2,	1,	0,	4,	1,	3],
[5,	4,	4,	4,	1,	4,	3,	6,	0,	1,	9],
[0,	1,	0,	3,	1,	0,	2,	0,	1,	0,	3],
[3,	3,	3,	4,	1,	3,	1,	4,	5,	2,	0]
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
nx.write_gexf(G,'CHIvsESP_J2.gexf')