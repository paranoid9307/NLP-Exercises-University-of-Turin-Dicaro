import itertools

#method that divide a document, using the new calculated splitting points
def divideDocument(document, intervals):
    divided = []
    i = 0    
    for min in intervals:
        if i>len(document)-1:
            break
        breaking = i + min
        if breaking>len(document)-1:
            breaking = min+1
        adding = document[i:breaking]
        adding = list(itertools.chain(*adding))
        divided.append(adding)
        #just_words.append(preProcess(document[i:breaking]))
        i=min 
    return divided