# Q2. Modify the linear search procedure to know the different position of an element .(Assume the element can occur more than on place.)

random_list = [1, 18, 2, 4, 15, 78, 83, 94, 2]
element = int(input("Enter element you want to search: "))

def find(element):
    positions = []
    for indx, elm in enumerate(random_list):
        if elm == element:
            positions.append(indx)
    return positions
        
if find(element):
    print("element found in postions: ", find(element))                
else:
    print("element not in list!")    