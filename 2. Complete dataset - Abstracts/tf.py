# G.M. Vazquez-Sanchez - 04/07/2015 - UoE MSc Artificial Intelligence - Dissertation
# This code computes the TF of each NP (noun phrase) in the collection of papers
# The output is a document where NPs are sorted from higher to lower TF

import operator
from collections import defaultdict

def get_np(f_name): 
    """Gets nounphrases (NPs) from the preprocessing stage."""
    f = open(f_name,'r')
    np = f.readlines()
    np = map(str.strip,np)
    f.close()
    return np

def get_tf(np):
    """Gets the term-frequency of each NP in a document."""
    counts = defaultdict(float)
    for k_word in np:
        counts[k_word] += 1.0
    return counts

def save_k_words(k_words,f_name,value):
    f = open(f_name,'w')
    for k_word in k_words:
        if k_word:
            if value:
                f.write(str(k_word[1]) + " " + k_word[0] + "\n")
            else:
                f.write(k_word[0] + "\n")
    f.close()

for f_num in range (1,2305):
    np = get_np("pp_docs/%d.txt" % f_num)
    tf = get_tf(np)
    sorted_tf = sorted(tf.items(), key=operator.itemgetter(1), reverse=True)
    save_k_words(sorted_tf,"results/tf/with_tf_values/%d.txt" % f_num,True)
    save_k_words(sorted_tf,"results/tf/just_keywords/%d.txt" % f_num,False)
    print "TF-Document No. %d is finished" % f_num