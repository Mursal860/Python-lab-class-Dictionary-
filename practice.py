
# //practiced positive and negative indexing

# text="Data sience"
# print(text[0])
# print(text[-1])
# print(len(text))
# print(text.lower())


# //Lists are ordered, mutable collections.

# numbers=[1, 2, 3, 4]
# numbers.append(5)
# print(len(numbers))
# print(numbers)
# numbers[4]=6
# print(numbers)


# // Dictionaries; they are mutable and maybe not orderd and they store datas as key and values.
# Regestration={
#     "STU_Name":["Mursal","Horya"],
#     "STU_Id":["222280", "222196"],
#     "STU_Major":["Computer Science","Public Health"],

# }
# print(Regestration["STU_Name"])
# print(Regestration["STU_Id"])
# print(Regestration["STU_Major"])

  # How to use dictionaries to print a collumn of same data?

Regestration=[
     ['Names':"Mursal","IDs":"222280", "Major": "Computer Science"],
     ["Names": "Horya","IDs":"222196", "Major":"Public Health"],
     ["Names", "Somaya","IDs":"123456", "Major":"Economics"]
]



ID= [I["IDs"] for I in Regestration]
print(IDs)

