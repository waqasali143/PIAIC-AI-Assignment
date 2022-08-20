#                               COUNT EACH CHARACTER 

# chList = []
# chrt = input("Enter the Word: ")
# for data in chrt:
#     if data not in chList:
#         chList.append(data)
# for data2 in chList:
#     print(data2,chrt.count(data2),"Times")


#                        COUNT VOWELS AND CONSONANT IN YOUR MESSAGE 

# sent = input("Enter the message : ").casefold()
# vowCount = 0
# cons = 0
# vowList = ["a","e","i","o","u"]
# for i in sent:
#     if i in vowList:
#         vowCount = vowCount+1
# msgLen = sent.__len__()
# cons = msgLen-vowCount
# print(f"Vowel Letter are {vowCount} Your Given Message.")
# print(f"Consonant are {cons} Your Given Message.")

#                           PRINT TRIANGLE WITH DIGIT

# num = int(input("Enter the number for number triangle "))
# num2 = 1
# for i in range(num):
#     for y in range(i+1):
#         print(num2,end=" ")
#         num2 = num2+1
#     print()    

#                           PRINT TRIANGLE WITH DIGIT

# a = int(input("Please Enter The value 1 : "))
# b = int(input("Please Enter The Second value : "))
# if a==1 and b>1:
#     for i in  range(a,b):
#         for y in range(i+1):
#             print(y,end=" ")
#         print()  
# else:
#     print("Your First Value Is Wrong")

