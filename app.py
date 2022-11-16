from flask import Flask, render_template

app = Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():
    return "hi amit bhai how are you"

if __name__ == "__main__":
    app.run(debug = True)
