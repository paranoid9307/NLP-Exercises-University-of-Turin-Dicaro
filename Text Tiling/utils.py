import matplotlib.pyplot as plt
import nltk
from nltk import tokenize
from nltk.stem import PorterStemmer
from collections import Counter
from pathlib import Path

#reading a document from a file
def getSentences(path):
    file = open(path,encoding="utf8")
    line = file.read().replace("\n", " ")
    file.close()
    return tokenize.sent_tokenize(line)

#function tha calculate the local minima in a list
def local_min(ys):
    return [y for i, y in enumerate(ys)
            if ((i == 0) or (ys[i - 1] >= y))
            and ((i == len(ys) - 1) or (y < ys[i+1]))]

#function that divides a document in paragraphs of 6 sentences. It returns also a list of preprocessed paragraphs, 
#used in the estimation of the similarities
def divideDocument(document):
    divided = []
    just_words = []
    i = 0
    while (i<len(document)):
        breaking = i + 6
        if breaking>len(document)-1:
            breaking = len(document)
        divided.append(document[i:breaking])
        just_words.append(preProcess(document[i:breaking]))
        i+=7
    return divided, just_words

#method the process a list of sentences
def preProcess(definitions):
    sentences = [d for d in definitions if d != '']
    processed = []
    for s in sentences:
        processed.extend(bagOfWords(s))
    return processed

#method that process a sentence removing stopwords, punctuation and lemmatizing
def bagOfWords(sentence):
    stop_words = set(open('./txtFiles/stop_words_FULL.txt').read().split())
    punct = {',', ';', '.', '(', ')', '{', '}', ':', '?', '!', "''", '“', '”' , "’"}
    lemmatizer = nltk.WordNetLemmatizer()
    tokens = nltk.word_tokenize(sentence.lower())
    tokens = filter(lambda x: x not in stop_words and x not in punct, tokens)
    return list((lemmatizer.lemmatize(w) for w in tokens))

"""
The method use a statistical approach, based on the frequency of words to calculate the similarity 
between two paragraph (a paragraph and its subsequent).
Input:
    sentences: a preprocessed paragraph (containing 6 sentences)
    sentences1: the subsequent, preprocessed, paragraph of 'sentences'
Output:
    sim: normalized value of similarity 
"""
def getSimilarity(sentences, sentences1):
    count = Counter(sentences)
    count1 = Counter(sentences1)
    word = [*count]
    word1 = [*count1]
    sim = 0
    for w in word:
        freq = count[w]
        if w in word1:
            freq += count1[w]
        else: freq = 0
        sim += freq

    return sim/len(sentences)

#method that write the originally splitted document on a file
def writeEqualDivision(document, filepath):
    path = Path('./output/EqualDivision.txt')
    if path.is_file():
        path.unlink()

    with open(filepath,"w", encoding="utf8") as f:
        for parag in document:                
            for s in parag:
                f.write(s)
                f.write("\n")
            f.write('\n'*5)  

#method that write the document divided with the calculated splitting points on a file
def writeTiling(document, filepath):
    path = Path('./output/Tiling.txt')
    if path.is_file():
        path.unlink()

    with open(filepath,"w", encoding="utf8") as f:
        for parag in document:                
            for s in parag:
                f.write(s)
                f.write("\n")
            f.write('\n'*5)             

#method that save a plot on an image
def createPlot(similarities, index):
    path = Path('./output/splittingPoints.png')
    if path.is_file():
        path.unlink()

    plt.plot(similarities)
    for i in range(len(index)-1):
        plt.axvline(x= index[i], ls = "-", color='b', linewidth=2)
    plt.ylabel('Similarities values')
    plt.xlabel('Group of sentences in the document')
    plt.savefig('./output/splittingPoints.png',dpi=400)