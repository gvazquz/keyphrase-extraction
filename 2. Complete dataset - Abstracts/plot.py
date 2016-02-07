# G.M. Vazquez-Sanchez - 06/07/2015 - UoE MSc Artificial Intelligence - Dissertation
# This code is for plotting the results of the evaluation stage
# This code plots: TF, TF-IDF, PageRank, Degree, Betweenness, Closeness and Strength
# The output is a Precision-Recall (P-R) curve for a Recall from 0 to 27%

import matplotlib.pyplot as plt

def get_text(f_name): 
    """Opens the file of the precision and recall results."""
    f = open(f_name,'r')
    text = f.readlines()
    text = map(str.strip,text)
    floats = map(float,text)
    f.close()
    return floats

# Get results...
recall_tf = get_text("recall/tf.txt")
precision_tf = get_text("precision/tf.txt")
recall_tf_idf = get_text("recall/tf_idf.txt")
precision_tf_idf = get_text("precision/tf_idf.txt")
recall_pagerank = get_text("recall/pagerank.txt")
precision_pagerank = get_text("precision/pagerank.txt")
recall_degree = get_text("recall/degree.txt")
precision_degree = get_text("precision/degree.txt")
recall_betweenness = get_text("recall/betweenness.txt")
precision_betweenness = get_text("precision/betweenness.txt")
recall_closeness = get_text("recall/closeness.txt")
precision_closeness = get_text("precision/closeness.txt")
recall_strength = get_text("recall/strength.txt")
precision_strength = get_text("precision/strength.txt")

# Plot the results in a P-R curve
plt.figure()
plt.plot(recall_tf,precision_tf,color='brown',marker='+',label="TF")
plt.plot(recall_tf_idf,precision_tf_idf,'r',marker='s',label="TF-IDF")
plt.plot(recall_pagerank,precision_pagerank,'m',marker="^",label="Pagerank")
plt.plot(recall_degree,precision_degree,color='g',marker="o",label="Degree")
plt.plot(recall_betweenness,precision_betweenness,'b',marker="*",label="Betweenness")
plt.plot(recall_closeness,precision_closeness,'y',marker="v",label="Closeness")
plt.plot(recall_strength,precision_strength,'c',marker="x",label="Strength")
plt.xlabel('Recall (%)')
plt.ylabel('Precision (%)')
plt.title('P-R Curve')
plt.grid(True)
plt.legend()
plt.savefig("plots/pr_curves.jpg")
plt.show()
plt.close()