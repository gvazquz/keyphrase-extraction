# G.M. Vazquez-Sanchez - 05/07/2015 - UoE MSc Artificial Intelligence - Dissertation
# This code computes the Degree, Betweenness and Closeness of each NP (noun phrase) in the collection of papers
# It uses the networkx library to compute Degree, Betweenness and Closeness
# The output are documents where NPs are sorted from higher to lower according to: 
# Degree value, Betweenness value and Closeness value

import networkx as nx  # @UnresolvedImport
import operator

def get_graph(f_name): 
    """Gets the file of the undirected graph."""
    f = open(f_name,'r')
    graph = f.readlines()
    graph = map(str.strip,graph)
    f.close()
    return graph

def get_nodes_and_edges(graph):
    """Divides the nodes and the edges to build the graph."""
    nodes = []
    edges = []
    for i in range (0,len(graph)-1,3):
        nodes.append(graph[i])
        nodes.append(graph[i+1])
        edges.append((graph[i],graph[i+1],float(graph[i+2])))
    nodes = list(set(nodes))  
    return nodes,edges

def compute_centrality_measures(G):
    """Uses networkx library to compute three centrality measures."""
    # Compute Degree
    degree = nx.degree_centrality(G).items()
    degree.sort(key=operator.itemgetter(1), reverse =True)
    # Compute Betweenness
    betweenness = nx.betweenness_centrality(G).items()
    betweenness.sort(key=operator.itemgetter(1), reverse =True)
    # Compute Closeness
    closeness = nx.closeness_centrality(G).items()
    closeness.sort(key=operator.itemgetter(1), reverse =True)
    return degree,betweenness,closeness

def save_ranking(c_measure,f_name,value):
    f = open(f_name,'w')
    for element in c_measure:
        if value:
            f.write(str(element[1]) + " " + element[0] + "\n")
        else:
            f.write(element[0] + "\n")
    f.close()
    
for f_num in range (1,2305):
    graph = get_graph("graphs/undirected/%d.txt" % f_num)
    nodes,edges = get_nodes_and_edges(graph)
    #Create undirected graph
    G=nx.Graph()
    G.add_nodes_from(nodes)
    G.add_weighted_edges_from(edges)
    degree,betweenness,closeness = compute_centrality_measures(G)
    save_ranking(degree,"results/degree/with_degree_values/%d.txt" % f_num,True)
    save_ranking(degree,"results/degree/just_keywords/%d.txt" % f_num,False)
    print "Degree-Document No. %d is finished" % f_num
    save_ranking(betweenness,"results/betweenness/with_betweenness_values/%d.txt" % f_num,True)
    save_ranking(betweenness,"results/betweenness/just_keywords/%d.txt" % f_num,False)
    print "Betweenness-Document No. %d is finished" % f_num
    save_ranking(closeness,"results/closeness/with_closeness_values/%d.txt" % f_num,True)
    save_ranking(closeness,"results/closeness/just_keywords/%d.txt" % f_num,False)
    print "Closeness-Document No. %d is finished" % f_num