                #  LIST


# LIST INTRO             
# lst=[1,2,4,4.9,"hello",[2,8]]
# print(lst)
# # a list stores all types of datatype. liist,dictionaries,int,strings etc.  
# # initialised with square brackets and has indexing


# APPEND
# lst=[1,2,4,4.9,"hello",[2,8]]
# #append( adds in at the last index & for single element )
# lst.append("apple")
# lst.append([2,3,4])
# print(lst)


# EXTEND
# lst=[1,2,4,4.9,"hello",[2,8]]
# # extend( adds element at the last index & for multiple elements )
# # lst.extend(2,5,6) #shows error
# lst.extend(["banana","watermelon","mango"])
# lst.extend("grapes")
# # lst.extend(5) shows error as integer is no iterable 
# print(lst) 
# #  each element in the list will be added like individaul elements



# INSERT
# lst=[1,2,4,4.9,"hello",[2,8]]
# #insert(index,value)
# lst.insert(2,100)
# print(lst)


# POP
# lst=[1,2,4,4.9,"hello",[2,8]]
# #pop() removes last element 
# lst.pop()
# #pop(index) removes element at the GIVEN INDEX
# lst.pop(4)
# print(lst)


# REMOVE
# lst=[1,2,3,6,7,2,3,1,10]
# # remove(value) the FIRST OCCURENCE OF THE VALUE will be removed
# lst.remove(10)
# lst.remove(6)
# lst.remove(3)
# print(lst)


# INDEX
# lst=[1,2,3,6,7,2,3,1,10]
# #index(value) return the index at thich the value is present & return the index of the first reoccurence
# print(lst.index(6))
# print(lst.index(3))


# COUNT
# lst=[1,2,3,6,7,2,3,1,10]
# #count(value) returns the frequency of that element in the list
# print(lst.count(6))
# print(lst.count(2))
# print(lst.count(100))


# SORT
# lst=[1,2,3,6,7,2,3,1,10]
# #sort() sorts based on the ASCII values
# print(lst.sort())
# sorted_list=lst.sort()
# print(sorted_list) 
# lst.sort()
# print(lst)


# SORTED{
# lst=[1,2,3,6,7,2,3,1,10]
# #sorted() first has to be stored
# print(lst)
# print(sorted(lst))
# print(lst)

# sorted_list=sorted(lst)
# print(sorted_list)
# }


# MAX()
# lst=[1,2,3,6,7,2,3,1,10]
# #max(list_name)
# # lst.max() gives error
# maximum=max(lst)
# print(maximum)


# MIN()
# lst=[1,2,3,6,7,2,3,1,10]
# #min(list_name)
# # lst.min() gives error
# minimum=min(lst)
# print(minimum)

# SUM()
# lst=[1,2,3,6,7,2,3,1,10]
# #sum(list_name)
# # lst.sum() gives error
# summation=sum(lst)
# print(summation)
                       


# #INPUTING IN A LIST
# size=int(input("Enter the size"))
# lis1=[]
# lis2=[]
# i=1
# while i<=size:
#   a=int(input())
#   lis1.append(a)
#   i=i+1
# print(lis1)
# i=1
# while i<=size:
#   b=int(input())
#   lis2.append(b)
#   i=i+1
# print(lis2)


# # TAKE 2 LISTS OF SAME LENGTH
# # ADD THE CONSECUTIVE INDICES AND ENTER THE VALUES IN A LIST
# lis1=[1,2,3]
# lis2=[4,3,2]
# lis3=[]
# i=0
# while i<3:
#   s=lis1[i]+lis2[i]
#   lis3.append(s)
#   i=i+1
# print(lis3)