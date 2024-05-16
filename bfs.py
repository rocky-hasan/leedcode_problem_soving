# graph algorythm
# total_vartex=int(input('Enter totall vartex : '))
# graph={}
# flag=True
# for i in range(total_vartex):
#     vartex=input('Enter vartex : ')
#     graph[vartex]=list()
#     while flag:
#         child=input(f'Enter child of vartex {vartex} : ')
#         if child:
#             graph[vartex].append(child)
#         else:
#             flag=False
#     flag=True
# print(graph)

#   BFS Algorythm
total_vartex=int(input('Enter totall vartex : '))
graph={}
flag=True
visited=[]
queue=[]
def bfs(graph,temp):
    visited.append(temp)
    queue.append(temp)
    while queue:
        node=queue.pop(0)
        print(node, end=' ')
        for child in graph[node]:
            if child not in visited:
                visited.append(child)
                queue.append(child)





for i in range(total_vartex):
    vartex=input('Enter vartex : ')
    graph[vartex]=list()
    while flag:
        child=input(f'Enter child of vartex {vartex} : ')
        if child:
            graph[vartex].append(child)
        else:
            flag=False
    flag=True
print(graph)
bfs(graph,'A')