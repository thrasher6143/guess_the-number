from flask import Flask
import random

app = Flask(__name__)



print('------------------------------')
print('------Guess the Number--------')
print('------------------------------')
print()

# the_number = random.randint(1, 100)
# guess = -1
# no_tries = 0
#
# while guess != the_number:
#     no_tries += 1
#     guess_text = input('Guess a number between 1 and 100:  ')
#     guess = int(guess_text)
#
#     if guess < the_number:
#         print('Your guess is too low')
#     elif guess > the_number:
#         print('Your guess is too high')
#     else:
#         print('Finally you win!!')
#
# print('It took you {no_tries} tries to guess the number')


@app.route('/api/guess/<int:num>')
def get_guess(num):
    if num < 1 or num > 100:
        return 'Bad Request: Number must be between 1 and 100', 400

    the_num = random.randint(1, 100)
    if num != the_num:
        return f'Sorry, the number was {the_num}.', 200
    else:
        return f'Great guess! {num} was the number', 200


if __name__ == '__main__':
    app.run()