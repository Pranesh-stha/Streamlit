import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Load the dataset
@st.cache_data
def load_data():
    data = pd.read_csv("vgsales.csv")
    # Drop rows with missing values in critical columns
    data = data.dropna(subset=["Genre", "Platform", "NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"])
    return data

data = load_data()

# Title of the app
st.title("Video Game Sales Predictor")

# Sidebar for user inputs
st.sidebar.header("Select Parameters")

# User selects Genre, Platform, and Region
genre = st.sidebar.selectbox("Select Genre", sorted(data["Genre"].unique()))
platform = st.sidebar.selectbox("Select Platform", sorted(data["Platform"].unique()))
region = st.sidebar.selectbox("Select Region", ["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"])

# Filter data based on user inputs
filtered_data = data[(data["Genre"] == genre) & (data["Platform"] == platform)]

# Display filtered data
st.subheader("Filtered Data")
st.dataframe(filtered_data[["Name", "Year", "Publisher", region]])

# Statistical Summary
st.subheader("Statistical Summary")
summary = filtered_data[region].describe()
st.write(summary)

# Predictive Modeling
st.subheader("Predict Sales Using Regression")

# Prepare data for regression
X = filtered_data[["Year"]]
y = filtered_data[region]

# Encode Year as numeric if needed
X = X.fillna(0)  # Fill missing years with 0 for simplicity

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)

# Display model performance
st.write(f"Mean Squared Error: {mse:.2f}")

# Plot predictions vs actual
fig, ax = plt.subplots()
ax.scatter(X_test, y_test, color="blue", label="Actual")
ax.scatter(X_test, y_pred, color="red", label="Predicted")
ax.set_xlabel("Year")
ax.set_ylabel("Sales")
ax.legend()
st.pyplot(fig)

# Predict sales for a specific year
st.subheader("Predict Future Sales")
year_to_predict = st.number_input("Enter Year to Predict", min_value=1980, max_value=2025, value=2023)
predicted_sales = model.predict([[year_to_predict]])
st.write(f"Predicted Sales for {year_to_predict}: {predicted_sales[0]:.2f} million units")