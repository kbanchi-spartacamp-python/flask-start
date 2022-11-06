from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello Flask"


@app.route("/hiraizumi")
def hiraizumi():
    return "やっほーー、平泉町"


@app.route("/user/<name>")
def heyName(name):
    return name


@app.route("/user/<name>/<age>")
def heyAge(name, age):
    return name + age


# from flask import render_template
@app.route("/html")
def html():
    # return "<h1>Hello HTML</h1>"
    return render_template("index.html")


@app.route("/html/<name>")
def htmlName(name):
    return render_template("name.html", name=name)


@app.route("/html/age/<age>")
def htmlAge(age):
    return render_template("age.html", htmlAge=age)


# from flask import request
@app.route("/query")
def query():
    search_text = request.args.get("search_text")
    if search_text is not None:
        return search_text
    else:
        return ""


# http://127.0.0.1:5000/query?search_text=AAA

# http://127.0.0.1:5000/html

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5001)
