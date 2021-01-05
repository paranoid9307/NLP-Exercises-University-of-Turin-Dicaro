import utils as ut
import onomasiology as on


#getting the definitions
res = ut.loadCsv('./csvFiles/content-to-form2.csv')
#processing the definitions
definitions_1 = ut.getCommonWords(res['Concetto 1'])
definitions_2 = ut.getCommonWords(res['Concetto 2'])
definitions_3 = ut.getCommonWords(res['Concetto 3'])
definitions_4 = ut.getCommonWords(res['Concetto 4'])
definitions_5 = ut.getCommonWords(res['Concetto 5'])
definitions_6 = ut.getCommonWords(res['Concetto 6'])
definitions_7 = ut.getCommonWords(res['Concetto 7'])
definitions_8 = ut.getCommonWords(res['Concetto 8'])
#content to form 
concept1 = on.getConcepts(definitions_1[:10], definitions_1)
concept2 = on.getConcepts(definitions_2[:10], definitions_2)
concept3 = on.getConcepts(definitions_3[:10], definitions_3)
concept4 = on.getConcepts(definitions_4[:10], definitions_4)
concept5 = on.getConcepts(definitions_5[:10], definitions_5)
concept6 = on.getConcepts(definitions_6[:10], definitions_6)
concept7 = on.getConcepts(definitions_7[:10], definitions_7)
concept8 = on.getConcepts(definitions_8[:10], definitions_8)

#create a table and writing results
table_result = ut.getTableResult(concept1, concept2, concept3, concept4, concept5, concept6, concept7, concept8)
ut.writeTable(table_result, "./output/bestConcepts.txt")
    
ut.writeResults(concept1, concept2, concept3, concept4, concept5, concept6, concept7, concept8)
    
