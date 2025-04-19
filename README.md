# Sales Prediction and Forecasting System
# Project Overview

This project focuses on predicting sales (in this case, stock prices) using machine learning techniques. The goal is to forecast the stock prices of Google (GOOGL) using historical data. This is achieved through a deep learning model built using **LSTM (Long Short-Term Memory)** networks, a type of Recurrent Neural Network (RNN). The predictions are then sent to the user in the form of a report via email.

The project fetches data from Yahoo Finance (yfinance) and stores it in a Firebase database for easy access. The system makes use of the stock market data stored in Firebase and performs predictive analysis. After making predictions, the system generates an email report containing the forecast for the upcoming days.

---

# Technology Stack
**Python**: The main programming language used for the project. Python is ideal for data analysis, machine learning, and integration with web services.

**yfinance**: This library is used to fetch historical stock price data from Yahoo Finance. We chose yfinance because it's a reliable, easy-to-use tool for accessing stock market data and integrates seamlessly with the project.

**Firebase**: Firebase is used for storing and managing the stock market data. It serves as a cloud-based NoSQL database for holding the historical stock data fetched from Yahoo Finance.

**LSTM (Long Short-Term Memory)**: A type of Recurrent Neural Network (RNN) used for time series forecasting. LSTM is used here because it is effective for predicting sequential data, such as stock prices, which have a temporal dependency.

**Joblib**: This is used to save and load the trained model and scaler for future use, making the predictions process faster and more efficient.

**Email (SMTP)**: After making predictions, the system sends a report via email to the user. This is done using Python's built-in smtplib for sending emails.

---

# Features
Fetch Data: The project fetches Google (GOOGL) stock price data from Yahoo Finance using the yfinance library. The data is fetched for the past year by default and stored in Firebase.

Training: The LSTM model is trained on the historical stock data, utilizing a sequence of 100 previous days to predict the stock price for the next 7 days.

Prediction: The trained LSTM model predicts the next 7 days of stock prices based on the historical data.

Email Reports: Once the prediction is made, the system sends an email report to a specified email address, detailing the predicted stock prices for the next days.

---

# Data Flow & Process
Data Fetching:

The system fetches historical stock data for Google (GOOGL) using the yfinance API.

This data is then stored in Firebase using Firebase Admin SDK.

---

# Model Training:

The data fetched from Firebase is processed and scaled using the MinMaxScaler to bring all values between 0 and 1.

The data is then used to train a deep learning model (LSTM) to predict stock prices based on the historical trends.

---

# Prediction:

After training, the model is used to predict the stock prices for the next 7 days.

The predicted prices are rescaled to their original values and formatted for easy readability.

---

# Email Report:

The predicted stock prices are compiled into an HTML email report.

The email is sent to a predefined email address via SMTP.

---

# Model Accuracy

The accuracy of the model is measured based on its performance on unseen test data. The model uses Mean Absolute Error (MAE) as the loss function during training, which is a common metric for regression tasks.

Given that stock prices are inherently volatile and influenced by numerous external factors, achieving high accuracy with stock market predictions is challenging. However, the model provides valuable predictions that can be used for decision-making in trading or sales forecasting.

---

Accuracy Metrics:
Mean Absolute Error (MAE): The model's performance is tracked using MAE. The lower the MAE, the better the model is at predicting stock prices.

Required Libraries: Install the required libraries by running the following command: pip install -r requirements.txt
