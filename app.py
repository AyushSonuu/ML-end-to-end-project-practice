from flask import Flask, render_templete

app = Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():
    return "starting ml project"

@app.route("/x",methods=['GET','POST'])
def x():
    return render_templete(index.html)

if __name__ == "__main__":
    app.run(debug = True)