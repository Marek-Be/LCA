#Node object for our binary tree.
graph = {}
#Checks if data is in given tree

def getAllParents(graphList, node):
    parents = []
    for i in range(len(graphList)):
        if (node in graphList[i][1]):
            parents.append(graphList[i][0])
    return parents

def checkTwoLists(list1,list2):
    for each in list1:
        if each in list2:
            return each
    return ""

def LCA(graph,n1,n2,n1Par = [], n2Par = []):
    if (n1 == n2 and n1 in graph):
        return n1
    graph = list(graph.items())
    n1Par.append(n1)
    n2Par.append(n2)
    n1Par = getAllParents(graph,n1)
    n2Par = getAllParents(graph,n2)

    val = checkTwoLists(n1Par,n2Par)
    if (val != ""):
        return val
    if (n1 in n2Par):
        return n1
    if (n2 in n1Par):
        return n2

    return LCA2(graph,n1,n2,n1Par,n2Par)
def LCA2(graph,n1,n2,n1Par,n2Par):
    newParents1 = n1Par[:]
    for each1 in n1Par:
        Parents = getAllParents(graph,each1)
        for each2 in Parents:
            if (each2 not in n1Par):
                newParents1.append(each2)

    newParents2 = n2Par[:]
    for each1 in n2Par:
        Parents = getAllParents(graph,each1)
        for each2 in Parents:
            if (each2 not in n2Par):
                newParents2.append(each2)

    if (newParents2 == n2Par and newParents1 == n1Par):
        return ""
    n2Par = newParents2
    n1Par = newParents1
    val = checkTwoLists(n1Par,n2Par)
    if (val != ""):
        return val
    if (n1 in n2Par):
        return n1
    if (n2 in n1Par):
        return n2
    return LCA2(graph,n1,n2,n1Par,n2Par)



# graph.update({'BASE': ['B', 'C']})
# graph.update({'B': ['D', 'E']})
# graph.update({'C': ['F', 'G']})
# graph.update({'G': ['W', 'X']})
# print(LCA(graph, "F","B"))
