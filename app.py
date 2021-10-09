from flask import Flask,render_template,request,redirect,url_for
from wikiContent import get_content_from_wikipedia
app = Flask(__name__)



@app.route("/",methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/",methods=["POST"])
def scrapped():
    search_key = request.form["search"]
    data = get_content_from_wikipedia(search_key)
    return render_template("index.html",data=data)


if __name__ == '__main__':
    app.run(debug=True)