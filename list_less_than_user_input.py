#there is list of random numbers and we need to take user input 
#Then according to that user input, we create another list and print those elements less than user input

a = [1,2,5,6,9,7,8,3,4,2,6,3,4,5,8,7,6,9,7]
b = []

User_input = int(input("Enter the number which you want the list to be less than of: "))

for elements in a:
    if elements < User_input:
        b.append(elements)

print(b)
