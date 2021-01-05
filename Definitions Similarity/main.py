import utils as ut
from prettytable import PrettyTable

#loading definitions
definitions = ut.loadCsv('./csvFiles/definizioni.csv')
#preprocessing definitions
building = ut.preProcess(definitions['concrete_generic'])
molecule = ut.preProcess(definitions['concrete_specific'])
freedom = ut.preProcess(definitions['abstract_generic'])
compassion = ut.preProcess(definitions['abstract_specific'])
#getting similarity
similarity_building = ut.getSimilarity(building)
similarity_molecule = ut.getSimilarity(molecule)
similarity_freedom = ut.getSimilarity(freedom)
similarity_compassion = ut.getSimilarity(compassion)
#create a table with the results
results = PrettyTable()
results.field_names = ["", "Abstract", "Concrete"]
results.add_row(["Generic" , 
        round(similarity_freedom,2), 
        round(similarity_building,2)])
results.add_row(["Specific" , 
        round(similarity_compassion,2), 
        round(similarity_molecule,2)])
#save the table to a file
ut.writeTable(results,'output/results.txt')