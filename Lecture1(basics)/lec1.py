# print("Hello World")


# SUM OF NUMBERS (AS INT)
    # a=int(input())
    # b=int(input())
    # c=int(input())
    # print(a+b+c)


# SUM OF NUMBERS (AS STRING)
    # a=input()
    # b=input()
    # c=input()
    # print(a+b+c)


# SWAP NUMBERS(METHOD 1)
    # a=int(input())
    # b=int(input())
    # b=a+b-a
    # print(b)
    # b=a+b-b
    # print(b)


# SWAP NUMBERS(METHOD 2)
    # a=int(input())
    # b=int(input())
    # a=a+b
    # b=a-b
    # a=a-b
    # print(a,b)


# PRINT EVEN NUMBERS UPTO 50 THEN ODD NUMBERS UPTO 50 (WITH CONDITIONAL STATEMENTS ONLY)
    # i = 0
    # j=1
    # while i <= 50:
    #     if (j==1):
    #         if i % 2 == 0:
    #             print(i)

    #         if i == 50:
    #             j=2
    #             i = 0
    #     else:
    #         if i % 2 != 0:
    #             print(i)
    #     i += 1


# USE OF ELIF
    # a=input()
    # a=a.lower()
    # if (a=="mon"):
    #   print("MONDAY")
    # elif(a=="tue"):
    #   print("TUESDAY")
    # elif(a=="wed"):
    #   print("WEDNESDAY")
    # elif(a=="thu"):
    #   print("THURSDAY")
    # elif(a=="fri"):
    #   print("FRIDAY")
    # elif(a=="sat"):
    #   print("SATURDAY")
    # else:
    #   print("SUNDAY")


# USE OF FOR LOOP
    # for i in range(1,10,2):
    #     print(i,"odd")


# USE OF WHILE LOOP
    # a=1
    # while a<10:
    #   print(a)
    #   a=a+1


# OPERATORS
    # /----> gives deciaml values 
    # //----> gives int values
    # *----> multiplication
    # **-----> exponential multiplication (a=5 and b=2; a**b=25)


# PALINDROME CHECK (METHOD 1)
    # a=input()
    # reverse_a= a[::-1]
    # if(a==reverse_a):
    # print("PALINDROME")
    # else:
    # print("NOT PALINDROME")


# PALINDROME CHECK (METHOD 2)
    # s=input()
    # a=len(s)
    # i=0
    # j=len(s)-1
    # y=0
    # while y<=a//2:
    # if(s[i]==s[j]):

    #     i=i+1
    #     j=j-1
    #     flag="PALINDROME"
    # else:
    #     flag="NOT PALINDROME"
    # y=y+1

    # print(flag)