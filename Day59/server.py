import os
from flask import Flask, render_template, request
import smtplib
import requests

to_email = os.environ["EMAIL"]
password = os.environ["PASSWORD"]

posts = requests.get("https://api.npoint.io/bdc08ef6aa4207b323e6", timeout=5).json()

app = Flask(__name__)


@app.route("/")
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=to_email, password=password)
            connection.sendmail(
                from_addr=email,
                to_addrs=to_email,
                msg=f"New 'contact me' message\n\n {name}\n{email}\n{phone}\n\n{message}",
            )
        return render_template(
            "contact.html", message="Successfully submitted your message. Have another?"
        )
    return render_template("contact.html", message="Contact me")


if __name__ == "__main__":
    app.run(port=8000, debug=True)
