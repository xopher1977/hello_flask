from flask import Flask


def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper


def make_italic(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper


def make_underline(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper


app = Flask(__name__)


@app.route('/')
def hello_world():
    return "<h1 style='text-align: center'>Hello, world</h1>" \
           "<p>This is a paragraph</p>" \
           "<img src='https://media.giphy.com/media/tMiHhTLvQcavm/giphy.gif'>"


@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, you are {number} years old"


@app.route("/bye")
@make_bold
@make_italic
@make_underline
def bye():
    return "Bye!"


if __name__ == "__main__":
    app.run(debug=True)
