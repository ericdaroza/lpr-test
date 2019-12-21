from random import randint

vetor_num = [81, 405, 189, 135, 297, 459, 783, 279, 684]
mdc = 0

# for i in range(6):
#     vetor_num.append(randint(1, 10000))

vetor_num.sort()
print("---------------------")
for value in range(1, vetor_num[0] + 1):
    null_div = 0
    print("Division by {}:".format(value))

    for number in vetor_num:
        null_div += (number % value)
        print("{} % {} = {}".format(number, value, (number % value)))

    print("---------------------")
    if null_div == 0:
        mdc = value

print(vetor_num)
print("The greatest common divisor is {}".format(mdc))
