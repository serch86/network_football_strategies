import networkx as nx

DG=nx.DiGraph(Equipo="Argentina")

DG.clear()
#Nodos con nombre
DG.add_node(0, Label='S. ROMERO')
DG.add_node(1, Label='E. GARAY')
DG.add_node(2, Label='P. ZABALETA')
DG.add_node(3, Label='L. BIGLIA')
DG.add_node(4, Label='E. PEREZ')
DG.add_node(5, Label='G. HIGUAIN')
DG.add_node(6, Label='L. MESSI')
DG.add_node(7, Label='J. MASCHERANO')
DG.add_node(8, Label='M. DEMICHELIS')
DG.add_node(9, Label='M. ROJO')
DG.add_node(10, Label='E. LAVEZZI')

MDP=(
[0,	3,	0,	0,	0,	1,	0,	8,	8,	1,	0],
[3,	0,	2,	10,	3,	0,	1,	23,	6,	8,	0],
[2,	0,	0,	9,	8,	5,	6,	4,	11,	0,	5],
[2,	10,	9,	0,	1,	3,	10,	3,	7,	5,	2],
[1,	3,	10,	5,	0,	2,	6,	5,	3,	4,	1],
[0,	1,	0,	1,	6,	0,	2,	0,	1,	2,	2],
[0,	1,	2,	6,	8,	2,	0,	4,	1,	5,	2],
[2,	16,	14,	3,	6,	1,	5,	0,	17,	4,	2],
[3,	5,	13,	9,	11,	0,	5,	18,	0,	2,	0],
[1,	11,	0,	2,	5,	3,	1,	5,	0,	0,	10],
[0,	2,	2,	2,	0,	0,	2,	3,	0,	5,	0]
)

for x in range (0,11):
    for y in range (0,11):
      DG.add_weighted_edges_from([(x,y,MDP[x][y])])
#quito los enlaces que no exisiten (nunca dieron pase entre si)
      if MDP[x][y] == 0:
          DG.remove_edge(x, y)
      else:
          pass

nx.write_gexf(DG, "ARG_HOL_SEMI.gexf")