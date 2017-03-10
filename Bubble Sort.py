items = ["cat","bat","snake","frog","elephant","horse","dog"]

def BubbleSort(myItems):  
    global counter
    swapped = True
    # The Outer loop
    while swapped == True:
        swapped = False
        # The Inner Loop
        for x in range(len(myItems)-1):
            counter = counter + 1
            if myItems[x] > myItems[x+1]:
                # if this item is bigger than the next one
                # we need to swap them
                temp = myItems[x]
                myItems[x] = myItems[x+1]
                myItems[x+1] = temp
                swapped = True
    return myItems

print("The unsorted list is:")
print(items)
print()
counter = 0
print("The sorted list is:")
sortedItems = BubbleSort(items)
print (sortedItems)
print("I made", counter, "checks")
