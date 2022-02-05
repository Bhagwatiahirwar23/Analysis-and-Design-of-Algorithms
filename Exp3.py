#Q3. Modify the linear search procedure to get the frequency of an element present in random list of integers.
random_list = [1, 18, 2, 4, 15, 78, 83, 94, 2]
element = int(input("Enter element you want to search: "))

def find(element):
    frequency = 0
    for elm in random_list:
        if elm == element:
            frequency += 1 
    
    return frequency

if find(element):
    print(f"found element {find(element)} times!")                
else:
    print("element not in list!")    