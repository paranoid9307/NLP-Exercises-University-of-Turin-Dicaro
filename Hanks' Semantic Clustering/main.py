import nltk
import utils as ut
import wordnetUtils as wu
from collections import Counter

#importing the sentences extracted from SEMCOR
sentences = ut.importSentences('./txtFiles/sentences.txt')

#getting a list of tuples containing the subject and the object of the selected verb from the sentences
subject_object_list = ut.cleanData(ut.extractVerbSubjObj('give', sentences))

#getting a list of super senses couples, one for each analyzed sentence
semantic_types = wu.getSemanticTypes(sentences, subject_object_list)

#calculate the frequency of every couple and sorting the results
counts = Counter(semantic_types)
counts = {k: v for k, v in sorted(counts.items(), key=lambda item: item[1], reverse=True)}

#saving the results and creating a graph containing the 20 more frequent couples
ut.writeResults(len(subject_object_list), len(sentences), counts)
frequencies = [*counts.values()][:20]
couples = [*counts][:20]
ut.createHorizontalBar(couples, frequencies)

