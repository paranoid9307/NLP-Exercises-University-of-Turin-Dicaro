import csv
import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import wordnet as wn
from collections import Counter
from collections import defaultdict
from prettytable import PrettyTable

#all the correct concepts, used in writing the results
correct_terms = ["justice", "patience", "greed", "politics", "food", "radiator", "vehicle", "screw"] 

"""
Load a csv file
Input:
    path: file path
Output:
    dataset: dictionary in this form: {'Concetto 1': [definitions]... 'Concetto n': [definitions]}
"""
def loadCsv(path):
    columns = defaultdict(list) # each value in each column is appended to a list
    with open(path) as f:
        reader = csv.DictReader(f) # read rows into a dictionary format
        for row in reader: # read a row as {column1: value1, column2: value2,...}
            for (k,v) in row.items(): # go over each column name and value 
                columns[k].append(v) # append the value into the appropriate list
    return columns                             
"""
Preprocess a list of sentence
Input:
    definitions: list of sentence
Output:
    processed: list of words (no punct, no stop words)
"""
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
    lemmatizer = nltk.WordNetLemmatizer()
    tokens = nltk.word_tokenize(sentence.lower())
    tokens = filter(lambda x: x not in stop_words and x not in punct, tokens)
    return list((lemmatizer.lemmatize(w) for w in tokens))
    
"""
Order a list of sentence by the most common words
Input:
    list_of_words: list of sentence
Output:
    list of words processed and sorted by the most common words 
"""
def getCommonWords(list_of_words):
    return list(Counter(preProcess(list_of_words)).keys())

#write a table on a file
def writeTable(table, path):
    data = table.get_string()
    with open(path, 'w') as f:
        f.write(data)

"""
Write in a table the correct concepts, the authomatic concepts found and the corrispective definitions
Input: 
    c1,...c8 = lists of synsets sorted by the higher overlap with the given definitions
Output:
    res =  PrettyTable
"""
def getTableResult(c1, c2, c3, c4, c5, c6, c7, c8):
    
    res = PrettyTable()
    res.field_names = ["Correct Concept", "Authomatic Concept", "Definition"]
    res.add_row([correct_terms[0], c1[0].name(), c1[0].definition()])
    res.add_row([correct_terms[1], c2[0].name(), c2[0].definition()])
    res.add_row([correct_terms[2], c3[0].name(), c3[0].definition()])
    res.add_row([correct_terms[3], c4[0].name(), c4[0].definition()])
    res.add_row([correct_terms[4], c5[0].name(), c5[0].definition()])
    res.add_row([correct_terms[5], c6[0].name(), c6[0].definition()])
    res.add_row([correct_terms[6], c7[0].name(), c7[0].definition()]) 
    res.add_row([correct_terms[7], c8[0].name(), c8[0].definition()])
    return res

#write all the found concepts on a file
def writeResults(c1, c2, c3, c4, c5, c6, c7, c8):
    result_list = [c1, c2, c3, c4, c5, c6, c7, c8]
    with open("./output/allFoundConcepts.txt", "a") as a_file:
        ind = 0
        for term in correct_terms:
            a_file.write(term)
            a_file.write("\n")
            a_file.write(str(result_list[ind]))
            a_file.write("\n")
            a_file.write("\n")
            ind += 1
    