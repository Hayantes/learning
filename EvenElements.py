def get_even_elements(given_list):
    even_numbers_list = [num for num in given_list if num % 2 ==0]
    return even_numbers_list
numbers = [1,4,9,16,25,36,49,64,81,100]
print(get_even_elements(numbers))   