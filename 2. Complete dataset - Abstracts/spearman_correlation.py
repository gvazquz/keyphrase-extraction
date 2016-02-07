# G.M. Vazquez-Sanchez - 05/07/2015 - UoE MSc Artificial Intelligence - Dissertation
# This code is the evaluation of the correlation between the keyword rankings obtained by different methods
# This code evaluates: TF, TF-IDF, PageRank, Degree, Betweenness, Closeness and Strength
# The output is Spearman's rank correlation coefficient for each pair of methods and
# A graph to illustrate the ranking correlalation

import matplotlib.pyplot as plt
import scipy.stats
import numpy as np

def get_keywords(f_name):
    """Opens the file of the results (Keyword extraction in each method)."""
    f = open(f_name,'r')
    keywords = f.readlines()
    keywords = map(str.strip,keywords)
    f.close()
    return keywords

methods = ["tf","tf_idf","pagerank","degree","betweenness","closeness","strength"]
methods_names = ["TF","TF-IDF","PageRank","Degree","Betweenness","Closeness","Strength"]

for m in range(0,len(methods)-1):
    m_1 = methods[m]
    for n in range(m+1,len(methods)):
        m_2 = methods[n]
        spearman_list = []
        for f_num in range(1,2305):
            if f_num != 842 and f_num != 1793: # Eliminate papers that doesn't have abstract
                method_1 = get_keywords("results/" + m_1 + "/just_keywords/%d.txt" % f_num)
                method_2 = get_keywords("results/" + m_2 + "/just_keywords/%d.txt" % f_num)
                x = []
                y = []
                i = 1
                for keyword in method_1:
                    x.append(i)
                    y.append(method_2.index(keyword)+1)
                    i += 1
                spearman_list.append(scipy.stats.spearmanr(x,y)[0])
        print m_1 + " - " + m_2 + " correlation coefficient is:"
        print np.mean(spearman_list)
        plt.scatter(x,y)
        plt.xlabel(methods_names[m])
        plt.ylabel(methods_names[n])
        plt.title('Correlation between graph measures')
        plt.text(25,0,r'$\rho=%f$' % np.mean(spearman_list))
        plt.savefig("plots/spearman_" + m_1 + "_" + m_2 + ".jpg")
        plt.show()
        plt.close()