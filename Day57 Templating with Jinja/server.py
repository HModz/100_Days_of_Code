from flask import Flask
from flask import render_template
import random
import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    current_year = datetime.datetime.today().year
    random_number = random.randint(1, 10)
    return render_template("index.html", num=random_number, year=current_year)

@app.route('/guess/<name>')
def guess(name):
    params = {
        "name": name
    }
    response = requests.get("https://api.agify.io", params=params)
    age = response.json()["age"]
    response = requests.get("https://api.genderize.io", params=params)
    gender = response.json()["gender"]
    return render_template("guess.html", name=name, age=age, gender=gender)

@app.route('/blog')
def get_blog():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)