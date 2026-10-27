# integer = 10          # int
# floating = 3.14       # float
# string = "Hello"      # str
# boolean = True        # bool
# complex_num = 2 + 3j  # complex

# print(type(integer))
# print(type(floating))
# print(type(string))
# print(type(boolean))
# print(type(complex_num))

# print (type(integer))


# num_str = "123"
# num_int = int(num_str)    # ប្តូរពី str ទៅ int
# num_inkk = str(num_int)
# num_float = float(num_str) # ប្តូរពី str ទៅ float
# text = str(456)           # ប្តូរពី int ទៅ str

# print(num_int)
# print(num_float)
# print(text)
# print(num_inkk)





# name = input("បញ្ចូលឈ្មោះរបស់អ្នក: ")
# age = int(input("បញ្ចូលអាយុរបស់អ្នក: "))

# print(f"សួស្តី {name}! អ្នកមានអាយុ {age} ឆ្នាំ។")




# a = 10
# b = 3

# print(a + b)  # បូក
# print(a - b)  # ដក
# print(a * b)  # គុណ
# print(a / b)  # ចែក (លទ្ធផលជា float)
# print(a // b) # ចែកយកតែផ្នែកគត់
# print(a % b)  # យកសំណល់
# print(a ** b) # លើកកំពស់ (គុណ b ដង)





# x = 5
# y = 10

# print(x == y)  # ស្មើគ្នា
# print(x != y)  # មិនស្មើគ្នា
# print(x > y)   # ធំជាង
# print(x < y)   # តូចជាង
# print(x >= y)  # ធំជាងឬស្មើ
# print(x <= y)  # តូចជាងឬស្មើ








# a = True
# b = False

# print(a and b)  # ទាំងពីរត្រូវតែ True
# print(a or b)   # យ៉ាងហោចណាស់មួយ True
# print(not a)    # ប្តូរពី True ទៅ False ឬផ្ទុយមកវិញ







# x = 5  # binary: 0101
# y = 3  # binary: 0011

# print(x & y)   # AND (0101 & 0011 = 0001)
# print(x | y)   # OR (0101 | 0011 = 0111)
# print(x ^ y)   # XOR (0101 ^ 0011 = 0110)
# print(~x)      # NOT (~0101 = -0110)
# print(x << 1)  # Left shift (0101 << 1 = 1010)
# print(x >> 1)  # Right shift (0101 >> 1 = 0010)






# x = 10
# print(x)

# x += 5  # x = x + 5
# print(x)

# x -= 3  # x = x - 3
# print(x)

# x *= 2  # x = x * 2
# print(x)

# x /= 4  # x = x / 4
# print(x)






# #  Simple if Statement

# temperature = 30

# if temperature > 25:
#     print("អាកាសធាតុក្តៅណាស់")









# /// if-else Statement

# age = 18

# if age >= 18:
#     print("អ្នកជាមនុស្សពេញវ័យ")
# else:
#     print("អ្នកនៅតែជាអនីតិជន")







# /// if-elif-else Statement

# score = 75

# if score >= 90:
#     print("អ្នកបាននិទ្ទេស A")
# elif score >= 80:
#     print("អ្នកបាននិទ្ទេស B")
# elif score >= 70:
#     print("អ្នកបាននិទ្ទេស C")
# elif score >= 60:
#     print("អ្នកបាននិទ្ទេស D")
# else:
#     print("អ្នកបាននិទ្ទេស F")









# /// Nested if Statements - សេចក្តីបញ្ជា if ខាងក្នុង if

# score = 85

# if score >= 60:
#     print("អ្នកបានជាប់")
#     if score >= 80:
#         print("អបអរសាទរ! អ្នកបានពិន្ទុល្អណាស់")
# else:
#     print("អ្នកមិនបានជាប់ទេ")












# # ៊///  for Loop & while Loop - រង្វិលជុំ for និង while

# for i in range(5):
#      print(f"num ber : {i}")  #  0, 1, 2, 3, 4 តាមលំដាប់៖

# for i in range(1,6):  #  0, 1, 2, 3, 4  , 5
#      print (i)

# for i in range(1, 11, 2):   #ជាមួយជំហាន (step)
#     print(i)

# for i in range(1, 11):   # ប្រើ if ជាមួយ %
#     if i % 2 == 0:
#         print(i, "គូ")
#     else:
#         print(i, "សេស")

# for i in range(1, 4): # Nested loop គឺ loop នៅក្នុង loop
#     for j in range(1, 4):
#         print(i, "x", j, "=", i * j)

# for i in range(1, 5):  # គូររូប
#     print("*" * i)




# count = 10
# while count > -10:
#     print(f"ចំនួន: {count}")
#     count -= 1

