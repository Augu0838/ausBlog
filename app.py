from flask import Flask, render_template

# create a flask instance -- Helps flask finde flies and folders
app = Flask(__name__)

# Create a route decorator
@app.route('/')

# def index():
#     return "<h1>Hello World!</h1>"

def index():
    first_name = "Auguste"
    return render_template("index.html", first_name = first_name)


# http://127.0.0.1:5000/user/John
@app.route('/user/<name>')

def user(name):
    return render_template("user.html", user_name=name)

@app.route('/login')

def login():
    return render_template("login.html")

# Create custom error pages

# invalid URL
@app.errorhandler(404)
def pagenotfound(e):
    return render_template("404.html"), 404

# internal server error
@app.errorhandler(500)
def pagenotfound(e):
    return render_template("500.html"), 500