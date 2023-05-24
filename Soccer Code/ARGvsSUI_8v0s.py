import networkx as nx

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
[0,	6,	1,	0,	1,	0,	0,	6,	1,	6,	0],
[1,	0,	0,	10,	3,	0,	0,	14,	17,	18,	3],
[1,	2,	0,	5,	17,	2,	5,	4,	1,	15,	8],
[0,	5,	17,	0,	15,	2,	13,	9,	3,	3,	3],
[0,	1,	4,	7,	0,	1,	12,	6,	7,	2,	1],
[0,	0,	2,	1,	5,	0,	4,	0,	1,	0,	1],
[0,	1,	1,	9,	12,	2,	0,	3,	3,	0,	5],
[0,	9,	6,	18,	9,	5,	9,	0,	12,	14,	1],
[0,	13,	0,	4,	12,	5,	4,	10,	0,	0,	8],
[5,	13,	11,	10,	3,	3,	0,	15,	2,	0,	3],
[0,	1,	2,	6,	0,	1,	2,	4,	5,	0,	0]
)

for x in range (0,11):
    for y in range (0,11):
      DG.add_weighted_edges_from([(x,y,MDP[x][y])])
#quito los enlaces que no exisiten (nunca dieron pase entre si)
      if MDP[x][y] == 0:
          DG.remove_edge(x, y)
      else:
          pass

nx.write_gexf(DG, "ARG_SUI_8VOS.gexf")

