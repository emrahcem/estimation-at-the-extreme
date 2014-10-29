def random_walk(graph, start_node=None, sample_size=-1, metropolized=False):    
    """
    random_walk(G, start_node=None, sample_size=-1):
    
    Generates nodes sampled by a random walk (classic or metropolized)
    
    Parameters
    ----------  
    graph:        - networkx.Graph 
    start_node    - starting node (if None, then chosen uniformly at random)
    sample_size          - desired sample length (int). If -1 (default), then the generator never stops
    metropolized  - False (default): classic Random Walk
                    True:  Metropolis Hastings Random Walk (with the uniform target node distribution) 
    """
            
    if start_node==None:
        start_node = random.choice(graph.nodes())

    v = start_node
    for c in itertools.count():
        
        if c>=sample_size:  return
        if metropolized:   # Metropolis Hastings Random Walk (with the uniform target node distribution) 
            candidate = random.choice(graph.neighbors(v))
            v = candidate if (random.random() < float(graph.degree(v))/graph.degree(candidate)) else v
        else:              # classic Random Walk
            v = random.choice(graph.neighbors(v))
        yield v