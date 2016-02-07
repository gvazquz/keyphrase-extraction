# G.M. Vazquez-Sanchez - 05/07/2015 - UoE MSc Artificial Intelligence - Dissertation
# This code is the evaluation of the keyword extraction stage
# This code evaluates: TF, TF-IDF, PageRank, Degree, Betweenness, Closeness and Strength
# The output is a Precision-Recall (P-R) curve for a Recall from 0 to 70%

import numpy as np
import matplotlib.pyplot as plt

def get_text(f_name): 
    """Opens the file of the results (Keyword extraction in each method) and the key file."""
    f = open(f_name,'r')
    text = f.readlines()
    text = map(str.strip,text)
    f.close()
    return text

def get_precision(extracted_kw,reference_kw):
    """Computes precision."""
    intersection = set(extracted_kw).intersection(reference_kw)
    N = len(extracted_kw) * 1.0
    precision = (len(intersection)/N) * 100.00
    return precision

def get_recall(extracted_kw,reference_kw):
    """Computes recall."""
    intersection = set(extracted_kw).intersection(reference_kw)
    N = len(reference_kw) * 1.0
    recall = (len(intersection)/N) * 100.00
    return recall

def save_text(text,f_name):
    f = open(f_name,'w')
    for number in text:
        f.write(str(number) + "\n")
    f.close()

precision_dict = {"tf":[],"tf_idf":[],"pagerank":[],"degree":[],"betweenness":[],"closeness":[],"strength":[]}
recall_dict = {"tf":[],"tf_idf":[],"pagerank":[],"degree":[],"betweenness":[],"closeness":[],"strength":[]}

for centr_measure in precision_dict.keys():
    rcll = 0
    threshold = 1
    while(rcll < 70):
        precision = []
        recall = []
        for f_num in range (1,2305):
            extracted_kw = get_text("results/" + centr_measure + "/just_keywords/%d.txt" % f_num)
            reference_kw = get_text("pp_keys/%d.txt" % f_num)
            precision.append(get_precision(extracted_kw[0:threshold],reference_kw))
            recall.append(get_recall(extracted_kw[0:threshold],reference_kw))
        precision_dict[centr_measure].append(np.mean(precision))
        recall_dict[centr_measure].append(np.mean(recall))
        rcll = np.mean(recall)
        threshold += 10
    save_text(recall_dict[centr_measure],"recall/" + centr_measure + ".txt")
    save_text(precision_dict[centr_measure],"precision/" + centr_measure + ".txt")
    print "Evaluation for: " + centr_measure + " is ready"
        
# Plot the results in a P-R curve
plt.plot(recall_dict["tf"],precision_dict["tf"],color='orange',marker='d',label="TF")
plt.plot(recall_dict["tf_idf"],precision_dict["tf_idf"],'r',marker='s',label="TF-IDF") 
plt.plot(recall_dict["pagerank"],precision_dict["pagerank"],'b',marker='*',label="PageRank")
plt.plot(recall_dict["degree"],precision_dict["degree"],'g',marker="o",label="Degree")
plt.plot(recall_dict["betweenness"],precision_dict["betweenness"],'c',marker="x",label="Betweenness")
plt.plot(recall_dict["closeness"],precision_dict["closeness"],'y',marker="+",label="Closeness")
plt.plot(recall_dict["strength"],precision_dict["strength"],'m',marker="^",label="Strength")
plt.xlabel('Recall (%)')
plt.ylabel('Precision (%)')
plt.title('P-R Curve')
plt.grid(True)
plt.legend()
plt.show()