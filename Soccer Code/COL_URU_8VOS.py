#DATOS SE OBTUVIERON DE LA PAGINA DE FIFA--> MUNDIALES---->ESTADISTICAS---> PARTIDO (QUE SE QUIERA ANALIZAR)---->ESTADISTICAS HASTA ABAJO DE LA PAGINA

Colombia vs Uruguay
COL
MDP = ([0,5,3,2,1,1,0,0,0,1,9],[1,0,10,0,1,3,1,4,2,14,4],[2,9,0,4,7,3,2,1,2,1,0],[1,3,3,0,3,4,2,0,2,5],[2,1,1,3,0,8,2,11,9,1,5],[0,4,1,4,6,0,3,12,8,8,2],[0,0,1,1,0,3,0,2,2,2,4],[0,1,4,,1,5,7,1,0,3,4,2],[1,1,2,3,5,7,4,0,0,6,0],[1,6,0,3,0,7,1,4,8,0,3],[0,0,0,0,4,1,3,4,1,0,0])
URU
MDP = ([0,1,4,2,0,3,0,0,1,1,1],[0,0,0,4,0,5,2,1,1,1,13],[0,0,0,6,2,0,0,0,0,4,5],[0,0,5,0,3,0,2,1,0,3,5],[0,0,1,1,0,1,2,2,2,5,0],[0,4,0,0,3,0,7,1,2,2,2],[1,1,2,1,2,5,0,4,4,1,0],[0,4,1,5,1,2,7,0,2,4,4],[1,1,2,4,2,1,7,1,0,1,1],[0,1,0,4,2,1,1,3,2,0,7],[4,7,3,5,3,3,2,6,3,10,0])



import networkx as nx
#GrafoCHILE"

G=nx.DiGraph(Equipo="CHILE")  #creacion de grafo

G.clear()
#Nodos con nombre
G.add_nodes(0, name='C. Bravo')
G.add_nodes(1, name='E. Mena')
G.add_nodes(2, name='M. Isla')
G.add_nodes(3, name='F. Silva')
G.add_nodes(4, name='A. Sanchez')
G.add_nodes(5, name='A. Vidal')
G.add_nodes(6, name='F. Guitierrez')
G.add_nodes(7, name='G. Medel')
G.add_nodes(8, name='G. Jara')
G.add_nodes(9, name='C. Aranguiz')
G.add_nodes(10, name='M. DIAZ')


#MDP- Matriz de Pases
MDP=([0,1,0,0,2,3,0,8,1,0,0],[0,0,1,1,6,7,1,0,7,0,4],[1,0,0,12,6,7,3,3,0,10,6],[3,1,7,0,3,1,0,16,2,2,6],[0,2,3,0,0,2,2,1,2,3,6],[0,4,6,1,10,0,0,2,0,4,2],[0,3,2,1,3,1,0,2,2,1,1],[5,0,4,11,6,4,1,0,19,5,9],[6,4,3,2,5,3,3,7,0,6,6],[1,2,6,3,2,3,0,3,2,0,5],[2,4,8,6,4,7,3,9,3,2,0])

#empieza el rango desde cero ya que tiene que coincidir con el valor de la matriz
for x in range (0,11):
    for y in range (0,11):
      G.add_weighted_edges_from([(x,y,MDP[x][y])])  #Creador de enlaces con peso
      if MDP[x][y] == 0:
          G.remove_edge(x, y)          #elimina los enlaces que no existen, es decir, con peso = 0 o numero de pases = 0
      else:
          pass

#DATOS EN GEXF PARA GePHI
nx.write_gexf(G,'CHI_CHIvsBRA_8VOS.gexf')

#Grafo BRAZIL"

G=nx.DiGraph(Equipo="BRAZIL")  #creacion de grafo

G.clear() #borrar grafo anterior

#Nodos con nombre
G.add_node(0, Label='J.Cesar')
G.add_node(1, Label='D. Alves')
G.add_node(2, Label='T. Silva')
G.add_node(3, Label='D. Luiz')
G.add_node(4, Label='FERNANDINHO')
G.add_node(5, Label='Marcelo')
G.add_node(6, Label='Hulk')
G.add_node(7, Label='Fred')
G.add_node(8, Label='Neymar')
G.add_node(9, Label='Oscar')
G.add_node(10, Label='L. Gustavo')

#MDP- Matriz de Pases
MDP=([0,3,2,3,1,4,0,4,1,1,3],[0,0,5,3,4,0,10,3,4,15,11],[4,10,0,7,1,7,0,0,1,2,3],[6,5,5,0,1,5,0,0,1,0,7],[0,4,2,1,0,1,3,0,2,0,1],[0,1,1,7,1,0,10,0,17,7,11],[0,9,0,1,0,5,0,0,3,1,1],[0,2,0,0,1,1,0,0,3,0,0],[0,2,3,2,11,4,3,1,0,1,1],[0,5,2,0,1,2,0,4,6,0,1],[3,4,5,10,3,13,11,0,1,1,0])

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