Run the *.py files in the next order:

	1. preprocessing.py -> Preprocesses the abstract of the documents to find the noun phrases aka. candidate key phrases.
	2. directed_graph.py -> Builds the edges of the directed graph for each document.
	3. undirected_graph.py -> Builds the edges of the undirected graph for each document.
	4. tf.py -> Ranks the candidate key phrases of each document according to their TF score.
	5. tf_idf.py -> Ranks the candidate key phrases of each document according to their TF-IDF score.
	6. pagerank.py -> Ranks the candidate key phrases of each document according to their PageRank score.
	7. strength.py Ranks the candidate key phrases of each document according to their Strength score.
	8. centrality_measures.py Ranks the candidate key phrases of each document according to three scores: Degree, Closeness and Betweenness.
	9. evaluation.py -> Computes Precision, Recall and P-R curves to compare the performance of the different key phrase extraction methods.
	10. plot.py -> Plots and saves the P-R curves.
	11. spearman_correlation.py -> Computes Spearman’s rank correlation coefficient between the rankings obtained through each method.