# count = 0
# while count < 5:
#     print(f"ចំនួន: {count}")
#     count += 1

# fruits = ["ស្វាយ", "ចេក", "ក្រូច"]

# for fruit in fruits:
#     print("ខ្ញុំចូលចិត្ត", fruit)

# fruits = ["ស្វាយ", "ចេក", "ក្រូច"]
# print(len(fruits))



# Loop Control (break, continue, pass)
# for i in range(10):
#     if i == 5:
#         break  # បញ្ចប់រង្វិលជុំនៅ i = 5
#     if i == 3:
#         continue  # រំលង i = 3
#     if i == 7:
#         pass  # មិនធ្វើអ្វីទេ
#     print(f"លេខ: {i}")










#  // Defining & Calling Functions - ការកំណត់ និង ការហៅអនុគមន៍
# Functions ត្រូវបានកំណត់ដោយប្រើ def 
# def greet():
#     print("សួស្តី! ស្វាគមន៍មកកាន់ Python")

# greet()

# # Functions អាចទទួល parameters ដើម្បីធ្វើការជាមួយទិន្នន័យផ្សេងៗ
# def greet(name):
#     print("សួស្តី", name)

# greet("សុខា")
# greet("ដារា")

# def add(a, b):
#     return a + b

# result = add(3, 5)
# print(result)

# # រួមបញ្ចូលអ្វីដែលបានរៀន (loop, list, len)៖
# def average(numbers):
#     total = 0
#     for n in numbers:
#         total = total + n
#     return total / len(numbers)

# scores = [80, 65, 90, 45]
# print(average(scores))




# # ១.
# def square(x):
#     return x*x
# print(square(5))
# # 2
# def is_even(n):
#     if n % 2==0 :
#         return True
#     else:
#         return False
# print(is_even(10))


# Lambda Functions - អនុគមន៍ Lambda
# square = lambda x: x ** 2

# print(square(5))










# Importing Modules (Built-in & Custom) - ការនាំចូលម៉ូឌុល
# Modules អនុញ្ញាតឱ្យប្រើ functions និងកូដពីឯកសារផ្សេងទៀត។ 
# import math
# def say_hello():
#     print("ជម្រាបសួរ!")
# print(math.sqrt(16))





# 6. Data Structures - រចនាសម្ព័ន្ធទិន្នន័យ
# Lists (Dynamic Arrays) 
# fruits = ["ផ្លែប៉ោម", "ផ្លែចេក", "ផ្លែឪឡឹក"]
# fruits.append("ផ្លែស្ត្របឺរី")
# print(fruits)
# fruits[1] = "ផ្លែត្រសក់"
# print(fruits)

# # Tuples ស្រដៀងនឹង Lists ប៉ុន្តែមិនអាចផ្លាស់ប្តូរបាន (immutable) បន្ទាប់ពីកំណត់
# colors = ("ក្រហម", "ខៀវ", "លឿង")
# print(colors[0])
# # colors[0] = "បៃតង" # នឹងបណ្តាលឱ្យមានកំហុស


# # Sets (Unique Collections) 
# numbers = {1, 2, 3, 3, 4}
# numbers.add(5)
# print(numbers)

# Dictionaries (Key-Value Pairs)
# student = {"ឈ្មោះ": "សុខា", "អាយុ": 20, "ជំនាញ": "សរសេរកម្មវិធី"}
# student["អាយុ"] = 21
# student["សាលា"] = "សាកលវិទ្យាល័យ"
# print(student)

# student = {
#     "name": "sokxa",
#     "age": 20,
#     "score": 85
# }

# print(student["name"])
# print(student["age"])
# print(student["score"])

# # # បន្ថែម ចុល​និ ផ្លាសផ្តូ
# student["score"] = 90
# student["city"] = "ភ្នំពេញ"
# print(student)

# # ប្រើ loop ជាមួយ dictionary៖
# for key, value in student.items():
#     print(key, ":", value)

# for key in student:  # ot man value
#     print(key)


# students = [
#     {"name": "សុខា", "score": 85},
#     {"name": "ដារា", "score": 70},
#     {"name": "ចាន់ថា", "score": 55}
# ]

# for s in students:
#     print(s["name"], s["score"])


# students = [
#     {"name": "សុខា", "score": 85},
#     {"name": "ដារា", "score": 70}, 
#     {"name": "ចាន់ថា", "score": 55}
# ]

# print("name  score")
# for student in students:
#     print(f"{student['name']}  {student['score']}")

# import pandas as pd

# students = [
#     {"name": "សុខា", "score": 85},
#     {"name": "ដារា", "score": 70},
#     {"name": "ចាន់ថា", "score": 55}
# ]

# df = pd.DataFrame(students)
# print(df)

