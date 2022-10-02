my_list = [1, 2, 3]


def multiply_by2(item):
    return item*2


print(list(map(multiply_by2, my_list)))
print(my_list)

my_list = []
for letter in "dovid":
    my_list.append(letter)
print(my_list)

my_list1 = [letter for letter in "hello"]
print(my_list)
my_list2 = [num for num in range(0, 100)]
print(my_list2)
