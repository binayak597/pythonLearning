myList = [1, 2, 9, 5, 3, 5]

# traditional way


# squaredList = []
# for item in myList:
#     squaredList.append(item*item)

# same operation with list comprehension

squaredList = [i*i for i in myList]

print(squaredList)

# traditional way

# checkedList = []

# for item in myList:
#     if item < 8:
#         checkedList.append(item)

# print(checkedList)

# same operation with list comprehension

checkedList = [item for item in myList if item < 8]

print(checkedList)