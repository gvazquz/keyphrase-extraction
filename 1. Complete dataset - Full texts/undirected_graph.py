# G.M. Vazquez-Sanchez - 04/07/2015 - UoE MSc Artificial Intelligence - Dissertation
# This code creates an undirected graph with the next characteristics:
# Nodes: Are the noun phrases obtained in the preprocessing stage
# Edges: Co-occurrence of two nodes within a window of 10 nounphrases
# Weight of the edges: Number of co-occurrences

from collections import defaultdict

def get_np(f_name):
    """Gets noun phrases from the preprocessing stage."""
    f = open(f_name,'r')
    np = f.readlines()
    np = map(str.strip,np)
    f.close()
    return np

def create_pairs(np):
    """Creates pairs of NPs (noun phrases) within a window of 10."""
    pairs = []
    for i in range (0, len(np)-1):
        pairs += zip([np[i]]*9, np[i+1:i+10])
    return pairs

def count_pairs(pairs):
    """Counts the number of co-occurrences of the pairs."""
    counts = defaultdict(float)
    for pair in pairs:
        if pair in counts:
            counts[pair] += 1.0
        else:
            if (pair[1],pair[0]) in counts:
                counts[pair] += 1.0
            else:
                counts[pair] = 1.0
    return counts

def save_pairs(counts,f_name):
    f = open(f_name,'w')
    for pair in counts.keys():
        if pair[0] != pair[1]:
            text = [pair[0],pair[1],str(counts[pair])]
            f.write("\n".join(text) + "\n")
    f.close()
                
for f_num in range (1,2305):
    np = get_np("pp_docs/%d.txt" % f_num)
    np_pairs = create_pairs(np)
    counts = count_pairs(np_pairs)
    save_pairs(counts,"graphs/undirected/%d.txt" % f_num)
    print "Undirected graph No. %d is finished" % f_num
