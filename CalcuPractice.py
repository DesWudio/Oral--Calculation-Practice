import random

# DesWudio, 20211017
# 我因为连着算错了多个两位数的加减法问题而做错了多道题目
# 故编写了这样一个程序来提升我基本无可救药的两位数加减法水平
# 希望它有用


def Additionandsubtraction(count):
    num1 = random.randint(0, count)
    num2 = random.randint(-1*count, count)
    correct = num1 + num2
    if(correct < 0 or correct > count):
        return 0
    if(num2 > 0):
        print('Q: %s + %s = ?' % (num1, num2))
    else:
        print('Q: %s - %s = ?' % (num1, num2*-1))
    correct = num1 + num2
    A = input('A: ')
    if A == str(correct):
        print('Good job!')
    else:
        print('Wrong answer!')
        print('Might be: %s' % correct)
    return 1

count = input('Digits: ') # 在输入结果(例如十以内输入1，百以内输入2)
count = 10**(int(count))
while True:
    A = Additionandsubtraction(count)
