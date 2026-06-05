# def function_name(parameters):
#   #body


# def multiplication(a,b):
#   return a*b
# print(multiplication(10,5))
# result=multiplication(10,3)
# print(result)


# LAMBDA FUNCTION - This function is used to create one liner functions. It helps to avoid the use of "def" again and again.


# lamda function declaration:
# lamda arguments:expression
# can take multiple arguments but takes only one expression


# add_two_numbers=lambda a,b:a+b
# print(add_two_numbers(20,5))


#remove spaces.            strip(removes spaces from both sides),lstrip(from left),rstrip(from right)
#split text.               split()
#join text.                join()
#replce text               replace()
#change case.              lower(),upper(),title(),capitalise
#find text                 find() find index(-1 if not found)
#check text.               startswith(),endswith()
#count values.             count()
#length                    len()
#sort chairs               sorted()


# str="       HeLLo        "
# print(str)
# print(str.strip())
# print(str.lstrip())
# print(str.rstrip())


# str="HeLLo mY namE IS Kavya"
# print(str)
# print(str.split())


# letters = ["P", "Y", "T", "H", "O", "N"]
# print("".join(letters))

# fruits = ["Apple", "Mango", "Banana"]
# print(" ".join(fruits))
# print("!".join(fruits))
# print("ab ".join(fruits))


# str="HeLLo mY namE IS Kavya"
# print(str)
# print(str.replace("HeLLo","Hi"))


# str="HeLLo mY namE IS Kavya"
# print(str)
# print(str.lower(),"-LOWERCASE")
# print(str.upper(),"-UPPERCASE")
# print(str.title(),"-TITLE")
# print(str.capitalize(),"-CAPITALISE")


# str="HeLLo mY namE IS Kavya"
# print(str)
# print(str.find("Hello"))
# print(str.find("mY"))


# str="HeLLo mY namE IS Kavya"
# print(str)
# print(str.startswith("HeLLo"))
# print(str.startswith("Hello"))
# print(str.endswith("HeLLo"))
# print(str.endswith("Kavya"))


# letters = ["P", "Y", "T", "H", "O", "N","P","Y"]
# print(letters.count("P"))


# letters = ["P", "Y", "T", "H", "O", "N","P","Y"]
# print(len(letters))
# str="HeLLo mY namE IS Kavya"
# print(len(str))


# letters = ["P", "Y", "T", "H", "O", "N","P","Y"]
# print(sorted(letters))
# str="HeLLo mY namE IS Kavya"
# print(sorted(str))


# first_name='    anshika   '
# second_name='gupta   '
# #strip
# first_name=first_name.rstrip()
# print(first_name)
# second_name=second_name.rstrip()
# print(second_name)
# str2=first_name+second_name
# str3=first_name+' '+second_name
# print(str2)
# print(str3)


# s="hello world"
# print(s)
# print(s[7:11])
# print(s[:5])
