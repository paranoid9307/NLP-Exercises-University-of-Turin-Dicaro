import nltk
from nltk.corpus import wordnet as wn
from nltk.wsd import lesk

"""
Input:
    sentences: list of sentences with the selected verb form SEMCOR
    subj_obj_list: a list of tuples in the form [(subject, object, index of the corrispondent sentence)]
Output:
    sem_type: list of tuples in the form[(subject supersense, object supersense)]
"""
def getSemanticTypes (sentences, subj_obj_list):
    sem_type = []
    for sub in subj_obj_list:
        subj_ss = getSuperSense(sentences[sub[2]], sub[0])
        obj_ss = getSuperSense(sentences[sub[2]], sub[1])
        sem_type.append((subj_ss, obj_ss))
    return sem_type

#using the Nltk lesk alghorithm that returns a wordnet synset,
#this method return a wordnet super sense (with the function lexname())
#of a given word
def getSuperSense(sentence, ambiguous):
    person_pronouns = ['i', 'you', 'he', 'she', 'we', 'you', 'they', 'me', 'you', 'him', 'her', 'us', 'them']
    if ambiguous in person_pronouns:
        return 'noun.person'
    if ambiguous == 'it':
        return 'noun.object'
    sense = lesk (sentence, ambiguous, pos='n' )
    if not sense:
        return 'noun.object'
    super_sense = sense.lexname()
    return str(super_sense)
