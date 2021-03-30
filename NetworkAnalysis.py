import numpy as np
import networkx as nx
from pyvis.network import Network

#============================================================
def ManualMatrixGeneration():
    """
    Generates a squared array by inserting the elements in order
    row by row from the terminal.\n
    *- Suggestion: use this one to generate small networks, because
    every element must be entered by hand.*

    How To Use
    ----------
    >>> ManualMatrixGeneration()
    -Number of Nodes:
    >>> 3
    
    We generated a 3x3 empty matrix. The function is ready to
    receive 9 elements that must be given as 3 row vectors:
    
    >>> 
    -Build the Adjacency Matrix Row by Row:
    - 1 row: 
    >>> 1.1 2 7
    - 2 row: 
    >>> 0 0 0
    - 3 row: 
    >>> 26.3 1 0
    
    The result is a 3x3 array like this:
    
    >>>
    [[1.1,2,7],
     [0,0,0],
     [26.3,1,0]]
    
    Returns
    -------
    output : ndarray
        The output of the function is a squared numpy array.

    """
    n_nodes=int(input("-Number of Nodes: "))
    if n_nodes<0:
        raise ValueError("In the function ManualMatrixGeneration(), n_nodes must be a positive integer.")
    
    print('\n-Build the Adjacency Matrix Row by Row: ')
    adjacencyMatrix=np.zeros((n_nodes,n_nodes))
    for i in range(0,n_nodes):
        print('\n-',i+1,'row: ')
        row=list(map(int, input().split()))
        if len(row) != n_nodes:
            raise ValueError("The number of elements entered",len(row),
                                 "is different from the wanted network size",n_nodes)
        adjacencyMatrix[i]=row
        
    print(adjacencyMatrix)
    return adjacencyMatrix
#============================================================


#============================================================
def CanonicalNetwork(n_nodes=100,link_prob=0.1):
    """
    Generates a network with a fixed number of nodes where each
    link between the nodes has a fixed probability 'link_prob' to
    be generated.

    Parameters
    ----------
    n_nodes : int, optional
        Set the size of the network. 
        The default value is 100.
    link_prob : float, optional
        Set the link probability between two generic nodes 
        (also with the same node).
        The default value is '0.1'.

    Returns
    -------
    output : ndarray
        The output of the function is a squared numpy array with 
        only 0 and 1.
        
    Examples
    --------
    >>> CanonicalNetwork(n_nodes=4)
    [[0,0,0,1],
     [1,1,0,0],
     [0,0,0,0],
     [0,0,0,0]]
    
    
    """
    if not isinstance(n_nodes,(int)):
        raise TypeError("In the function CanonicalNetwork(), n_nodes must be a positive integer.")
    elif n_nodes<0:
        raise ValueError("In the function CanonicalNetwork(), n_nodes must be a positive integer.")
        
    if not isinstance(link_prob,(int,float)):
        raise TypeError("In the function CanonicalNetwork(), link_prob must be an integer or a float.")
    elif link_prob < 0:
        raise ValueError("In the function CanonicalNetwork(), link_prob must be grater than 0.")
    elif link_prob > 1:
        print("\n========== WARNING: Using a probability that is greater than 1 ==========\n")

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
    """
    This function generates a random adjacency matrix of a network with
    'n_nodes' nodes. The links between the nodes are random.

    Parameters
    ----------
    n_nodes : int, optional
        Set the number of nodes of the network. 
        The default value is 100.

    Returns
    -------
    output : ndarray
        The output of the function is a squared numpy array 
        with only 0 and 1.

    Examples
    --------
    >>> RandomNetwork(5)
    [[0,0,1,0,1],
     [1,1,1,0,0],
     [0,0,1,0,1],
     [1,0,0,1,0],
     [0,0,0,1,0]]
    
    """
    
    if not isinstance(n_nodes,(int)):
        raise TypeError("In the function RandomNetwork(), n_nodes must be a positive integer.")
    elif n_nodes<0:
        raise ValueError("In the function RandomNetwork(), n_nodes must be a positive integer.")
