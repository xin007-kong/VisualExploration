from flask import Flask, render_template, request
from model import LinearRegressor
import numpy as np

app = Flask(__name__)

model = LinearRegressor()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    x_new = float(request.form["x_new"])
    y_new = model.predict(np.array([[x_new]]))
    return render_template("predict.html", x_new=x_new, y_new=y_new)


if __name__ == "__main__":
    # Load the data and train the model
    X = np.array([1, 2, 3, 4, 5]).reshape((-1, 1))
    y = np.array([2, 4, 6, 8, 10])
    model.fit(X, y)

    # Run the application
    app.run(debug=True)
