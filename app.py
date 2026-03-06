from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("Rainfall.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    MinTemp = float(request.form.get("MinTemp"))
    MaxTemp = float(request.form.get("MaxTemp"))
    Rainfall = float(request.form.get("Rainfall"))
    Humidity3pm = float(request.form.get("Humidity3pm"))
    Pressure3pm = float(request.form.get("Pressure3pm"))

    sample = np.array([[MinTemp, MaxTemp, Rainfall, Humidity3pm, Pressure3pm]])
    prediction = model.predict(sample)[0]

    if prediction == 1:
        return render_template("chance.html")
    else:
        return render_template("noChance.html")

if __name__ == "__main__":
    app.run(debug=True)