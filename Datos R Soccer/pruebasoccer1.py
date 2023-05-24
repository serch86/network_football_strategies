# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este archivo temporal se encuentra aquí:
/home/serch/.spyder2/.temp.py
"""
import networkx as nx
import matplotlib.pyplot as plt



G=nx.Graph()
G.add_nodes_from([1,2,3,4,5,6,7,8,9,10,11])
G.add_edges_from([(1,2,{'weight':4}), (1,3,{'weight':1})])

nx.draw(G)
