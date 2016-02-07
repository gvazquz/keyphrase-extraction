# G.M. Vazquez-Sanchez - 04/07/2015 - UoE MSc Artificial Intelligence - Dissertation
# This code computes the TF-IDF of each NP (noun phrase) in the collection of papers
# The output is a document where NPs are sorted from higher to lower TF-IDF

import operator
import math
from collections import defaultdict

def get_np(f_name): 
    """Gets noun phrases (NPs) from the preprocessing stage."""
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

def get_df(k_words,df_dic):
    """Gets the document-frequency of each NP in the collection."""
    for k_word in k_words:
        df_dic[k_word] += 1.0
    return df_dic

def save_k_words(k_words,f_name,value):
    f = open(f_name,'w')
    for k_word in k_words:
        if k_word:
            if value:
                f.write(str(k_word[1]) + " " + k_word[0] + "\n")
            else:
                f.write(k_word[0] + "\n")
    f.close()

tf_dic = defaultdict()
df_dic = defaultdict(float)
D_dic = defaultdict()
C = 0.0

for f_num in range (1,2305):
    np = get_np("pp_docs/%d.txt" % f_num)
    tf_dic[f_num] = get_tf(np)
    df_dic = get_df(tf_dic[f_num].keys(),df_dic)
    D_dic[f_num] = len(np) 
    C += 1.0

for f_num in range (1,2305):
    k_words = tf_dic[f_num].keys()
    tf_idf = defaultdict()
    for k_word in k_words:
        tf = tf_dic[f_num][k_word]
        df = df_dic[k_word]
        D = D_dic[f_num]
        tf_idf[k_word] = (tf/D) * (math.log(C/df))
    sorted_tf_idf = sorted(tf_idf.items(), key=operator.itemgetter(1), reverse=True)
    save_k_words(sorted_tf_idf,"results/tf_idf/with_tf_idf_values/%d.txt" % f_num,True)
    save_k_words(sorted_tf_idf,"results/tf_idf/just_keywords/%d.txt" % f_num,False)
    print "TF-IDF-Document No. %d is finished" % f_num
