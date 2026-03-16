from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

# Load model and columns
model = pickle.load(open("churn_model.pkl", "rb"))
model_columns = pickle.load(open("model_columns.pkl", "rb"))

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/predict", methods=["POST"])
def predict():

    try:

        input_data = {
            "SeniorCitizen": int(request.form["SeniorCitizen"]),
            "MonthlyCharges": float(request.form["MonthlyCharges"]),
            "TotalCharges": float(request.form["TotalCharges"]),
            "tenure": float(request.form["tenure"]),
            "gender": request.form["gender"],
            "Partner": request.form["Partner"],
            "Dependents": request.form["Dependents"],
            "PhoneService": request.form["PhoneService"],
            "MultipleLines": request.form["MultipleLines"],
            "InternetService": request.form["InternetService"],
            "OnlineSecurity": request.form["OnlineSecurity"],
            "OnlineBackup": request.form["OnlineBackup"],
            "DeviceProtection": request.form["DeviceProtection"],
            "TechSupport": request.form["TechSupport"],
            "StreamingTV": request.form["StreamingTV"],
            "StreamingMovies": request.form["StreamingMovies"],
            "Contract": request.form["Contract"],
            "PaperlessBilling": request.form["PaperlessBilling"],
            "PaymentMethod": request.form["PaymentMethod"]
        }

        df = pd.DataFrame([input_data])

        # Convert categorical to dummy variables
        df = pd.get_dummies(df)

        # Match training columns
        df = df.reindex(columns=model_columns, fill_value=0)

        prediction = model.predict(df)[0]
        probability = model.predict_proba(df)[0][1]

        if prediction == 1:
            result = f"Customer Will Churn (Probability: {probability:.2f})"
        else:
            result = f"Customer Will NOT Churn (Probability: {1-probability:.2f})"

        return render_template("home.html", prediction_text=result)

    except Exception as e:
        return render_template("home.html", prediction_text=f"Error: {str(e)}")


if __name__ == "__main__":
    app.run(debug=True)