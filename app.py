from flask import Flask, render_template, request
import pickle
import pandas as pd
import os

app = Flask(__name__)

# Load model
MODEL_PATH = "advertisingmodel.pkl"

if os.path.exists(MODEL_PATH):
    print("file exist")
    model = pickle.load(open(MODEL_PATH, "rb"))
else:
    print("file not exist")

# Home page
@app.route("/")
def index():
    return render_template("index.html")

# Prediction route
@app.route("/predict", methods=["POST"])
def predict():
    sy0 = float(request.form["s0"])
    sy1 = float(request.form["s1"])
    sy2 = float(request.form["s2"])

    features = pd.DataFrame(
        [[sy0, sy1, sy2]],
        columns=[
            "TV Ad Budget ($)",
            "Radio Ad Budget ($)",
            "Newspaper Ad Budget ($)"
        ]
    )

    pred = round(model.predict(features).ravel()[0], 2)


    return render_template("result.html", data=pred)

if __name__ == "__main__":
    app.run(debug=True)
