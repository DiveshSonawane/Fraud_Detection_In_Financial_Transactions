import streamlit as st
import joblib
import pandas as pd

# Load saved pipeline (scaler + XGBoost)
model = joblib.load(r"C:\Users\hp\PycharmProjects\FraudDetection\.venv\fraud_detection_pipeline.pkl")

# App title
st.set_page_config(page_title="Fraud Detection System", page_icon="💳", layout="wide")
st.title("💳 Fraud Detection in Financial Transactions")
st.write("Manually enter transaction details below to check if it's fraudulent.")

# --- Input Section ---
st.subheader("Enter Transaction Features")

# Collect all inputs
input_values = {}
feature_list = [
    'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10',
    'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20',
    'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28',
    'norm_Time', 'norm_Amount'
]

# Create 3-column layout for cleaner UI
cols = st.columns(3)
for i, feature in enumerate(feature_list):
    with cols[i % 3]:
        input_values[feature] = st.number_input(
            f"{feature}",
            value=0.0,
            step=0.01,
            format="%.5f"
        )

# Convert to DataFrame
input_df = pd.DataFrame([input_values])

# --- Prediction Section ---
if st.button("Check Transaction"):
    # Predict probability and class
    prob = model.predict_proba(input_df)[:, 1][0]
    prediction = model.predict(input_df)[0]

    st.subheader("Prediction Results")

    # Fraud
    if prediction == 1:
        st.error(f"Fraudulent Transaction Detected!")
        st.write(f"**Fraud Probability:** {prob:.4f}")
        st.warning("Suggestion: Block or flag this transaction for manual review.")
    else:
        st.success(f"Legitimate Transaction.")
        st.write(f"**Fraud Probability:** {prob:.4f}")
        st.info("Suggestion: Allow this transaction but continue monitoring unusual patterns.")
