from flask import Flask, render_template
import requests

response = requests.get(url="https://api.npoint.io/f0fd5241a70832694e38")
response.raise_for_status()

blogs = response.json()


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", blogs=blogs)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/post/<int:index>')
def post(index):
    requested_post = None
    for blog in blogs:
        if blog["id"] == index:
            requested_post = blog

    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)