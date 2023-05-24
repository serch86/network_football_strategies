# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 19:15:41 2015

@author: serch
"""
import matplotlib.pyplot as plt
import networkx as nx
#Grafo Aleman"


DG=nx.DiGraph(Equipo="Alemania")

DG.clear()
#Nodos con nombre
DG.add_node(0, nom='Neuer')
DG.add_node(1, nom='Hoewedes')
DG.add_node(2, nom='Hummels')
DG.add_node(3, nom='Schweinsteiger')
DG.add_node(4, nom='Oezil')
DG.add_node(5, nom='Klose')
DG.add_node(6, nom='Muller')
DG.add_node(7, nom='Lahm')
DG.add_node(8, nom='Kroos')
DG.add_node(9, nom='Boateng')
DG.add_node(10, nom='Schuerrle') #se agrego a schuerrle en lugar de krammer 
#por que tuvo mayor tiempo de participacion en el partido

MDP=([0,0.07,0.04,0.04,0.03,0,0.03,0.11,0.03,0.05,0.03],[0.02,0,0.08,0.06,0.03,0.01,0.02,0,0.13,0.02,0.18],[0.06,0.09,0,0.07,0.02,0.02,0.03,0.07,0.09,0.11,0],[0.04,0.09,0.08,0,0.13,0.01,0.08,0.15,0.23,0.09,0.07],[0,0.03,0,0.16,0,0.01,0.06,0.13,0.15,0.05,0.03],[0,0,0,0,0.01,00.06,0.02,0.01,0.02,0,0],[0,0.01,0,0.03,0.07,0.02,0,0.16,0.09,0.03,0.03],[0.01,0,0.02,0.23,0.24,0.06,0.12,0,0.07,0.23,0.01],[0,0.12,0.08,0.17,0.10,0.01,0.08,0.11,0,0.03,0.19],[0.09,0.03,0.10,0.13,0.08,0,0.05,0.22,0.06,0,0.01],[0,0.07,0.04,0.03,0.07,0,0.05,0.03,0.17,0.01,0])
#empiea el rango desde cero ya que tiene que coincidir con el valor de la matriz
for x in range (0,11):
    for y in range (0,11):
      DG.add_weighted_edges_from([(x,y,MDP[x][y])])  
      if MDP[x][y] == 0:
          DG.remove_edge(x, y)
      else:
          print " "    
      
nx.draw(DG,node_color='1',node_shape='8')
limits=plt.axis('on')
plt.draw()

print (nx.degree(DG))
print (nx.in_degree_centrality(DG))
print (nx.out_degree_centrality(DG))
print (nx.closeness_centrality(DG))
