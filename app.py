import joblib
import numpy as np
import streamlit as st

scaler = joblib.load("scaler.pkl")
model = joblib.load("model.pkl")

st.title("Churn Prediction App")
st.divider()
st.write("Please enter the values and hit the predict button for getting a prediction")
st.divider()

age = st.number_input("Enter Age", min_value=10, max_value=100, value=30)
tenure = st.number_input("Enter Tenure", min_value=0, max_value=130, value=10)
monthlycharges = st.number_input("Enter Monthly Charges", min_value=30, max_value=150)
gender = st.selectbox("Enter the Gender", ["Male", "Female"])

st.divider()

prediction = st.button("Predict!")

if prediction:
    gender_selected = 1 if gender=="Female" else 0
    X = [age, gender_selected, tenure, monthlycharges]
    X1 = np.array(X)
    X_array = scaler.transform([X1])
    prediction = model.predict(X_array)[0]
    predicted = 'Yes' if prediction == 1 else 'No'
    st.write(f"Predicted: {predicted}")

else:
    st.write("Please enter the values and use predict button")