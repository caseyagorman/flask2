"""A madlib game that compliments its users."""
from pprint import pprint
from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    return render_template("greet.html",
                           person=player,)


@app.route('/play_game')
def play_game():
    """Plays game."""

    game_response = request.args.get("play")
    if game_response == "no":
        return render_template("goodbye.html")
    else: 
        return render_template("play_game.html")
                

@app.route('/madlibs')
def show_madlib():
    color = request.args.get("color")
    noun = request.args.get("noun")
    person = request.args.get("person")
    adjective = request.args.get("adjective")
    return render_template("madlibs.html",
    color=color,
    noun=noun,
    person=person,
    adjective=adjective)

if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)