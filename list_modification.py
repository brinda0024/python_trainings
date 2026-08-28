#in this one, i leart about lst modifcation since lists are mutable

list2 = ["Mercedes", "Volvo", "Tesla" ,"Volkswagen"]

#to modify only one element of a index
list2[2] = "BMW"
print(list2)

#to add an element, we use append() method which adds elements in the end of the list
list2.append("Maserati")
print(list2)

#to remove an element, we use remove() method
#if there are two elements of same name then, remove() method will remove the first occurance
list2.remove("Volvo")
print(list2)

#to add multiple elements or another list, we use extend() method
list3 = ["Lamborghini", "Ford", "Nissan", "Koenigsegg"]
list2.extend(list3)
print(list2)

#to insert element in a specific location, we use insert() method
list2.insert(3, "Hyundai")
print(list2)

#to reverse the list
list2.reverse()
print(list2)

#to clear the list
list2.clear()
print(list2)

