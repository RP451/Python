import random


length = int(input("Enter the lenght of array "))
list = []


for i in range(length):
        list.append(random.randint(1,1000))  

list.sort()

search_term = input("Enter number to be searched between 1 and 1000")
first_index = 0
last_index = len(list) - 1

def binary_search(list,search_term,first_index,last_index):
        mid_index = (first_index+last_index)//2
        mid_element = list[mid_index]

        if mid_element == search_term:
                return f"{}"