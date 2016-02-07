# G.M. Vazquez-Sanchez - 05/07/2015 - UoE MSc Artificial Intelligence - Dissertation
# This code computes the Strength of each NP (noun phrase) in the collection of papers
# The output is a document where NPs are sorted from higher to lower Strength value

import numpy
import heapq
from collections import defaultdict

def get_graph(f_name): 
    """Gets the file of the undirected graph."""
    f = open(f_name,'r')
    graph = f.readlines()
    graph = map(str.strip,graph)
    f.close()
    return graph

def get_strength(graph):
    """Gets the sum of weights of the edges incident to each node."""
    strength_dict = defaultdict()
    for i in range (0,len(graph),3):
        node_1 = graph[i]
        node_2 = graph[i+1]
        weight = float(graph[i+2])
        if node_1 in strength_dict:
            strength_dict[node_1] += weight
        else:
            strength_dict[node_1] = weight
        if node_2 in strength_dict:
            strength_dict[node_2] += weight
        else:
            strength_dict[node_2] = weight
    return strength_dict

def sort(strength_dict):
    """Sorts the keywords according to their Strength values."""
    strength = numpy.array(strength_dict.values())
    keywords = list(strength_dict.keys())
    tops = heapq.nlargest(len(strength), range(len(strength)), strength.__getitem__)
    return strength,keywords,tops

def save_k_words(strength_dict,f_name,value):
    strength,keywords,tops = sort(strength_dict)
    f = open(f_name,'w')
    for top in tops:
        if value:
            f.write(str(strength[top]) + " " + keywords[top] + "\n")
        else:
            f.write(keywords[top] + "\n")
    f.close()

for f_num in range (1,2305):
    graph = get_graph("graphs/undirected/%d.txt" % f_num)
    strength = get_strength(graph)
    save_k_words(strength,"results/strength/with_strength_values/%d.txt" % f_num,True)
    save_k_words(strength,"results/strength/just_keywords/%d.txt" % f_num,False)
    print "Strength-Document No. %d is finished" % f_num
