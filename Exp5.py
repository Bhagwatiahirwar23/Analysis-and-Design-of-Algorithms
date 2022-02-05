#Implement the insertion sort algorithm to sort given set of integer values in descending order.
def InsertionSort(Array):
    for index in range (1,len(Array)):
        current_element = Array[index]
        position = index
        while current_element > Array[position-1] and position > 0:
            Array[position] = Array[position-1]
            position = position-1
        Array[position] = current_element

Array = [4,7,9,2,1]
InsertionSort(Array)      # FUNCTION CALL
print(Array)

