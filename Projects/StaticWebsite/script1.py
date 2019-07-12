
# importing the flask class object from the flask library
from flask import Flask

# create variable where you will store your flask application. Instatiate the class object
app = Flask(__name__)

#add decorator, where the URL where the page will be viewed. where the page will be viewed.
#Here, a "/" means the home page. Or you can change it to "/about/"
# just return a string to the website.
@app.route('/')
def home():
    return "Homepage content goes here!"

@app.route('/about/')
def about():
    return "About page content goes here!"

if __name__ == "__main__":
    app.run(debug=True)


