


#                                           Binary Search 
#           EXAMPLE: Finding the position of a number from a List of length 5. 

#           Storing a Sequence of Elements in an Array
my_list = [1,3,5,7,9]
# NOTE: Binary Search only works when the List is in sorted order. 

def binary_search(list,item):

#           Determining the Part of the List that We'll Search In
# Beginning of the List   
    low = 0
# End of the List 
    high = len(list)-1

    while low <= high:
# NOTE: While you haven't narrowed it down to one elemenent... 
        mid = int((low + high) / 2)
# NOTE: "mid" is rounded down by Python automatically if isn't an even number. 
        guess = list[mid]

# Founding the Item 
        if guess == item:
            return mid 

# When Guess is Too High 
        if guess > item:
            high = mid - 1
        else:

# When Guess is Too Low 
            low = mid + 1

# When the Item doesn't Exist 
    return None 

print(binary_search(my_list,3))
print(binary_search(my_list,9))
print(binary_search(my_list,-1))

