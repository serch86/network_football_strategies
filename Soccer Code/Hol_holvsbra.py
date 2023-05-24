# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 20:04:14 2015

@author: serch
"""

import networkx as nx
#Grafo Holandes"

DG=nx.DiGraph(Equipo="Holanda")

DG.clear()

#Nodos con nombre
DG.add_node(0, Label='Cillessen')
DG.add_node(1, Label='Vlaar')
DG.add_node(2, Label='De Vrij')
DG.add_node(3, Label='Martins Indi')
DG.add_node(4, Label='Blind')
DG.add_node(5, Label='De Guzman')
DG.add_node(6, Label='Van Persie')
DG.add_node(7, Label='Robben')
DG.add_node(8, Label='Kuyt')
DG.add_node(9, Label='CLasie')
DG.add_node(10, Label='Wijnaldum') 


MDP=([0,2,0,4,1,1,1,2,4,2,0],[1,0,3,6,4,1,1,1,2,1,2],[4,4,0,1,0,2,0,3,6,1,4],[6,1,0,0,9,1,1,2,3,5,2],[1,2,1,8,0,4,4,7,0,1,0],[0,2,1,2,3,0,5,10,2,2,1],[0,0,0,1,0,2,0,3,3,2,2],[0,1,4,1,3,6,2,0,6,2,7],[2,1,7,1,0,3,2,4,0,4,4],[0,1,1,4,2,6,4,2,2,0,7],[0,3,3,1,0,4,4,7,6,5,0])

#empieza el rango desde cero ya que tiene que coincidir con el valor de la matriz

for x in range (0,11):
    for y in range (0,11):
      DG.add_weighted_edges_from([(x,y,MDP[x][y])])  

#quito los enlaces que no exisiten (nunca dieron pase entre si)    
      if MDP[x][y] == 0:            DG.remove_edge(x, y)
      else:
          pass

nx.write_gexf(DG, "HolandaP.gexf")


G=nx.Graph(Equipo="Holanda Sin Peso")  #creacion de grafo
#Nodos con nombre

G.add_node(0, Label='Cillessen')
G.add_node(1, Label='Vlaar')
G.add_node(2, Label='De Vrij')
G.add_node(3, Label='Martins Indi')
G.add_node(4, Label='Blind')
G.add_node(5, Label='De Guzman')
G.add_node(6, Label='Van Persie')
G.add_node(7, Label='Robben')
G.add_node(8, Label='Kuyt')
G.add_node(9, Label='CLasie')
G.add_node(10, Label='Wijnaldum') 

for x in range (0,11):
    for y in range (0,11):
      if MDP[x][y] == 0:    
          pass
      else:
          G.add_edges_from([(x,y)])  #Creador de enlaces con peso
      
nx.write_gexf(G,'HolandaSP.gexf')