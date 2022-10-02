number = input("give me a number 1-100: ")
if int(number) % 3 == 0:
    print('Fizz')
elif int(number) % 5 == 0:
    print('Buzz')
elif int(number) % 5 == 0 and int(number) % 3 == 0:
    print('fizzbuzz')
