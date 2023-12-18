"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    #pass  # TODO: replace this line with your code
    for item in items:
        print(item)


def get_all_evens(nums):
    #pass  # TODO: replace this line with your code
    even_nums = []

    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)
    
    return even_nums


def get_odd_indices(items):
    #pass  # TODO: replace this line with your code
    odd_nums = []
    
    for i in range(len(items)):
        if i % 2 != 0:
            odd_nums.append(items[i])
    
    return odd_nums    
# print(get_odd_indices([1, 'hello', True, 500]))

def print_as_numbered_list(items):
    #pass  # TODO: replace this line with your code
    count = 1

    for item in items:
        print(f"{count}. {item}")

        count += 1
        
#come back and figure out how not to return None (we didn't have a return statement)
# print(print_as_numbered_list([1, 'hello', True]))

def get_range(start, stop):
    #pass  # TODO: replace this line with your code
    lst = []
    
    lst.append(start)

    for num in range(start, stop): #range(0, 5) return up to 4
        if num < stop: 
            lst.append(num + 1)
    
    return lst 
#print(get_range(0, 5))

def censor_vowels(word):
    pass  # TODO: replace this line with your code


def snake_to_camel(string):
    pass  # TODO: replace this line with your code


def longest_word_length(words):
    pass  # TODO: replace this line with your code


def truncate(string):
    pass  # TODO: replace this line with your code


def has_balanced_parens(string):
    pass  # TODO: replace this line with your code


def compress(string):
    pass  # TODO: replace this line with your code
