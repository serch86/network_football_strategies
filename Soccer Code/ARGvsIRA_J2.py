import networkx as nx
#Grafo Argentino

DG=nx.DiGraph(Equipo="Argentina")

DG.clear()
#Nodos con nombre
DG.add_node(0, Label='S. ROMERO')
DG.add_node(1, Label='E. GARAY')
DG.add_node(2, Label='P. ZABALETA')
DG.add_node(3, Label='F. GAGO')
DG.add_node(4, Label='A. DI MARIA')
DG.add_node(5, Label='G. HIGUAIN')
DG.add_node(6, Label='L. MESSI')
DG.add_node(7, Label='J. MASCHERANO')
DG.add_node(8, Label='M. ROJO')
DG.add_node(9, Label='F. FERNANDEZ')
DG.add_node(10, Label='S. AGUERO')

MDP=(
[0,	5,	0,	2,	0,	1,	1,	3,	2,	2,	0],
[0,	0,	1,	7,	1,	0,	0,	18,	3,	3,	0],
[2,	0,	0,	16,	0,	0,	10,	7,	0,	7,	3],
[0,	4,	18,	0,	6,	5,	22,	25,	8,	9,	5],
[0,	5,	0,	7,	0,	5,	5,	4,	8,	1,	2],
[0,	0,	1,	0,	4,	0,	3,	1,	0,	0,	1],
[0,	2,	7,	7,	6,	2,	0,	9,	2,	1,	1],
[0,	1,	8,	35,	18,	3,	8,	0,	17,	7,	5],
[0,	6,	0,	3,	15,	1,	1,	14,	0,	1,	5],
[4,	2,	3,	15,	1,	1,	0,	13,	0,	0,	0],
[0,	1,	0,	3,	4,	0,	2,	0,	2,	0,	0]
)

for x in range (0,11):
    for y in range (0,11):
      DG.add_weighted_edges_from([(x,y,MDP[x][y])])
#quito los enlaces que no exisiten (nunca dieron pase entre si)
      if MDP[x][y] == 0:
          DG.remove_edge(x, y)
      else:
          pass

nx.write_gexf(DG, "ARG_IRA_J2.gexf")

