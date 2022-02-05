# Q1. Implement linear search to find an element in the given random list of integers

random_list = [1, 18, 2, 4, 15, 78, 83, 94, 2]
element = int(input("Enter element you want to search: "))

def find(element):
    for elm in random_list:
        if elm == element:
            return 1
    else:
        return 0

if find(element):
    print("element found!")                
else:
    print("element not in list!")    