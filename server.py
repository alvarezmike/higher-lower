from flask import Flask
from random import randint

app = Flask(__name__)

GUESS_NUMBER = randint(0, 9)

# homepage with instructions of the game
@app.route('/')
def hello_world():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' alt='0-9 gif'>"

# check if number guessed is the right one
@app.route("/<int:check_number>")
def verify_number(check_number):
    if check_number == GUESS_NUMBER:
        return "<h1 style='color:green';>You found me</h1>" \
               "<iframe src='https://giphy.com/embed/O9zloGTTajAY0' width='480' " \
                "height='480' frameBorder='0' </iframe><p>" \
                "<a href='https://giphy.com/gifs/celebration-clapping-joker-O9zloGTTajAY0'>via GIPHY</a></p>"
    elif check_number < GUESS_NUMBER:
        return "<h1 style='color:blue';>Too low, try again</h1>" \
               "<iframe src='https://giphy.com/embed/3ohhwH6yMO7ED5xc7S' width='480'" \
               " height='270' frameBorder='0' ></iframe><p>" \
                "<a href='https://giphy.com/gifs/mlb-yankees-thumbs-down-3ohhwH6yMO7ED5xc7S'>via GIPHY</a></p>"
    else:
        return "<h1 style='color:purple';>Too high, try again</h1>" \
               "<iframe src='https://giphy.com/embed/3oz8xPQMrmfzAFB0IM' width='480'" \
               " height='330' frameBorder='0'></iframe><p>" \
               "<a href='https://giphy.com/gifs/ufc-3oz8xPQMrmfzAFB0IM'>via GIPHY</a></p>"


if __name__ == "__main__":
    # run the app in debug mode to auto-reload
    app.run(debug=True)