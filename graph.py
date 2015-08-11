'''
Created on 12-Nov-2013

@author: raghavan
'''

class Graph(object):
    '''
    A graph with nodes and edges
    '''

    def __init__(self, comp_fn = None):
        '''
        Initialize the graph
        Comparison function is required for the sorting of components of the graph (see the comments
        for the get_connected_components method
        '''
        # Your code


    def is_node(self, node):
        '''
        Check if a given node is part of the graph
        '''
        # Your code


    def add_node(self, node):
        '''
        Add a new node to the graph without edges
        '''
        # Your code
        

    def add_directed_edge(self, node1, node2):
        '''
        Add a directed edge going from node1 to node2
        You may not be able to assume that node1 or node2 are already there in the adjacency list
        '''
        # Your code

            
    def add_edge(self, node1, node2):
        '''
        Add an undirected edge between node1 and node2
        This is the same as adding two directed edges
        '''
        # Your code
        
    
    def get_connected_components(self):
        '''
        Return a list of all the connected components (each connected component will be a sublist of the list that
        is returned). A connected component is just a list of nodes making up that component
        Algorithm:
        1. Keep a hash to assign component numbers to each node - if two nodes have the same component number
        then they belong to the same component.
        2. Walk through all the edges of the graph (for each key - every key is a node of the graph - of the adjacency 
        walk through all the nodes it is connected to - the list self.adacency[node] )
        3. For each edge see if the component numbers of the two endpoints are the same - otherwise, let 'label' be the min
        of two component numbers and let 'node' be the end point which does not have the component number 'label'.
        Make the component number of 'node' and all its neighbours as 'label' (this step is equivalent to merging the 
        two components).
        4. From this extract the list of components (list of lists of nodes with the same component number)
        5. Return the component list arranged as described below:
        The nodes in each component are to be sorted according to the comparison function
        The list returned must be sorted in the decreasing order of the sizes of the components
        '''
        # Your code