# app.py

import streamlit as st
import pandas as pd

# Load the dataset
@st.cache_data
def load_data():
    return pd.read_csv('vgsales.csv')

# Main function
def main():
    # Title of the app
    st.title("Video Game Sales Analysis")

    # Load the data
    df = load_data()

    # Sidebar for user inputs
    st.sidebar.header("Filter Options")

    # Select Console (Platform)
    platforms = df['Platform'].unique()
    selected_platform = st.sidebar.selectbox("Select Console", platforms)

    # Select Genre
    genres = df['Genre'].unique()
    selected_genre = st.sidebar.selectbox("Select Genre", genres)

    # Select Region
    regions = ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']
    region_names = {
        'NA_Sales': 'North America',
        'EU_Sales': 'Europe',
        'JP_Sales': 'Japan',
        'Other_Sales': 'Other Regions',
        'Global_Sales': 'Global'
    }
    selected_region = st.sidebar.selectbox("Select Region", regions, format_func=lambda x: region_names[x])

    # Filter the data based on user inputs
    filtered_data = df[(df['Platform'] == selected_platform) & (df['Genre'] == selected_genre)]

    # Display statistics
    st.header(f"Sales Statistics for {selected_genre} games on {selected_platform} in {region_names[selected_region]}")
    
    if filtered_data.empty:
        st.warning("No data available for the selected filters.")
    else:
        # Display total sales
        total_sales = filtered_data[selected_region].sum()
        st.metric("Total Sales (in millions)", f"{total_sales:.2f}")

        # Display top 10 games by sales
        top_games = filtered_data.nlargest(10, selected_region)[['Name', selected_region]]
        top_games.columns = ['Game Name', 'Sales (in millions)']
        st.subheader("Top 10 Games by Sales")
        st.table(top_games)

        # Display a bar chart for top games
        st.subheader("Bar Chart of Top Games")
        st.bar_chart(top_games.set_index('Game Name'))

        # Display average sales
        avg_sales = filtered_data[selected_region].mean()
        st.metric("Average Sales per Game (in millions)", f"{avg_sales:.2f}")

# Run the app
if __name__ == "__main__":
    main()