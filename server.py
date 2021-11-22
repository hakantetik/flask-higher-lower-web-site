from random import randint

from flask import Flask

app = Flask(__name__)


@app.route("/")
def greet():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"


@app.route("/<int:guessed_num>")
def return_page(guessed_num):
    number = randint(1, 9)
    if guessed_num < number:
        return "<h1 style='color: red'>You guessed Too Low!</h1>" \
               "<img src='https://media.giphy.com/media/3oKHWfu68Q6XOz2I6Y/giphy.gif'>"
    elif guessed_num > number:
        return "<h1 style='color: purple'>You guessed Too High!</h1>" \
               "<img src='https://media.giphy.com/media/2cei8MJiL2OWga5XoC/giphy.gif'>"
    elif guessed_num == number:
        return "<h1 style='color: green'>Correct Answer!</h1>" \
               "<img src='https://media.giphy.com/media/26tknCqiJrBQG6bxC/giphy.gif'>"


if __name__ == "__main__":
    app.run(debug=True)
