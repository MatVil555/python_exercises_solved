# Task 1--
def average(a, b):     return (a+b)/2

# Task 2--
#def reverse_list(input_list): input_list: input_list[::-1]
reverse_list = lambda input_list: input_list[::-1] #lambda function, equivalent to the previous line


# Task 3--
def sort_numbers_descending(number_list):
    number_list.sort(reverse=True)
    return number_list


# Task 4--
def add_indices(string_list):
    new_list = []
    n=1
    for lett in string_list:
        new_list.append(str(n)+'. '+lett)
        n += 1
    return new_list


# Task 5--
def capitalize_last_letter_in_each_word(string):
    output=[]
    for i in range(len(string.split())):
        output.append(string.split()[i][:-1]+string.split()[i][-1].capitalize())
    return ' '.join(output)


# Task 6--
def element_wise_merge(list1, list2):
    new_list = [ a +' '+ b for a,b in zip(list1,list2)]
    return new_list

    """
    Function that performs element-wise merge of list elements, inserting blank space in between
    :param list1: list of string
    :param list2: list of strings of the same length as list1
    :return: new list of merged strings
    """


# Task 7--
def execute_safely(operator, a, b):
    try:
        int(operator(a,b)) #also works for results that are floats
        return operator(a,b)
    except:
        return -1
    """
    Function that executes operator on arguments (a, b) -- or returns -1
    :param operator: some real-valued function, taking on input two real arguments
    :param a: a real number
    :param b: a real number
    :return: operator evaluated on (a,b) -- or -1 if this operation would be illegal
    """

