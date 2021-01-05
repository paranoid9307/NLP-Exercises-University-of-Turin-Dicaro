import nltk
import utils as ut
from nltk.corpus import wordnet as wn

"""
Return a list of synset, related to a concept. The list contains the synset of every
common word, its hypernyms and its hyponym, sorted by the overlaps with context 
(list[0] will be the most probable sense).
Input: 
    common_words = lists of the 10 most common words in the definition  
    context = list of processed words from the definitions of every concept
Output:
    overlaps_list =  list of synset sorted by the overlaps
"""
def getConcepts (common_words, context):
    overlaps_list = []

    for word in common_words:
        hyper_list = getAllHypernyms(word)
        hypo_list = getAllHyponyms(word)
        overlaps_list.extend(getSynsetsOverlap(wn.synsets(word), context))
        overlaps_list.extend(getSynsetsOverlap(hyper_list, context))
        overlaps_list.extend(getSynsetsOverlap(hypo_list, context))
    overlaps_list.sort(key=lambda tup: tup[1], reverse=True)  
    overlaps_list = [a_tuple[0] for a_tuple in overlaps_list]

    #returning 10 because lists are long
    return overlaps_list[:10]

#get the wordnet hypernyms of a word
def getAllHypernyms(word):
    hyper_list = []
    for ss in wn.synsets(word):
        hyper_list.extend(ss.hypernyms())
    return hyper_list

#get the wordnet hyponyms of a word
def getAllHyponyms(word):
    hypo_list = []
    for ss in wn.synsets(word):
        hypo_list.extend(ss.hyponyms())
    return hypo_list

"""
Create a list of tuples that contains all the synsets and the corrispective overlap with the given context
Input: 
    synsets = lists of synsets 
    context = list of processed words from the definitions of every concept
Output:
    best_synsets =  list of tuples in the form : [(synset 1, overlap 1),...(synset n, overlap n)]
"""
def getSynsetsOverlap(synsets, context):
    best_synsets = []
    for syn in synsets:
        syn_context = getSynsetContext(syn)
        overlap = intersection(syn_context, context)
        best_synsets.append((syn, overlap))        
    return best_synsets 

# get the context of a synset (formed by its definition and its examples) 
# in a bag-of-word approach
def getSynsetContext(s):
    context=ut.bagOfWords(s.definition())
    for e in s.examples():
        context=list(set().union(context, ut.bagOfWords(e)))
    return context

#intersection between two lists
def intersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return len(lst3)