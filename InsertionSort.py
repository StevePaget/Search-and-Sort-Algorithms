items = ["cat","bat","snake","frog","elephant","horse","dog"]

def InsertionSort(myItems):
    global counter
    for mainPointer in range(2, len(myItems)):
        temp = myItems[mainPointer]
        insertionPoint = mainPointer - 1
        while myItems[insertionPoint] > temp:
            counter = counter + 1
            myItems[insertionPoint+1] = myItems[insertionPoint]
            insertionPoint = insertionPoint -1
        myItems[insertionPoint+1] = temp
    return myItems
    
print("The unsorted list is:")
print(items)print()
counter = 0
print("The sorted list is:")
sortedItems = InsertionSort(items)
print (sortedItems)
print("I made", counter, "checks")
