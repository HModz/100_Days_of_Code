from flask import Flask
from random import randint

app = Flask(__name__)
random_number = randint(1, 9)





@app.route('/')
def home():
    return '<h1> Guess a number between 0 and 9 </h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">' \

@app.route('/<int:number>')
def guess(number):
    if number == random_number:
        return '<h1 style="color:green"> CORRECT! </h1>'
    elif number < random_number:
        return '<h1 style="color:red"> TOO LOW! </h>'
    else:
        return '<h1 style="color:blue"> TOO HIGH! </h>'


if __name__ == "__main__":
    app.run(debug=True)
