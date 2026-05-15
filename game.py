import random
secret_num = random.randint(1, 100)
count = 0
limit = 10
while count < limit :
    Guess = int(input('Guess : '))
    count += 1

    if Guess == secret_num:
        print('You are correct')
        break
    elif Guess < secret_num:
        if count < limit:
            print('Guess little higher')
    elif Guess > secret_num:
        if count < limit:
            print ('Guess little lower')

else:
        print('Sorry, You loose')
        print(f'{secret_num} was the number')