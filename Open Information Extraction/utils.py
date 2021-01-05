import csv 
import nltk
from nltk.corpus import semcor as sc

#getting a number of sentences from semcor corpus
def importSentences(path, num_of_sent):
    semcor_sentences = sc.sents()[:num_of_sent]
    with open('./txtFiles/sentences.txt','w', newline="") as f:
        csv.writer(f,delimiter=" ").writerows(semcor_sentences)
    f = open(path, 'r')
    content = f.readlines()
    content = list(map(str.strip,content))
    f.close()
    return content
#write a table on a file txt
def writeTable(table, path):
    data = table.get_string()
    with open(path, 'w') as f:
        f.write(data)