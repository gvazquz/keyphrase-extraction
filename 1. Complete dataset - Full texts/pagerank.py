# G.M. Vazquez-Sanchez - 04/07/2015 - UoE MSc Artificial Intelligence - Dissertation
# This code computes the Pagerank (PR) of each NP (noun phrase) in the collection of papers
# It uses the library networkx to compute PR values
# The output is a document where NPs are sorted from higher to lower PR value

import networkx as nx  # @UnresolvedImport
import numpy
import heapq

def get_graph(f_name): 
    """Gets the file of the directed graph."""
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

def sort(PR):
    """Sorts the keywords according to their PR values."""
    pagerank = numpy.array(PR.values())
    keywords = list(PR.keys())
    N = len(pagerank)
    i = heapq.nlargest(N, range(N), pagerank.__getitem__)
    return pagerank,keywords,i

def save_k_words(PR,f_name,value):
    pagerank,keywords,tops = sort(PR)
    f = open(f_name,'w')
    for top in tops:
        if value:
            f.write(str(pagerank[top]) + " " + keywords[top] + "\n")
        else:
            f.write(keywords[top] + "\n")
    f.close()
    
for f_num in range (1,2305):
    graph = get_graph("graphs/directed/%d.txt" % f_num)
    nodes,edges = get_nodes_and_edges(graph)
    #Create directed graph
    G=nx.DiGraph()
    G.add_nodes_from(nodes)
    G.add_weighted_edges_from(edges)
    # Compute pagerank
    pr = nx.pagerank(G)
    save_k_words(pr,"results/pagerank/with_pagerank_values/%d.txt" % f_num,True)
    save_k_words(pr,"results/pagerank/just_keywords/%d.txt" % f_num,False)
    print "PR-Document No. %d is finished" % f_num
