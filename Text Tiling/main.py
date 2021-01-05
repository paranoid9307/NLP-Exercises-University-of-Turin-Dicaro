import utils as ut
import textTiling as tt

#getting the document as a list
document = ut.getSentences("./txtFiles/HistoryOfRome.txt")

#dividing the document in equal parts (of six sentences each one)
divided_document, just_words = ut.divideDocument(document)

#calculating similarities between the parts of the document with a statistical approach
similarities = []
for i in range(len(just_words)-1):
    similarities.append(ut.getSimilarity(just_words[i], just_words[i+1]))

#getting the values that are local minimums and the indexes correspondent at the parts of the document 
#that have a similarity with the parts that are next to them different from the rest of the similarities 
local_min = ut.local_min(similarities)
index = [similarities.index(m) for m in local_min]
index.append(len(similarities))

#dividing the document using the new splitting points
new_divided = tt.divideDocument(divided_document, index)

#writing the results to files
ut.writeTiling(new_divided, "./output/Tiling.txt" )
ut.writeEqualDivision(divided_document, "./output/EqualDivision.txt" )
ut.createPlot(similarities, index)


