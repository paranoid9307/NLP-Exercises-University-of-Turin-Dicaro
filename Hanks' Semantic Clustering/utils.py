import nltk
from nltk.stem import WordNetLemmatizer
from nltk import Tree
import spacy
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

#importing the sentences taken from SEMCOR
def importSentences(path):
    f = open(path, 'r')
    content = f.readlines()
    content = list(map(str.strip,content))
    f.close()
    return content

#the method uses the library spacy to extract a dependency tree from a sentence   
def getTree(sentence):
    nlp = spacy.load('en_core_web_sm')
    sent = str(sentence)
    nlp_doc=nlp(sent)
    return nlp_doc

"""
Extract subjects and objects of verb selected
Input:
    verb: selected verb
    sentences: the list containing all the sentences which contains the selected verb
Output:
    subject_object_list: a list in the form [([subject_1], [object_1], [index of the sentence],...[])
"""
def extractVerbSubjObj (verb, sentences):
    subj_dept = ['nsubj', 'nsubjpass']
    obj_dept = ['dobj', 'obj']
    lemmatizer = WordNetLemmatizer()
    subj_obj_list = []
    ind = 0
    for s in sentences:
        tree = getTree(s)
        verbAddress = next(t.text for t in tree if lemmatizer.lemmatize(t.text, 'v') == verb)
        subjects = list(t.text for t in tree if str(t.head) == verbAddress and t.dep_ in subj_dept)
        objects = list(t.text for t in tree if str(t.head) == verbAddress and t.dep_ in obj_dept)
        subj_obj_list.append([subjects, objects, [ind]])
        ind += 1
    return subj_obj_list

#returns a list containing only the tuples with three elements (subject, object, index of the sentence from which 
#the two elements are taken)
def cleanData (subject_object_list):
    new = []
    for sub in subject_object_list:
        new.append(sum(sub, []))
    new = [sub for sub in new if len(sub)==3] 
    return new

#write the results on a txt file
def writeResults(length_analyzed, total_sentences, frequencies):
    path = Path('./output/results.txt')
    if path.is_file():
        path.unlink()

    with open("./output/results.txt", "a") as a_file:
        a_file.write("Analyzed verb: GIVE ")
        a_file.write("\n")
        a_file.write("Total number of sentences with the analyzed verb in the SEMCOR corpus: "+str(total_sentences))
        a_file.write("\n")
        a_file.write("Analyzed sentences (after cleaning the data): "+str(length_analyzed))
        a_file.write("\n")
        a_file.write("Number of semantyc types found: "+str(len(frequencies)))
        a_file.write("\n")
        a_file.write(str([*frequencies]))

#create a graph containing the 20 more frequent semantyc types
def createHorizontalBar(couples, frequencies):
    path = Path('./output/hBar.png')
    if path.is_file():
        path.unlink()

    fig, ax = plt.subplots()
    y_axis = np.arange(len(frequencies))
    ax.barh(y_axis, frequencies, align='edge', color='blue', ecolor='black')
    ax.set_xlabel('Frequencies')
    ax.set_title('Semantic clusters for GIVE')
    ax.set_yticks(y_axis)
    ax.set_yticklabels(couples, fontsize=9)
    plt.subplots_adjust(left=0.55)
    plt.subplots_adjust(bottom=0.25)
    plt.savefig('./output/hBar.png',dpi=400)
    
