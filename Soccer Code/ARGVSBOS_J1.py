import networkx as nx
#Grafo Argentino

DG=nx.DiGraph(Equipo="Argentina")

DG.clear()
#Nodos con nombre
DG.add_node(0, Label='S. ROMERO')
DG.add_node(1, Label='E. GARAY')
DG.add_node(2, Label='H. CAMPAGNARO')
DG.add_node(3, Label='P. ZABALETA')
DG.add_node(4, Label='A. DI MARIA')
DG.add_node(5, Label='L. MESSI')
DG.add_node(6, Label='F. GAGO') # SE TOMO EN CUENTA DEBIDO A QUE TUVO MAYOR PARTICIPACION EN MINUTOS DURANTE EL JUEGO
DG.add_node(7, Label='J. MASCHERANO')
DG.add_node(8, Label='M. ROJO')
DG.add_node(9, Label='F. FERNANDEZ')
DG.add_node(10, Label='S. AGUERO')

MDP=(
[0,	7,	2,	0,	0,	0,	0,	4,	1,	7,	1],
[1,	0,	3,	1,	12,	2,	2,	11,	5,	16,	1],
[0,	3,	0,	8,	1,	2,	0,	7,	0,	7,	1],
[0,	0,	6,	0,	0,	6,	9,	2,	0,	3,	3],
[0,	3,	1,	1,	0,	14,	5,	16,	7,	1,	3],
[0,	2,	2,	4,	6,	0,	7,	15,	2,	1,	3],
[0,	1,	0,	5,	7,	14,	0,	7,	1,	1,	2],
[1,	13,	3,	6,	22,	16,	7,	0,	7,	8,	3],
[2,	4,	0,	2,	10,	2,	0,	4,	0,	0,	2],
[2,	11,	5,	3,	3,	3,	5,	14,	1,	0,	2],
[0,	1,	0,	0,	2,	2,	1,	1,	1,	0,	0]
)
#empieza el rango desde cero ya que tiene que coincidir con el valor de la matriz

for x in range (0,11):
    for y in range (0,11):
      DG.add_weighted_edges_from([(x,y,MDP[x][y])])
#quito los enlaces que no exisiten (nunca dieron pase entre si)
      if MDP[x][y] == 0:
          DG.remove_edge(x, y)
      else:
          pass

nx.write_gexf(DG, "ARGvsBOS_J1.gexf")
