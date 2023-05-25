# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 19:39:05 2015

@author: serch
"""

import networkx as nx
#Grafo Aleman"
DG=nx.MultiDiGraph(Equipo="Alemania")

#Nodos con nombre
DG.add_node(1, nom='Neuer')
DG.add_node(2, nom='Hoewedes')
DG.add_node(3, nom='Hummels')
DG.add_node(4, nom='Schweinsteiger')
DG.add_node(5, nom='Oezil')
DG.add_node(6, nom='Klose')
DG.add_node(7, nom='Muller')
DG.add_node(8, nom='Lahm')
DG.add_node(9, nom='Kroos')
DG.add_node(10, nom='Boateng')
DG.add_node(11, nom='Schuerrle') #se agrego a Schuerrle en lugar de Krammer 
#por que tuvo mayor tiempo de participacion en el partido

#matriz de enlace o pase
MP=([0,1,1,1,1,0,1,1,1,1,1],[1,0,1,1,1,1,1,0,1,1,1],[1,1,0,1,1,1,1,1,1,1,0],[1,1,1,0,1,1,1,1,1,1,1],[0,1,1,0,1,1,1,1,1,1,1],[0,0,0,0,1,0,1,1,1,1,0],[0,1,0,1,1,1,0,1,1,1,1],[1,0,1,1,1,1,1,0,1,1,1],[0,1,1,1,1,1,1,1,0,1,1],[1,1,1,1,1,0,1,1,1,0,1],[0,1,1,1,1,0,1,1,1,1,0])

#Enlaces de peso del enlace o numero de pases
MDP=([0,0.07,0.04,0.04,0.03,0,0.03,0.11,0.03,0.05,0.03],[0.02,0,0.08,0.06,0.03,0.01,0.02,0,0.13,0.02,0.18],[0.06,0.09,0,0.07,0.02,0.02,0.03,0.07,0.09,0.11,0],[0.04,0.09,0.08,0,0.13,0.01,0.08,0.15,0.23,0.09,0.07],[0,0.03,0,0.16,0,0.01,0.06,0.13,0.15,0.05,0.03],[0,0,0,0,0.01,00.06,0.02,0.01,0.02,0,0],[0,0.01,0,0.03,0.07,0.02,0,0.16,0.09,0.03,0.03],[0.01,0,0.02,0.23,0.24,0.06,0.12,0,0.07,0.23,0.01],[0,0.12,0.08,0.17,0.10,0.01,0.08,0.11,0,0.03,0.19],[0.09,0.03,0.10,0.13,0.08,0,0.05,0.22,0.06,0,0.01],[0,0.07,0.04,0.03,0.07,0,0.05,0.03,0.17,0.01,0])

for x in range (0,11):
    for y in range (0,11):
        
        if MP[x][y] == 1:
            DG.add_weighted_edges_from([(x,y,1)])
        else:
            print " "

for x in range (0,11):
    for y in range (0,11):
        DG[x][y]['weight'] = MDP[x][y]            

nx.draw(DG, 'Alemania Pesada.jpeg')        
print DG.edges(data=True)