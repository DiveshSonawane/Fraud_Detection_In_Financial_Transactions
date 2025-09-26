# Fraud_Detection_In_Financial_Transactions
Internship Project at Codec Technologies Detecting Frauds in Financial Transactions

## Project Overview
This project aims to **identify suspicious or fraudulent financial transactions** using machine learning. The solution uses both **supervised and unsupervised techniques** to detect anomalies in credit card transactions.  

The project leverages the following:

- **Supervised Models:** Logistic Regression, Random Forest, XGBoost  
- **Unsupervised Models for Anomaly Detection:** Isolation Forest, AutoEncoder  
- **Class Imbalance Techniques:** SMOTE, Random Undersampling, Class Weights  
- **Data Visualization & EDA:** Pandas, Seaborn, Matplotlib  
- **Deployment:** Streamlit app for interactive testing  

---

## Dataset
The dataset used is the **Credit Card Fraud Detection Dataset** from Kaggle:

[Credit Card Fraud Detection Dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)  

> **Note:** For privacy reasons, the dataset is not uploaded to this repository. Please download it from Kaggle and process it as required before retraining models.

---

## Project Structure

| File | Description |
|------|-------------|
| `Fraud_Detection.ipynb` | Jupyter Notebook containing full EDA, preprocessing, model training, and evaluation. |
| `app.py` | Streamlit application for real-time transaction fraud prediction. |
| `fraud_detection_pipeline.pkl` | Pre-trained pipeline containing scaler + XGBoost model. |
| `xgboost_fraud_model.pkl` | Optional saved XGBoost model separately (if needed). |
| `README.md` | Project description, instructions, and usage. |
| `Fraud_Detection_Financial_Transaction_Report` | Detailed Project Report. |

---

## Installation and Setup

1. Clone the repository:

```bash
git clone https://github.com/DiveshSonawane/Fraud_Detection_In_Financial_Transactions.git
cd FraudDetectionApp

---

## Author

Divesh Sonawane
Email: diveshsonawane66@gmail.com  
Internship Project – Fraud Detection in Financial Transactions
