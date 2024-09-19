d={1:[1,2],2:[1,3,4],3:[1,2,4],4:[2,3]}
q=[1]
vis=[1]
while q:
    a=q.pop(0)
    print(a)
    for i in d[a]:
        if i not in vis:
            q.append(i)
            vis.append(i)
            