#Adjacency Matrix Generation
    adjacencyMatrix = np.random.rand(n_nodes,n_nodes)
    for i in range(0,n_nodes):
        for j in range(0,n_nodes):
            adjacencyMatrix[i,j]=np.round(adjacencyMatrix[i,j])
    return adjacencyMatrix
#============================================================


#============================================================
def NetworkVisualization(adjacencyMatrix,Directed=True,
                         px_X='900',px_Y='600',
                         network_name="NetworkPlot.html"):
    """
    This function generates an HTML file in which is plotted the
    network created.
    
    Parameters
    ----------
    adjacencyMatrix : ndarray
        Insert a squared NumPy array of real numbers.
    Directed : bool, optional
        Specifies if the Network has to be visualized as directed (True)
        or undirected (False). The default value is True.
    px_X : string, optional
        Set the number of pixels on the X-Axis; must be given as a string.
        The default value is '900'.
    px_Y : string, optional
        Set the number of pixels on the Y-Axis; must be given as a string.
        The default value is '600'.
    network_name : string, optional
        Set the name of the HTML file generated by the function.
        The default name is "NetworkPlot.html".
    
    Returns
    -------
    This function returns nothing, but it generates an HTML file inside the
    working directory.

    Examples
    --------
    >>> test_array=np.array([[0,1,1,1,1],[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0]])
    [[0,1,1,1,1],
     [1,0,0,0,0],
     [1,0,0,0,0],
     [1,0,0,0,0],
     [1,0,0,0,0]]
    >>> NetworkVisualization(test_array,network_name="New Network Plot!")
    
    >>> test_array=np.array([[0,1.3,0],[0,0,0.3],[4,0,0]])
    [[0,1.3,0],
     [0,0,0.3],
     [4,0,0.1]]
    >>> NetworkVisualization(test_array,Directed=False,px_X='600')
    
    >>> test_array=np.random.default_rng()
    >>> test_array.integers(2, size=(100, 100))
    random 100x100 array of zeros and ones
    >>> NetworkVisualization(test_array,px_X='1000',px_Y='1200')
    """
    node_number=adjacencyMatrix.shape[1]
    
    if Directed == True:
        NX_Network=nx.DiGraph(adjacencyMatrix)
        pyvis_net=Network(notebook=True,directed=True,height=px_Y+'px', 
                          width=px_X+'px')
        pyvis_net.from_nx(NX_Network,default_node_size=node_number)
        pyvis_net.hrepulsion(node_distance=300)
        pyvis_net.show_buttons()
        pyvis_net.show(network_name)
    else:
        NX_Network=nx.Graph(adjacencyMatrix)
        pyvis_net=Network(notebook=True,directed=False,height=px_Y, 
                          width=px_X)
        pyvis_net.from_nx(NX_Network,default_node_size=node_number)
        pyvis_net.hrepulsion(node_distance=300)
        pyvis_net.show_buttons()
        pyvis_net.show(network_name)
#============================================================

#TESTING

#CanonicalNetwork function
def test_Canonical1():
    """ Test if the sizes of a 0 array generated with 
    CanonicalNetwork is actually 0."""
    assert CanonicalNetwork(0).size == 0

def test_Canonical2():
    """ Test if the size of the array generated with 
    CanonicalNetwork is correct."""
    value=np.random.randint(0,100)
    assert CanonicalNetwork(value).size == value*value

def test_Canonical3():
    """ Test if the array generated with a '0' link probability 
    is actually an array full of zeros"""
    value=np.random.randint(0,100)
    assert np.array_equal(CanonicalNetwork(value,0),
                          np.zeros((value,value)))
    
def test_Canonical4():
    """ Test if the array generated with a '1' link probability 
    is actually an array with no zeros"""
    value=np.random.randint(0,100)
    assert CanonicalNetwork(value,1).all()
    
#RandomNetwork function
def test_Random1():
    """ Test if the size of the array generated with 
    RandomNetwork is correct."""
    value=np.random.randint(0,100)
    assert RandomNetwork(value).size == value*value

