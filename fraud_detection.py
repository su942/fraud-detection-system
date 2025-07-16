import streamlit as st
import pandas as pd
import joblib
import urllib.request


url = "https://your-link-to/fraud_detection_pipeline.pkl"
urllib.request.urlretrieve(url, "fraud_detection_pipeline.pkl")


model = joblib.load("fraud_detection_pipeline.pkl")

st.title("FRaud Detection  Prediction App")

st.markdown("Please enter the transaction detailes and use the predict button")

st.divider()

transaction_type = st.selectbox("Transaction Type", ["PAYMENT","TRANSFER","CASH_OUT","DEPOSIT"])
amount = st.number_input("Amount",min_value=0.0, value=1000.0)
oldbalanceOrg = st.number_input("Old Balance (sender)" ,min_value=0.0,value=1000.0)
newbalanceOrig =st.number_input("New Balance (sender)" ,min_value=0.0,value=9000.0)
oldbalanceDest = st.number_input("Old Balance (Receiver)" ,min_value=0.0,value=0.0)
newbalanceDest = st.number_input("New Balance (Receiver)" ,min_value=0.0,value=0.0)\

if st.button("Predict"):
    input_data = pd.DataFrame([{
        "type": transaction_type,
        "amount" : amount,
        "oldbalanceOrg" : oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest
    }])


    prediction = model.predict(input_data)

    st.subheader(f"Prediction : '{int(prediction)}'")

    if prediction ==1 :
        st.error("This transaction can be fraud")
    else:
        st.success("This transaction looks like it is not a fraud")    
