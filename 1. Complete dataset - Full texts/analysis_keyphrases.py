# G.M. Vazquez-Sanchez - 05/07/2015 - UoE MSc Artificial Intelligence - Dissertation
# This code is the TF analysis of the expert assigned keywords
# We want to know the percentage of keywords with TF = {1,2,3...}
# The output is a normalised histogram of TF vs Probability

from collections import defaultdict
import os
import matplotlib.pyplot as plt

count = []

for f_num in range (52795,1040307):
    # Check whether a file exists...
    if os.path.isfile("all_docs/%d.txt" % f_num):
        
        f = open("all_docs/%d.txt" % f_num)
        # Read the document
        text = f.read().lower()
        # Read the assigned keywords
        for keyword in open("all_docs/%d.key" % f_num).readlines():
            if keyword.strip() in text:
                c = text.count(keyword.strip()) # Compute TF
                count.append(c)
            else:
                count.append(0)
        print f_num

tf_values = list(set(count))
tf_values.sort()

plt.hist(filter(lambda a: a <= 150, count),bins=filter(lambda a: a <= 150, tf_values),normed=True)
plt.title("Histogram: TF of the reference keyphrases")
plt.xlabel("TF values")
plt.ylabel("Probability")
plt.savefig("plots/histogram_tf_vs_probability.jpg")
plt.show()
plt.close()