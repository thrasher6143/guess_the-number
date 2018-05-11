import random

print('------------------------------')
print('------Guess the Number--------')
print('------------------------------')
print()

the_number = random.randint(1, 100)
guess = -1
no_tries = 0

while guess != the_number:
    no_tries += 1
    guess_text = input('Guess a number between 1 and 100:  ')
    guess = int(guess_text)

    if guess < the_number:
        print('Your guess is too low')
    elif guess > the_number:
        print('Your guess is too high')
    else:
        print('Finally you win!!')

print(f'It took you {no_tries} tries to guess the number');
