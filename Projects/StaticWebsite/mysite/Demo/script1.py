
# importing the flask class object from the flask library
from flask import Flask, render_template

# create variable where you will store your flask application. Instatiate the class object
app = Flask(__name__)

#add decorator, where the URL where the page will be viewed. where the page will be viewed.
#Here, a "/" means the home page. Or you can change it to "/about/"
# just return a string to the website.
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about/')
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)


