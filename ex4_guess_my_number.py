import random

answer = random.randint(1,1000)

while True:

    userinput = input('Enter a Number from 1-1000')
    userinput = int(userinput)

    print(f'You have entered {userinput}')

    if userinput == answer:
        print('Correct!')
        break
    elif userinput > answer:
        print("Too Big!")
    else:
        print('Too small!')