# print(df["score"].mean())   # មធ្យមភាគ → 70.0
# print(df["score"].max())    # ពិន្ទុខ្ពស់បំផុត → 85
# print(df["score"].min())    # ពិន្ទុទាបបំផុត → 55
# print(df["score"].sum())    # ផលបូក → 210

# print(df[df["score"] >= 65])

# df["pass"] = df["score"] >= 50
# print(df)



# # String
# text = "Hello Python"
# print(text.upper()) # ប្តូរទៅអក្សរធំទាំងអស់
# print(text.lower()) # ប្តូរទៅអក្សរតូចទាំងអស់
# print(text.replace("Python", "អ្នកសិក្សា")) # ជំនួសអក្សរមួយដោយអក្សរមួយទៀត
# print(text.split(" "))  #  បំបែកអក្សរទៅជាបញ្ជីដោយប្រើគម្លាត







# import re

# text = "ទូរស័ព្ទ: 012-345-6789, អ៊ីមែល: example@email.com"
# phone = re.search(r"\d{3}-\d{3}-\d{4}", text)
# email = re.search(r"[a-z]+@[a-z]+\.[a-z]+", text)

# print(phone.group())
# print(email.group())
# import pandas as pd
# df = pd.read_csv(r"D:\LEARN BROGRAMMING ALL\PYHTON\learn\sales.csv")

# print(df["product"][0])
# print(df["price"][1])
# print(df["price"].max())
# print(df["quantity"].sum())

# df["total"] = df["price"] * df["quantity"]
# print(df)
# print(df["total"].sum())
# print(df["total"].max())
# print(df.sort_values("total", ascending=False))
# print(df.groupby("category")["total"].sum())











# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_csv(r"D:\LEARN BROGRAMMING ALL\PYHTON\learn\sales.csv")
# df["total"] = df["price"] * df["quantity"]

# name= ["cofee" , "tea" , "cake"]
# sels= [1000, 37, 60]

# plt.bar(name, sels)       
# plt.show()













# # string

# tex = "you er"
# number=10
# pulity = 50

# print (tex)
# print (len(tex))           #[ចាប់ផ្តើម:ឈប់]
# print (tex[-1:0])
# print (tex[2:])
# print (tex.upper)
# print (tex.lower)
# print (tex.strip)
# print (tex.replace("hello " , "pyton"))
# print (tex.split)
# print ("you" in tex)
# print ("java" in tex)
# print (tex.startswith("java"))
# print (tex.endswith("you"))
# print (f"hello {tex} you lik me {len(tex)}")
# print (f"total {number + pulity}")
# print (f"total {number + pulity:.2f}")
# print (tex +" " + tex.supper)
# print ("--"*10)
# print ("--"*10)




#list 

# nums = [10, 20, 50, 60]

# print(nums[0])       # 10
# print(nums[-1])      # 50 (ចុងក្រោយ)
# print(nums[1:4])     # [20, 30, 40]
# print(nums[:2])      # [10, 20]
# print(nums[2:])      # [30, 40, 50]

# fruit =["apple" , "cake"]

# fruit.addend("cerry")      # បន្ថែមទៅចុង
# fruit.insert(0 ,"bubu")        # បញ្ចូលនៅទីតាំង 0
# fruit.removw("cake")          # លុបតាមតម្លៃ
# last = fruit.pop()          # យកចេញធាតុចុងក្រោយ ហើយផ្តល់តម្លៃនោះ
# print (fruit , last)
# print (sorted(nums))        # [45, 65, 80, 90] (list ថ្មី ពី ធំ តៅ ទូច)
# print (sorted(nums , reverse=True))        # [90, 80, 65, 45]
# print (min(nums) , max(nums) , sum(nums))        
# print (len(nums))        
# print (10 in nums)        
# print (100 in nums)        

# for i, fruit in enumerate(fruit):
#     print (i , fruit)

# point = (10, 20)
# print(point[0])      # 10
# # point[0] = 99      # error! tuple កែមិនបាន

# a=  {"cake" , "ber" , "donat"}
# b= {"pink" , "blue" }

# print (a & b)   # {'តែ'} (មានទាំងពីរ)
# print (a | b)   # ទាំងអស់បញ្ចូលគ្នា
# print (a - b)    # មានក្នុង a តែគ្មានក្នុង b










# # អាន/សរសេរឯកសារ និង import
# with open("notes.txt", "w", encoding="utf-8") as f:
#     f.write("Python\n")
#     f.write(" love you \n")

# with open("notes.txt", "r", encoding="utf-8") as f:
#     content = f.read()        # អានទាំងអស់ជា string មួយ
#     print(content)
#     for line in f:
#         print (line.strip)
#     line = f.readline()
#     print (len(line))

