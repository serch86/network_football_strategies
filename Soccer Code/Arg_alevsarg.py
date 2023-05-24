# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 10:39:20 2015

@author: serch
"""

import networkx as nx
#Grafo Argentino

DG=nx.DiGraph(Equipo="Argentina")

DG.clear()
#Nodos con nombre
DG.add_node(0, Label='Romero')
DG.add_node(1, Label='Garay')
DG.add_node(2, Label='Zabaleta')
DG.add_node(3, Label='Biglia')
DG.add_node(4, Label='Perez')
DG.add_node(5, Label='Higuain')
DG.add_node(6, Label='Messi')
DG.add_node(7, Label='Mascherano')
DG.add_node(8, Label='Demichelis')
DG.add_node(9, Label='Rojo')
DG.add_node(10, Label='Aguero') #se agrego a Aguero en lugar de Lavezzi 
#por que tuvo mayor tiempo de participacion en el partido

MDP=([0,0,1,1,2,0,1,3,5,5,2],[3,0,0,3,3,0,2,7,8,13,2],[2,1,0,3,4,5,8,2,10,0,5],[2,7,3,0,2,1,10,7,1,3,5],[0,1,3,2,0,3,2,9,3,3,0],[0,0,1,1,7,0,0,3,0,0,1],[0,2,4,4,2,1,0,4,0,0,5],[3,6,4,8,6,0,5,0,9,7,4],[3,8,6,4,5,0,3,6,0,1,1],[0,6,0,12,3,3,3,9,0,0,2],[0,0,1,2,0,3,3,3,0,1,0])
#empieza el rango desde cero ya que tiene que coincidir con el valor de la matriz

for x in range (0,11):
    for y in range (0,11):
      DG.add_weighted_edges_from([(x,y,MDP[x][y])])  
#quito los enlaces que no exisiten (nunca dieron pase entre si)    
      if MDP[x][y] == 0:    
          DG.remove_edge(x, y)
      else:
          pass

nx.write_gexf(DG, "ARG_ALE_FINAL.gexf")

'''
G=nx.Graph(Equipo="Argenitna Sin Peso")  #creacion de grafo
#Nodos con nombre

G.add_node(0, Label='Romero')
G.add_node(1, Label='Garay')
G.add_node(2, Label='Zabaleta')
G.add_node(3, Label='Biglia')
G.add_node(4, Label='Perez')
G.add_node(5, Label='Higuain')
G.add_node(6, Label='Messi')
G.add_node(7, Label='Mascherano')
G.add_node(8, Label='Demichelis')
G.add_node(9, Label='Rojo')
G.add_node(10, Label='Aguero') #se agrego a Aguero en lugar de Lavezzi 
#por que tuvo mayor tiempo de participacion en el partido

for x in range (0,11):
    for y in range (0,11):
      if MDP[x][y] == 0: 
          pass
      else:
          G.add_edges_from([(x,y)])  #Creador de enlaces con peso

nx.write_gexf(G,'ArgentinaSP.gexf')
'''
