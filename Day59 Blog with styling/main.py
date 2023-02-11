from flask import Flask
from flask import render_template
from flask import request
import requests

app = Flask(__name__)

blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
all_blogs = requests.get(blog_url).json()

@app.route('/')
def main():
    return render_template('index.html', blog_posts=all_blogs)

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/post/<int:id>')
def get_post(id):
    return render_template('post.html', blog_posts=all_blogs, num=id)

@app.route('/form-entry', methods=["POST"])
def receive_data():
    data = request.form
    print(data["name"])
    print(data["email"])
    print(data["phone"])
    print(data["message"])
    return "<h1>Succesfully sent message</h1>"



if __name__ == "__main__":
    app.run(debug=True)
