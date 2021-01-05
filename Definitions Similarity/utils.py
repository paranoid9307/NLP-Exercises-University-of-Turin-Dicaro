import csv
import nltk
from nltk.stem import PorterStemmer
from collections import Counter
"""
Load a csv file
Input:
    path: file path
Output:
    dataset: dictionary with following keys: conc_generic, conc_specific, abst_generic, abst_specific)
"""
def loadCsv(path):
    dataset = {
        'concrete_generic': [],
        'concrete_specific': [],
        'abstract_generic': [],
        'abstract_specific': []
    }
    with open(path, 'r', encoding='latin1') as fileCSV:
        for row in fileCSV.readlines()[1:]:
            temp = row.split(";")
            temp[-1] = temp[-1].replace('\n', '')

            dataset["concrete_generic"].append(temp[1])
            dataset["concrete_specific"].append(temp[2])
            dataset["abstract_generic"].append(temp[3])
            dataset["abstract_specific"].append(temp[4])

    return dataset
#preprocessing a list of sentences
def preProcess(definitions):
    sentences = [d for d in definitions if d != '']
    processed = []
    for s in sentences:
        processed.extend(bagOfWords(s))
    return processed

#method that process a sentence removing stopwords, punctuation and lemmatizing
def bagOfWords(sentence):
    stop_words = set(open('./txtFiles/stop_words_FULL.txt').read().split())
    punct = {',', ';', '.', '(', ')', '{', '}', ':', '?', '!', "''"}
    ps = PorterStemmer()
    tokens = nltk.word_tokenize(sentence.lower())
    tokens = filter(lambda x: x not in stop_words and x not in punct, tokens)
    return list((ps.stem(w) for w in tokens))
    
"""
Get similarity of definitions that are seen as a list of words. This method count the occurences of every word in 
definitions, get the max value of it and then normalize it on the number of words contained into the definition
Input:
    list_of_words: a list of words tha represents the definition
Output:
    similarity: a number that indicates how are definitions similar
"""
def getSimilarity(list_of_words):
    c = Counter(list_of_words)
    max_value = max(c.values())  # maximum value
    similarity = max_value/len(list_of_words)
    return similarity

#write a table on a file
def writeTable(table, path):
    data = table.get_string()
    with open(path, 'w') as f:
        f.write(data)
