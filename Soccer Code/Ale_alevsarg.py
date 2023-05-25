# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 19:15:41 2015

@author: serch
"""

#DATOS SE OBTUVIERON DE LA PAGINA DE FIFA--> MUNDIALES---->ESTADISTICAS---> PARTIDO (QUE SE QUIERA ANALIZAR)---->ESTADISTICAS HASTA ABAJO DE LA PAGINA

import networkx as nx
#Grafo Aleman"

DG=nx.DiGraph(Equipo="Alemania")  #creacion de grafo

DG.clear() #borrar grafo anterior

#Nodos con nombre
DG.add_node(0, nom='Neuer')  #creado de nodos en eñl grafo DG
DG.add_node(1, nom='Hoewedes')
DG.add_node(2, nom='Hummels')
DG.add_node(3, nom='Schweinsteiger')
DG.add_node(4, nom='Oezil')
DG.add_node(5, nom='Klose')
DG.add_node(6, nom='Muller')
DG.add_node(7, nom='Lahm')
DG.add_node(8, nom='Kroos')
DG.add_node(9, nom='Boateng')
DG.add_node(10, nom='Schuerrle') #se agrego a Schuerrle en lugar de Krammer por que tuvo mayor tiempo de participacion en el partido

#MDP- Matriz de Pases
MDP=([0,7,4,4,3,0,3,11,3,5,3],[2,0,8,6,3,1,2,0,13,2,18],[6,9,0,7,2,2,3,7,9,11,0],[4,9,8,0,13,1,8,15,23,9,7],[0,3,0,16,0,1,6,13,15,5,3],[0,0,0,0,1,6,2,1,2,0,0],[0,1,0,3,7,2,0,16,9,3,3],[1,0,2,23,24,6,12,0,7,23,1],[0,12,8,17,10,1,8,11,0,3,19],[9,3,10,13,8,0,5,22,6,0,1],[0,7,4,3,7,0,5,3,17,1,0])

#empieza el rango desde cero ya que tiene que coincidir con el valor de la matriz
for x in range (0,11):
    for y in range (0,11):
      DG.add_weighted_edges_from([(x,y,MDP[x][y])])  #Creador de enlaces con peso
      if MDP[x][y] == 0:    
          DG.remove_edge(x, y)          #elimina los enlaces que no existen, es decir, con peso = 0 o numero de pases = 0
      else:
          pass

#DATOS EN GEXF PARA GePHI
nx.write_gexf(DG,'AlemaniaP.gexf')



G=nx.Graph(Equipo="Alemania Sin Peso")  #creacion de grafo

#Nodos con nombre
G.add_node(0, nom='Neuer')  #creado de nodos en el grafo G
G.add_node(1, nom='Hoewedes')
G.add_node(2, nom='Hummels')
G.add_node(3, nom='Schweinsteiger')
G.add_node(4, nom='Oezil')
G.add_node(5, nom='Klose')
G.add_node(6, nom='Muller')
G.add_node(7, nom='Lahm')
G.add_node(8, nom='Kroos')
G.add_node(9, nom='Boateng')
G.add_node(10, nom='Schuerrle') #se agrego a Schuerrle en lugar de Krammer por que tuvo mayor tiempo de participacion en el partido

for x in range (0,11):
    for y in range (0,11):
      if MDP[x][y] == 0: 
          pass
      else:
          G.add_edges_from([(x,y)])  #Creador de enlaces con peso
      
nx.write_gexf(G,'AlemaniaSP.gexf')