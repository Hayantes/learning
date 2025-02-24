import random

def get_common_elements(list_1, list_2):
    # Use a list comprehension to find common elements
    print(list_1)
    print(list_2)
    common_elements = [element for element in list_1 if element in list_2]
    return common_elements


list_1 =[random.randint(1,100) for i in range(10)]
list_2 =[random.randint(1,100) for d in range(10)]



common_elements = get_common_elements(list_1, list_2)
print(common_elements)  # Output: [1, 1, 2, 3, 5, 8, 13]

