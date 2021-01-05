
import spacyUtils as su
import utils as ut
from prettytable import PrettyTable

#importing sentences
sentences = ut.importSentences('./txtFiles/sentences.txt',100)

#creating the table that will contain results
results = PrettyTable()
results.field_names = ["Sentence", "Hypernym relations (Such as)", "Verbal relations", "Adjective relations"]

#obtaining informations from the sentences
for s in sentences:
    such, verb, adj = su.get_relations(s)
    results.add_row([s, such, verb, adj])
#writing the results
ut.writeTable(results, './output/results.txt')