import numpy as np
import networkx as nx
from pyvis.network import Network

#============================================================
def GenerateMatrix():
    n_nodes=int(input("-Number of Nodes: "))
    print('\n-Build the Adjacency Matrix Row by Row: ')
    adjacencyMatrix=np.zeros((n_nodes,n_nodes))
    for i in range(0,n_nodes):
        print('\n-',i+1,'row: ')
        adjacencyMatrix[i]=list(map(int, input().split()))
    print(adjacencyMatrix)
    return adjacencyMatrix
#============================================================


#============================================================
def CanonicalNetwork(n_nodes=100,link_prob=0.1):
#Adjacency Matrix Generation
    adjacencyMatrix=np.zeros((n_nodes,n_nodes))
    for i in range(0,n_nodes):
        for j in range(0,n_nodes):
            if np.random.default_rng().random() <= link_prob:
               adjacencyMatrix[i,j]=1
            else: adjacencyMatrix[i,j]=0
    return adjacencyMatrix
#============================================================


#============================================================
def RandomNetwork(n_nodes=100):
#Adjacency Matrix Generation
    adjacencyMatrix = np.random.rand(n_nodes,n_nodes)
    for i in range(0,n_nodes):
        for j in range(0,n_nodes):
            adjacencyMatrix[i,j]=np.round(adjacencyMatrix[i,j])
    return adjacencyMatrix
#============================================================


#============================================================
def NetworkVisualization(adjacencyMatrix,Directed=True,nodeSize=7,
                         px_X='1000',px_Y='600'):
#Network visualization using NetworkX and Pyvis
    if Directed == True:
        NX_Network=nx.DiGraph(adjacencyMatrix)
        pyvis_net=Network(notebook=True,directed=True,height=px_Y+'px', 
                          width=px_X+'px')
        pyvis_net.from_nx(NX_Network,default_node_size=nodeSize)
        pyvis_net.hrepulsion(node_distance=300)
        pyvis_net.show_buttons()
        pyvis_net.show("NetworkPlot.html")
    else:
        NX_Network=nx.Graph(adjacencyMatrix)
        pyvis_net=Network(notebook=True,directed=False,height=px_Y, 
                          width=px_X)
        pyvis_net.from_nx(NX_Network,default_node_size=nodeSize)
        pyvis_net.hrepulsion(node_distance=300)
        pyvis_net.show_buttons()
        pyvis_net.show("NetworkPlot.html")
#============================================================
GenerateMatrix()
