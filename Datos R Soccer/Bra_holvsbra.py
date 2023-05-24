# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 12:08:26 2015

@author: serch
"""

import networkx as nx
#Grafo Brasileño

DG=nx.DiGraph(Equipo="Brasil")

DG.clear()
#Nodos con nombre
DG.add_node(0, Label='Julio Cesar')
DG.add_node(1, Label='Silva')
DG.add_node(2, Label='David Luiz')
DG.add_node(3, Label='Paulinho')
DG.add_node(4, Label='Oscar')
DG.add_node(5, Label='Maxwell')
DG.add_node(6, Label='Ramires')
DG.add_node(7, Label='Fernandinho') #se cambio Luiz Gustavo por Fernandinho por tiempo de juego
DG.add_node(8, Label='Willian')
DG.add_node(9, Label='Jo')
DG.add_node(10, Label='Maicon') 

MDP=([0,4,7,0,4,1,0,2,0,1,0],[3,0,3,2,1,2,2,9,1,0,10],[0,6,0,4,8,6,4,9,5,2,3],[1,0,2,0,2,3,1,1,1,1,2],[0,1,3,2,0,6,3,3,15,5,9],[0,0,7,4,8,0,1,4,12,3,0],[0,4,4,0,1,0,0,1,2,0,2],[0,6,8,0,6,4,0,0,6,1,7],[1,3,5,5,14,4,4,6,0,1,8],[0,3,1,0,4,1,2,1,5,0,8],[0,5,2,1,12,1,5,6,8,16,0])

#empieza el rango desde cero ya que tiene que coincidir con el valor de la matriz

for x in range (0,11):
    for y in range (0,11):
      DG.add_weighted_edges_from([(x,y,MDP[x][y])])  

#quito los enlaces que no exisiten (nunca dieron pase entre si)    
      if MDP[x][y] == 0:            DG.remove_edge(x, y)
      else:
          pass

nx.write_gexf(DG, "BrasilP.gexf")

G=nx.Graph(Equipo="Brasil Sin Peso")  #creacion de grafo
#Nodos con nombre

G.add_node(0, Label='Julio Cesar')
G.add_node(1, Label='Silva')
G.add_node(2, Label='David Luiz')
G.add_node(3, Label='Paulinho')
G.add_node(4, Label='Oscar')
G.add_node(5, Label='Maxwell')
G.add_node(6, Label='Ramires')
G.add_node(7, Label='Fernandinho') #se cambio Luiz Gustavo por Fernandinho por tiempo de juego
G.add_node(8, Label='Willian')
G.add_node(9, Label='Jo')
G.add_node(10, Label='Maicon')

for x in range (0,11):
    for y in range (0,11):
      if MDP[x][y] == 0:    
          pass
      else:
          G.add_edges_from([(x,y)])  #Creador de enlaces con peso
      
nx.write_gexf(G,'BrasilSP.gexf')