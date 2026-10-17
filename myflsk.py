from flask import Flask

app = Flask("__name__")

@app.route("/")
def home():
    return "Welcome To The Flask Web World."


@app.route("/about")
def about():
    return "Welcome to About Us page."

@app.route("/contact")
def contact():
    return "Welcome to Contact page." 

@app.route("/user/<name>")
def user(name):
    return f"Welcome Mr. {name}." 

@app.route("/student/<name>/<course>")
def studenr(name,course):
    return f"{name} is learning {course} course." 

if __name__ == "__main__":
    app.run(debug=True)