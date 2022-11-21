from flask import Flask, render_template
from housing.logger import logging
import sys
from housing.exception import HousingException
app = Flask(__name__)
import PyYAML


@app.route("/",methods=['GET','POST'])
def index():
    try:
        raise Exception("we are testing custom exception")
    except Exception as e:
        housing = HousingException(e,sys)
        logging.info(housing.error_messsage)
        logging.info("we are testing logging module")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug = True)
