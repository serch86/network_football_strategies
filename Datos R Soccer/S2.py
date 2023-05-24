# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 17:45:28 2015

@author: serch
"""

import networkx as nx
#Grafo Aleman"
DG=nx.MultiDiGraph(Equipo="Alemania")
"""print DG.graph"""
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
DG.add_node(11, nom='Schuerrle') #se agrego a schuerrle en lugar de krammer 
#por que tuvo mayor tiempo de participacion en el partido

#Matriz de peso (numero de pases)
MDP=([0,0.07,0.04,0.04,0.03,0,0.03,0.11,0.03,0.05,0.03],[0.02,0,0.08,0.06,0.03,0.01,0.02,0,0.13,0.02,0.18],[0.06,0.09,0,0.07,0.02,0.02,0.03,0.07,0.09,0.11,0],[0.04,0.09,0.08,0,0.13,0.01,0.08,0.15,0.23,0.09,0.07],[0,0.03,0,0.16,0,0.01,0.06,0.13,0.15,0.05,0.03],[0,0,0,0,0.01,00.06,0.02,0.01,0.02,0,0],[0,0.01,0,0.03,0.07,0.02,0,0.16,0.09,0.03,0.03],[0.01,0,0.02,0.23,0.24,0.06,0.12,0,0.07,0.23,0.01],[0,0.12,0.08,0.17,0.10,0.01,0.08,0.11,0,0.03,0.19],[0.09,0.03,0.10,0.13,0.08,0,0.05,0.22,0.06,0,0.01],[0,0.07,0.04,0.03,0.07,0,0.05,0.03,0.17,0.01,0])

#Enlaces de Neuer
#DG.add_weighted_edges_from([(1,2,0.07),(1,3,0.04),(1,4,0.04),(1,5,0.03),(1,7,0.03),(1,8,0.11),(1,9,0.03),(1,10,0.05),(1,11,0.02)])
#Enlaces de Hoewedes
#DG.add_weighted_edges_from([(2,1,MDP[1][0])])


nx.draw(DG)
