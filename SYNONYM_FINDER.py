words=[
    {"diseal":"Di_fog"},
    {"Organisation":"Organization"},
    {"Group":"Organisation"},
    {"Orange":"narangi"},
    {"Orange":"Krit"}

]
def checkkey(key,dic):
    for keys in dic.keys():
        if key==keys:
            return True
    return False


GRAPH ={}
for i in words:
    key=i.keys()
    for j in key:
        if checkkey(j,GRAPH)is True:
           
             GRAPH[j]+=[i[j]]
             if checkkey(i[j],GRAPH)is True:
                GRAPH[i[j]]+=[j]
             else:
                GRAPH[i[j]]=[j]
            
        else:
            GRAPH[j]=[i[j]]
            if checkkey(i[j],GRAPH) is True:
                GRAPH[i[j]]+=[j]
            else:
                GRAPH[i[j]]=[j]


print(GRAPH)
VISITED={}
for i in GRAPH.keys():
    VISITED[i]=False


def size(GRAPH ,KEY):
    j=0
    for i in GRAPH[KEY]:
        j=j+1
    return j


def DFS(GRAPH ,key):
    if VISITED[key] is True:
        return []
    LIST=[key]
    VISITED[key]=True

    if  size (GRAPH,key)==0:
        return []
    for i in GRAPH [key]:
       LIST+= DFS(GRAPH,i)
    return LIST




SET=[]
for i in GRAPH:
    if VISITED[i] is False:
        SET+=[DFS(GRAPH,i)]




print(SET)







    

