list = [1,5,3,2,4]
def bubblesort(list1):
    #two loops then compare and swap

    for i in range(len(list1)-1,0,-1):
        for j in range(i):
            if (list1[j]>list1[j+1]):
                temp = list1[j+1]
                list1[j+1] = list1[j]
                list1[j]=temp

    print(list1)


#bubblesort(list)
