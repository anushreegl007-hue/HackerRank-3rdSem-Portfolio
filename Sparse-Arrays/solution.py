
def matchingStrings(stringList, queries):
    counts = {}
    for s in stringList:
        counts[s] = counts.get(s, 0) + 1
        
    return [counts.get(q, 0) for q in queries]
