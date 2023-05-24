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
DG.add_node(9, Label='E. LAVEZZI')
DG.add_node(10, Label='J. BASANTA')

MDP=(
[0,	5,	2,	1,	0,	2,	0,	3,	5,	0,	1],
[5,	0,	1,	1,	0,	1,	0,	5,	3,	4,	6],
[1,	2,	0,	4,	1,	7,	1,	2,	4,	0,	0],
[1,	4,	6,	0,	2,	0,	2,	7,	4,	2,	2],
[0,	0,	3,	3,	0,	4,	2,	2,	2,	0,	1],
[0,	1,	2,	4,	3,	0,	3,	4,	0,	2,	0],
[0,	1,	2,	6,	1,	2,	0,	2,	0,	6,	1],
[1,	2,	1,	3,	4,	4,	8,	0,	7,	5,	4],
[4,	0,	5,	6,	2,	6,	3,	5,	0,	0,	3],
[0,	0,	0,	2,	0,	1,	5,	7,	0,	0,	5],
[1,	6,	0,	2,	0,	2,	1,	5,	0,	11,	0]
)

for x in range (0,11):
    for y in range (0,11):
      DG.add_weighted_edges_from([(x,y,MDP[x][y])])
#quito los enlaces que no exisiten (nunca dieron pase entre si)
      if MDP[x][y] == 0:
          DG.remove_edge(x, y)
      else:
          pass

nx.write_gexf(DG, "ARG_BEL_4TOS.gexf")