import patterns
import spacy
from spacy.matcher import Matcher 
from spacy.tokens import Span 
from spacy.strings import *

#this method create a list of noun-adjective phrases that are in the sentence, navigating the spacy tree (doc)
def getAdjectiveRelations(text, nlp):    
    doc = nlp(text)
    adj = []    
    for token in doc:
        phrase = ''
        # if the word is a subject noun or an object noun
        if (token.pos_ == 'NOUN')\
            and (token.dep_ in ['dobj','pobj','nsubj','nsubjpass']):            
            # iterate over the children nodes
            for subtoken in token.children:
                # if word is an adjective or has a compound dependency
                if (subtoken.pos_ == 'ADJ') or (subtoken.dep_ == 'compound'):
                    phrase += subtoken.text + ' '                    
            if len(phrase)!=0:
                phrase += token.text             
        if  len(phrase)!=0:
            adj.append(phrase)     
    return adj

#this method create a list of verbal phrases that are in the sentence, navigating the spacy tree (doc)
def getVerbRelations(text, nlp):    
    doc = nlp(text)    
    sent = []    
    for token in doc:        
        # if the token is a verb
        if (token.pos_=='VERB'):            
            phrase =''            
            # only extract noun or pronoun subjects
            for sub_tok in token.lefts:                
                if (sub_tok.dep_ in ['nsubj','nsubjpass']) and (sub_tok.pos_ in ['NOUN','PROPN','PRON']):                    
                    # add subject to the phrase
                    phrase += sub_tok.text
                    # save the root of the verb in phrase
                    phrase += ', '+token.lemma_ 
                    # check for noun or pronoun direct objects
                    for sub_tok in token.rights:                        
                        # save the object in the phrase
                        if (sub_tok.dep_ in ['dobj']) and (sub_tok.pos_ in ['NOUN','PROPN']):                                    
                            phrase += ', '+sub_tok.text
            sent.append(phrase)            
    sent = [s for s in sent if s]
    return sent

#using the spacy matcher and a given pattern this method create a list that contain all the matches
#of the sentence with the "such as" pattern
def getHypernymRelation(text, nlp):
    hyp_rel = []
    matcher = Matcher(nlp.vocab)
    doc = nlp(text)
    matcher.add("SuchAs", None, patterns.such_pattern)
    matches = matcher(doc)
    for m in matches:
        span = doc[m[1]:m[2]]
        hyp_rel.append(span.text)
    return hyp_rel
    
"""
Extract three types of relations from a given sentence: hypernym relation with one of Hearst patterns, verb relations 
(subject, verb and eventually object) and noun-adjective relations
Input:
    sentence: a sentence from the corpus
Output:
    such_as_rel: a list containing all the parts of the sentence that match the "such as" pattern
    verb_rel: a list of all the verbal phrases in the sentence
    adj_rel: a list of all the adjective phrases in the sentence
"""
def get_relations(sentence):
    nlp = spacy.load('en_core_web_sm')
    such_as_rel = getHypernymRelation(sentence, nlp)
    verb_rel = getVerbRelations(sentence, nlp)
    adj_rel = getAdjectiveRelations(sentence, nlp)
    return such_as_rel, verb_rel, adj_rel

""" "GDP in developing countries such as Vietnam will continue growing at a high rate." """
