#                                               TASK 1 TABLR USER INPUT

# a = int(input("Please Enter The value For Table "))
# for i in  range(1,11):
#     print(f"{a} x {i}= {a*i}")

#                                             TASK 2 Random Number
# import random
# print("*"*5,"Ranom Number","*"*5)
# rnd1 = int(input("please enter your starter number: "))
# rnd2 = int(input("please enter your end number: "))

# print(random.randint(rnd1,rnd2))

# rnd_list = []
# rnd_list.append(random.randint(rnd1,rnd2))
# for i in range(rnd1,rnd2):
#     num = random.randint(rnd1,rnd2)
#     rnd_list.append(num)
# print("\nRandom Number List: ",rnd_list)

#                                               How to get Max Number
        
# import random
# rnd1 = int(input("please enter your starter number: "))
# rnd2 = int(input("please enter your end number: "))
# rnd_list = []
# rnd_list.append(random.randint(rnd1,rnd2))
# for i in range(rnd1,rnd2):
#     num = random.randint(rnd1,rnd2)
#     rnd_list.append(num)
# print("\nRandom Number List: ",rnd_list)
# maxNum = max(rnd_list)
# print("Maximum Number is :",maxNum)


 #                                              How to get Mini Number
        
# import random
# rnd1 = int(input("please enter your starter number: "))
# rnd2 = int(input("please enter your end number: "))
# rnd_list = []
# rnd_list.append(random.randint(rnd1,rnd2))
# for i in range(rnd1,rnd2):
#     num = random.randint(rnd1,rnd2)
#     rnd_list.append(num)
# print("\nRandom Number List: ",rnd_list)
# miniNum = min(rnd_list)
# print("Minimum Number is :",miniNum)

#                                            TASK3 If you want to check which number has come how much.


# import random
# rnd1 = int(input("please enter your starter number: "))
# rnd2 = int(input("please enter your end number: "))
# rnd_list = []
# rnd_list.append(random.randint(rnd1,rnd2))
# for i in range(rnd1,rnd2):
#     num = random.randint(rnd1,rnd2)
#     rnd_list.append(num)
# print("\nRandom Number List: ",rnd_list)
# print ("\n\nIf you want to check which number has come how much:")
# rnd3 = int(input("\nplease enter your  number: "))
# numCount = rnd_list.count(rnd3)
# print(f"Your Value {numCount} Times")

#                                               TASK4 Sum Of Number List

# print("\n","*"*5,"Sum Of Number List","*"*5)
# import random
# rnd1 = int(input("please enter your starter number: "))
# rnd2 = int(input("please enter your end number: "))
# rnd_list = []
# rnd_list.append(random.randint(rnd1,rnd2))
# for i in range(rnd1,rnd2):
#     num = random.randint(rnd1,rnd2)
#     rnd_list.append(num)
# print("\nRandom Number List: ",rnd_list)
# sum_list = 0
# for i in range(len(rnd_list)):
#     sum_list = sum_list + rnd_list[i]
# print("\nSum Of Value: ",sum_list)

#                                           check the common numbers b/w two lists.

# import random

# lst1 = []
# lst2 = []
# lst3 = []
# rnd1 = int(input("Enter the random starting number "))
# rnd2 = int(input("Enter the random ending number "))
# lst1.append(random.randint(rnd1,rnd2))
# for i in range(rnd1,rnd2):
#     num = random.randint(rnd1,rnd2)
#     lst1.append(num)
# rnd1 = int(input("Enter the random starting number for the 2nd list "))
# rnd2 = int(input("Enter the random ending numberfor the 2nd list "))
# lst2.append(random.randint(rnd1,rnd2))
# for i in range(rnd1,rnd2):
#     num = random.randint(rnd1,rnd2)
#     lst2.append(num)
# print("\nRandom Number List1: ",lst1)
# print("\nRandom Number List2: ",lst2)
# for i in lst1:
#     if i in lst2:
#         lst3.append(i)
# print("The common elements are: ",lst3)

#                               check how many times a particular character is repeated in that text

# chList = []
# chrt = input("Enter the Word: ")
# for data in chrt:
#     if data not in chList:
#         chList.append(data)
# for data2 in chList:
#     print(data2,chrt.count(data2),"Times")         