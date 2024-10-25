user_req = input('what you what to do + - * / ')

num1 = float(input('Enter first number you want calculate '))

num2 = float(input('Enter second number you want calculate '))

if user_req == '+':
        result = num1 + num2
        print(result)
elif user_req == '-':
        result2 = num1 - num2
        print(result2)
elif user_req == '*':
    result3 = num1 * num2
    print(result3)

elif user_req == '/':
    result4 = num1 / num2
    print(result4)

else:
    if user_req:
        print(f'the the number {user_req}you enter is wrong')


