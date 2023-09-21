from flask import Flask, request, render_template, url_for
import pandas as pd
import pickle
# import joblib


# Declare a Flask app
app = Flask(__name__)

# Main function here
# ------------------
@app.route("/")
def home():
    return render_template("index test2.html")

# Running the app
if __name__ == '__main__':
	# app.jinja_env.auto_reload = True
	# app.config['TEMPLATES_AUTO_RELOAD'] = True
	# app.jinja_env.cache = None
	app.run(debug = True)
