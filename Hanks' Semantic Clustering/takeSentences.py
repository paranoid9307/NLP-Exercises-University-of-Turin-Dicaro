import nltk
import utils as ut
from nltk.corpus import semcor as sc
import csv

#this script is executed once and permit to retrieve all the sentences which contains
#the choosen verb (in this case 'Give') from SEMCOR

semcor_sentences = sc.sents()
pos_tagged_sentences = sc.tagged_sents(tag = 'pos')
pos_tagged_sentences = getVerbs(pos_tagged_sentences)
indexes = []
for ind in range (len(pos_tagged_sentences)):
    if "give" in pos_tagged_sentences[ind]:
        indexes.append(ind)
test_sent = [semcor_sentences[x] for x in indexes]
with open('./txtFiles/sentences.txt','w', newline="") as f:
   csv.writer(f,delimiter=" ").writerows(test_sent)

#extract only the verbs from the sentences in SEMCOR using the already pos tagged sentences
def getVerbs(tagged_sentence):
    just_verbs = []
    lemmatizer = nltk.WordNetLemmatizer()
    for sem_sent in tagged_sentence:
        verbs = [po.leaves() for po in sem_sent 
        if ((po.label() == 'VB') 
        and (len(po.leaves()) == 1))]
        verbs = [val for sublist in verbs for val in sublist]
        ind = 0
        for v in verbs:
            verbs[ind] = lemmatizer.lemmatize(v, 'v')
            ind += 1
        just_verbs.append(verbs)
        return  just_verbs