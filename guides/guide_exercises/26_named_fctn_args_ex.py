#Coding Exercise

#Behind the scenes of the code test is a function called sequence that accepts 5 arguments: first, second, third, fourth, and fifth. Unfortunately, they are not in sequential order. Using named arguments, call the sequence function and pass in the 5 arguments, setting their values to 1, 2, 3, 4, 5 respectively.

def sequence(third , fifth, first, fourth, second):
    return first, second, third, fourth, fifth
print(sequence( first = 1 , second = 2, third = 3, fourth = 4, fifth = 5 ))

# def named_arguments_practice(third, fifth, first, fourth, second):
#     def sequence():
#         return first, second, third, fourth, fifth  
#     print(sequence())

# named_arguments_practice(first = 1, second = 2, third = 3, fourth = 4, fifth = 5)



