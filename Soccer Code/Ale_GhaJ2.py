# DATOS SE OBTUVIERON DE LA PAGINA DE FIFA--> MUNDIALES---->ESTADISTICAS---> PARTIDO (QUE SE QUIERA ANALIZAR)---->ESTADISTICAS HASTA ABAJO DE LA PAGINA

import networkx as nx
#Grafo ALEMANIA"

A=nx.DiGraph(Equipo="Alemania")  #creacion de grafo

A.clear() #borrar grafo anterior

#Nodos con nombre
A.add_node(0, nom='M NEUER')  #creado de nodos en el grafo A
A.add_node(1, nom='B. HOEWEDES')
A.add_node(2, nom='M. HUMMELS')
A.add_node(3, nom='S. KHEDIRA')
A.add_node(4, nom='M. OEZIL')
A.add_node(5, nom='T. MUELLER')
A.add_node(6, nom='P. LAHM')
A.add_node(7, nom='P. MERTESACKER')
A.add_node(8, nom='T. KROOS')
A.add_node(9, nom='M. GOETZE')
A.add_node(10, nom='J. BOATENG')

#MDP- Matriz de Pases
MDP=([0,    0,	11,	1,	0,	0,	5,	4,	3,	2,	1],[1,	0,	1,	3,	5,	6,	3,	0,	10,	4,	0],
     [7,	1,	0,	4,	2,	0,	8,	13,	22,	1,	2],
       [0,	1,	3,	0,	5,	4,	5,	5,	6,	7,	8],[0,	3,	1,	3,	0,	5,	5,	2,	6,	4,	0],
     [0,	2,	2,	3,	5,	0,	5,	0,	6,	3,	1],
       [2,	6,	9,	6,	7,	3,	0,	5,	21,	3,	2],[5,	1,	12,	9,	5,	2,	10,	0,	10,	1,	5],
     [0,	7,	5,	14,	14,	7,	16,	9,	0,	7,	1],
       [1,	0,	1,	3,	5,	4,	4,	1,	7,	0,	3],[1,	0,	1,	4,	3,	1,	2,	8,	0,	2,	0])

#empieza el rango desde cero ya que tiene que coincidir con el valor de la matriz
for x in range (0,11):
    for y in range (0,11):
      A.add_weighted_edges_from([(x,y,MDP[x][y])])  #Creador de enlaces con peso
      if MDP[x][y] == 0:
          A.remove_edge(x, y)          #elimina los enlaces que no existen, es decir, con peso = 0 o numero de pases = 0
      else:
          pass


#
# #Generacion de datos a analizar betweenness
# bet = nx.betweenness_centrality(A)
# #Acomodo de datos en forma de tabla y obtencion de resultados mayores y minimos para su analisis.
# val_b = bet.values()
# val_b_2 = []
# for i in range(0,len(val_b)-1):
#     val_b_2.append(val_b[i]/90)
#
# nx.set_node_attributes(A, 'betweenness', bet)
#
# #Generacion de datos a analizar closeness
# clos = nx.closeness_centrality(A)
# nx.set_node_attributes(A, 'closeness', clos)
# #Generacion de datos a analizar grado esto esta mal!!!!
# deg = nx.out_degree(A, weight=True)
# nx.set_node_attributes(A, 'degree', deg)
# print A.nodes(data=True), nx.info(A)

'''
M_1=nx.Graph(Equipo="Mexico Sin Peso")  #creacion de grafo
#Nodos con nombre

M_1.add_node(0, nom='G. Ochoa')  #creado de nodos en el grafo M
M_1.add_node(1, nom='F. Rodriguez')
M_1.add_node(2, nom='C. SALCIDO')
M_1.add_node(3, nom='R. Marquez')
M_1.add_node(4, nom='H. Herrera')
M_1.add_node(5, nom='M. Layun')
M_1.add_node(6, nom='G. Dos Santos')
M_1.add_node(7, nom='H. Moreno')
M_1.add_node(8, nom='A. Guardado')
M_1.add_node(9, nom='O. Peralta')
M_1.add_node(10, nom='P. Aguilar')

for x in range (0,11):
    for y in range (0,11):
      if MDPMx[x][y] == 0:
          pass
      else:
          M_1.add_weighted_edges_from([(x,y,MDPMx[x][y])]) #Creador de enlaces con peso
print nx.transitivity(M)
print nx.clustering(M_1)
'''
#DATOS EN GEXF PARA GePHI
nx.write_gexf(A,'ALEvsGHAJ2.gexf')

'''
#Grafo Holandes"

DG=nx.DiGraph(Equipo="Holanda")

DG.clear()

#Nodos con nombre
DG.add_node(0, Label='Cillessen')
DG.add_node(1, Label='Vlaar')
DG.add_node(2, Label='De Vrij')
DG.add_node(3, Label='D. BLIND')
DG.add_node(4, Label='Martins Indi')
DG.add_node(5, Label='Van Persie')
DG.add_node(6, Label='W. SNEIJDER')
DG.add_node(7, Label='A. Robben')
DG.add_node(8, Label='P. VERHAEGH')
DG.add_node(9, Label='D. Kuyt')
DG.add_node(10, Label='Wijnaldum')


MDP=([0,0,5,2,9,0,0,0,0,4,0],[0,0,7,8,10,0,3,2,2,6,1],[2,13,0,5,8,4,6,3,5,9,2],
     [2,4,8,0,9,2,6,3,7,10,6],[1,3,4,10,0,2,15,2,0,12,0],[0,0,1,1,0,0,4,1,2,2,2],
     [0,1,4,9,12,0,0,6,3,5,2],[0,1,4,4,0,4,4,0,2,5,2],[1,0,10,4,0,3,0,2,0,0,7],
     [0,4,1,4,5,1,13,8,3,0,10],[0,4,1,6,2,2,4,7,2,3,0])

#empieza el rango desde cero ya que tiene que coincidir con el valor de la matriz

for x in range (0,11):
    for y in range (0,11):
      DG.add_weighted_edges_from([(x,y,MDP[x][y])])

#quito los enlaces que no exisiten (nunca dieron pase entre si)
      if MDP[x][y] == 0:
          DG.remove_edge(x, y)
      else:
          pass
'''
# nx.write_gexf(DG, "HOL_MEXvsHOL.gexf")