import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
@st.cache_data
def load_data():
    data = pd.read_csv("vgsales.csv")
    
    # Handle missing values
    if data["Year"].isnull().sum() > 0:
        median_year = data["Year"].median()  # Calculate median of non-missing years
        data["Year"] = data["Year"].fillna(median_year)  # Fill missing years with median
    
    if data["Publisher"].isnull().sum() > 0:
        data["Publisher"] = data["Publisher"].fillna("Unknown")  # Fill missing publishers with "Unknown"
    
    # Drop rows with missing values in critical columns
    data = data.dropna(subset=["Genre", "Platform", "NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"])
    return data

data = load_data()

# Title of the app
st.title("Video Game Sales Analysis")

# Sidebar for user inputs
st.sidebar.header("Filter Options")

# User selects Genre, Platform, and Region
genre_options = ["All"] + sorted(data["Genre"].unique())
platform_options = ["All"] + sorted(data["Platform"].unique())
region_options = ["All", "NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"]

genre = st.sidebar.selectbox("Select Genre", genre_options)
platform = st.sidebar.selectbox("Select Platform", platform_options)
region = st.sidebar.selectbox("Select Region", region_options)

# Filter data based on user inputs
filtered_data = data.copy()

if genre != "All":
    filtered_data = filtered_data[filtered_data["Genre"] == genre]

if platform != "All":
    filtered_data = filtered_data[filtered_data["Platform"] == platform]

if region != "All":
    sales_column = region
else:
    # If "All" is selected, sum up all regional sales
    filtered_data["Total_Sales"] = filtered_data[["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"]].sum(axis=1)
    sales_column = "Total_Sales"

# Group data by year and calculate total sales
yearly_sales = filtered_data.groupby("Year")[sales_column].sum().reset_index()

# Display filtered data
st.subheader("Filtered Data")
st.dataframe(filtered_data[["Name", "Year", "Platform", "Genre", sales_column]])

# Plot yearly sales
st.subheader("Yearly Sales Trend")
fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(data=yearly_sales, x="Year", y=sales_column, ax=ax)
ax.set_title("Yearly Sales Trend")
ax.set_xlabel("Year")
ax.set_ylabel("Sales (in millions)")
st.pyplot(fig)

# Additional Insights: Top Games by Sales
st.subheader("Top 10 Games by Sales")
top_games = filtered_data.nlargest(10, sales_column)[["Name", "Year", "Platform", "Genre", sales_column]]
st.bar_chart(top_games.set_index("Name")[sales_column])

# Additional Insights: Sales Distribution by Genre
if genre == "All":
    st.subheader("Sales Distribution by Genre")
    genre_sales = filtered_data.groupby("Genre")[sales_column].sum().reset_index()
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=genre_sales, x="Genre", y=sales_column, ax=ax)
    ax.set_title("Sales Distribution by Genre")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    st.pyplot(fig)

# Additional Insights: Sales Distribution by Platform
if platform == "All":
    st.subheader("Sales Distribution by Platform")
    platform_sales = filtered_data.groupby("Platform")[sales_column].sum().reset_index()
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=platform_sales, x="Platform", y=sales_column, ax=ax)
    ax.set_title("Sales Distribution by Platform")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    st.pyplot(fig)