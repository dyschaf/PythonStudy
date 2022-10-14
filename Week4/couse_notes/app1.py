from multiprocessing.reduction import duplicate


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
my_list2 = [num/2 for num in range(100, 5, - 1)
            if num % 2 == 0]
print(my_list2)
some_list = ["a", "b", "c", 'd', "b", "m", "n", "m", "m"]
duplicates = []

for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)
print(duplicates)
duplicates1 = list(set(x for x in some_list if some_list.count(x) > 1))
print(duplicates1)
simple_dict = {
    "a": 1,
    "b": 2
}
my_dict = {key: value**2 for key, value in simple_dict}
print(my_dict)
