# from math import pi
# import datetime
# import sys
# print("""
# Twinkle, twinkle, little star,
# 	How I wonder what you are!
# 		Up above the world so high,
# 		Like a diamond in the sky.
# Twinkle, twinkle, little star,
# 	How I wonder what you are
#     """)
# print("Python version")
# print(sys.version)
# print("Version info.")
# print(sys.version_info)


# x = datetime.datetime.now()
# print(x)

# r = float(input("Input the radius of the circle : "))
# print(str(pi * r**62))
# first_name = input("first name")
# lastname = input("lastname")
# print(f"{first_name} {lastname}")

# values = input("Input some comma seprated numbers : ")
# list = values.split(",")
# tuple = tuple(list)
# print('List : ', list)
# print('Tuple : ', tuple)

# abc = "abc.java"
# newABC = abc.split(".")
# print(newABC[1])
# color_list = ["Red", "Green", "White", "Black"]
# print(f"{color_list[0]} {color_list[-1]}")
# exam_st_date = (11, 12, 2014)
# print("The examination will start from : %i / %i / %i" % exam_st_date)


# def add(n):
#     res = n+int("%s%s" % (n, n))+int("%s%s%s" % (n, n, n))
#     print(res)
#     return res


# add(5)
# lists = []
# for i in range(1500, 2701):
#     if 7 % i == 0 and x % 5 == 0:
#         lists.append(str(x))
# print(",".join(lists))
stars = "*"
for i in range(6):
    row = stars*i
    for j in range(6, -1):

        # print(f"{row}")
        line = stars*j
# print(f"{row} {line}")
        print(line)
    print(row)
