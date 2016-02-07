# G.M. Vazquez-Sanchez - 04/07/2015 - UoE MSc Artificial Intelligence - Dissertation
# This code is for preprocessing the raw text of a collection of papers
# The output is a list of NPs (nounphrases) extracted from each paper
# The code also preprocesses the reference keywords of the key-files
# At the end, it gets the percentage of keywords captured in the preprocessing stage of the text-files
# This code ONLY preprocess the abstract of each paper in the dataset, not the full text

import nltk
import os
import numpy as np

sentence_re = r'''(?x)      # set flag to allow verbose regexps
      ([A-Z])(\.[A-Z])+\.?  # abbreviations, e.g. U.S.A.
    | \w+(-\w+)*            # words with optional internal hyphens
    | \$?\d+(\.\d+)?%?      # currency and percentages, e.g. $12.40, 82%
    | \.\.\.                # ellipsis
    | [][.,;"'?():-_`]      # these are separate tokens
'''

lemmatizer = nltk.WordNetLemmatizer()
stemmer = nltk.stem.porter.PorterStemmer()

# Taken from Su Nam Kim Paper...
grammar = r"""
    NBAR:
        {<NN.*|JJ>*<NN.*>}  # Nouns and Adjectives, terminated with Nouns
        
    NP:
        {<NBAR>}
        {<NBAR><IN><NBAR>}  # Above, connected with in/of/etc...
"""
chunker = nltk.RegexpParser(grammar)

from nltk.corpus import stopwords
stopwords = stopwords.words('english')

def leaves(tree):
    """Finds NP (nounphrase) leaf nodes of a chunk tree."""
    for subtree in tree.subtrees(filter = lambda t: t.label() == 'NP'):
        yield subtree.leaves()

def normalise(word):
    """Normalises words to lowercase and stems and lemmatizes it."""
    word = word.lower()
    word = stemmer.stem_word(word)
    word = lemmatizer.lemmatize(word)
    return word

def acceptable_word(word):
    """Checks conditions for acceptable word: length, stopword."""
    accepted = bool(2 <= len(word) <= 40
        and word.lower() not in stopwords)
    return accepted

def get_terms(tree):
    """Returns NPs (nounphrases) of a tree from the text of the paper."""
    terms = []
    for leaf in leaves(tree):
        term = [normalise(w) for w,t in leaf if acceptable_word(w)]
        term = " ".join(term)
        terms.append(term)
    return terms

def get_keys(text):
    """Preprocesses the reference keywords from the key file."""
    keywords = []
    for keyword in text:
        keyword = [normalise(w) for w in keyword.split() if acceptable_word(w)]
        keyword = " ".join(keyword)
        keywords.append(keyword)
    return keywords
                
def read_text(f_name):
    f = open(f_name,'r')
    try:
        text = f.readlines()
        text = map(str.strip,text)
    finally:
        f.close()
    return text

def get_abstract(text):
    i = 1 + text.index('--A')
    j = text.index('--B')
    abstract = text[i:j]
    return abstract

def evaluation(terms,keys):
    """Finds the recall of the preprocessing stage."""
    matches = set(terms).intersection(keys)
    ratio = len(matches) * 1.0 /len(keys)
    return ratio

def save_text(text,f_name):
    f = open(f_name,'w')
    for k_word in text:
        if k_word:
            f.write(k_word + "\n")
    f.close()

all_ratios = []
index = 1

for f_num in range (52795,1040307):
    # Check whether a file exists...
    if os.path.isfile("all_docs/%d.txt" % f_num):
        
        # Get NPs from the text
        text = read_text("all_docs/%d.txt" % f_num)
        abstract = get_abstract(text)
        terms = []
        for sentence in abstract:
            toks = nltk.regexp_tokenize(sentence,sentence_re)
            if toks:
                postoks = nltk.tag.pos_tag(toks)
                tree = chunker.parse(postoks)
                terms.extend(get_terms(tree))
        terms = filter(None, terms)
        
        # Get reference keywords from key file and preprocess them
        text = read_text("all_docs/%d.key" % f_num)
        keys = get_keys(text)
        
        # Compute recall of the current document
        ratio = evaluation(terms,keys)
        all_ratios.append(ratio)
        
        # Save NPs and preprocessed keywords
        save_text(terms,"pp_docs/%d.txt" % index)
        save_text(keys,"pp_keys/%d.txt" % index)
        
        print "Document No. %d is finished" % index
        index += 1

# Print the average recall of keywords extracted
print np.mean(all_ratios)
print "Percentage of keywords found: %f" % np.mean(all_ratios)