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
DG.add_node(10, Label='E. LAVEZZI')

MDP=(
[0,	3,	1,	1,	1,	0,	0,	5,	0,	1, 0],
[2,	0,	3,	4,	7,	2,	1,	9,	9,	9, 0],
[0,	1,	0,	8,	1,	3,	2,	2,	0,	10, 3],
[0,	5,	8,	0,	7,	7,	7,	18,	1,	4, 10],
[0,	7,	3,	7,	0,	4,	4,	13,	12,	2, 7],
[0,	1,	0,	4,	9,	0,	2,	2,	1,	2, 2],
[0,	0,	0,	3,	7,	5,	0,	2,	1,	0, 3],
[0,	7,	5,	17,	16,	2,	7,	0,	10,	10, 4],
[0,	11,	0,	4,	18,	3,	1,	6,	0,	3, 2],
[1,	7,	4,	8,	4,	1,	1,	10,	2,	0, 3],
[0,	0,	2,	4,	6,	1,	3,	2,	2,	0, 0]
)

for x in range (0,11):
    for y in range (0,11):
      DG.add_weighted_edges_from([(x,y,MDP[x][y])])
#quito los enlaces que no exisiten (nunca dieron pase entre si)
      if MDP[x][y] == 0:
          DG.remove_edge(x, y)
      else:
          pass

nx.write_gexf(DG, "ARG_NIG_J3.gexf")