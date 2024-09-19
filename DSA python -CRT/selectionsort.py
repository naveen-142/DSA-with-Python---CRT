def selectionsort(L):
    for scan in range(1,len(L)):
        MEI= scan-1
        for index in range(scan,len(L)):
            if (L[MEI] > L[index]):
                MEI =index
        L[MEI],L[scan-1]=L[scan-1],L[MEI]
def Display(L):
    for i in range(len(L)):
        print(L[i],end=' ')
L=[7,-1,5,3,9,0]
selectionsort(L)
Display(L)