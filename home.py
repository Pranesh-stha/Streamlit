import streamlit as st


homepage_html = """
<style>

    body {
        font-family: 'Arial', sans-serif;
        background-color: #f4f4f9;
        color: #333;
        margin: 0;
        padding: 0;
    }

    /* Header Section */
    .header {
        text-align: center;
        margin-bottom: 30px;
    }

    .header h1 {
        font-size: 2.5em;
        color: #1f77b4;
        margin-bottom: 10px;
    }

    .header p {
        font-size: 1.2em;
        color: #555;
    }

    /* Group Information */
    .group-info {
        background-color: #262730;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 30px;
        
        display: flex;
        flex-direction: column;
        align-items: center;
      justify-content: center;
    }

    .group-info h2 {
        font-size: 1.8em;
        color: #1f77b4;
        margin-bottom: 15px;
    }

    .group-info ul {
        list-style-type: none;
        padding: 0;
    }

    .group-info li {
        font-size: 1.1em;
        margin-bottom: 10px;
        color: #B9DAF3;
    }

    /* Additional Content */
    .additional-content {
        text-align: center;
        font-size: 1.1em;
        color: #555;
    }

    .additional-content a {
        color: #1f77b4;
        text-decoration: none;
    }

    .additional-content a:hover {
        text-decoration: underline;
    }
</style>

<div class="header">
    <h1 style = "color: white; font-size:45pt;">🎮 Video Game Sales🎮 ​​​ ​Analysis & Prediction </h1>
    <h1>Welcome to Our Video Game Sales Dashboard</h1>
    <p>Analyze trends and predict future sales of video games.</p>
</div>

<div class="group-info">
    <h2>About Us</h2>
    <ul>
        <li><strong>Group Name:</strong> Pranesh's Team</li>
        <li><strong>Group Members:</strong></li>
        <li>1. Pranesh Shrestha</li>
        <li>2. Libisha Gurung</li>
        <li>3. Mallika Upreti</li>
    </ul>
</div>

<div class="additional-content">
    <p>Explore our features:</p>
    <p>
        🔍 <a href="/filter_app">Filter and Analyze Data</a> |
        📈 <a href="/predict_app">Predict Future Sales</a>
    </p>
    <p>Made with ❤️ by Pranesh's Team</p>
</div>
"""


st.markdown(homepage_html, unsafe_allow_html=True)