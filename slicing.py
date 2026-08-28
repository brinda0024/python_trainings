#In this one, I learnt about slicing in lists

list1 = [10, 20,30,40,50]

#syntax for slicing: list_name = [start: stop : step]
#stop one is not counted in the output.
# so, if we want first three elements than the stop will be '3', not '2'
#default is index 0 for start and index -1 or last element for stop

#for first three elements of the list
print(list1[0:3])

#indexing can be negative also. 
# The last element index will always be '-1', then second last element will be '-2', and so on.
print(list1[-1:])

#to get the reverse list (asked in interviews)
print(list1[::-1])

#for alternating elements
print(list1[0::2])