import streamlit as st
import pandas as pd
from recommender import recommend_restaurants

# Page config
st.set_page_config(
    page_title="Swiggy Restaurant Recommender",
    layout="wide"
)
# Load data
df = pd.read_csv("cleaned_data.csv")

# -----------------------------
# UI
# -----------------------------
st.title("🍽️ Swiggy Restaurant Recommendation System")

st.sidebar.header("🔍 User Preferences")

city = st.sidebar.selectbox(
    "Select City",
    sorted(df['city'].unique())
)

cuisine = st.sidebar.selectbox(
    "Select Cuisine",
    sorted(df['cuisine'].unique())
)

min_rating = st.sidebar.slider(
    "Minimum Rating",
    1.0, 5.0, 3.5
)

max_cost = st.sidebar.slider(
    "Maximum Cost (₹)",
    min_value=0,
    max_value=1000,
    value=300,
    step=50
)

top_n = st.sidebar.slider(
    "Number of Recommendations",
    1, 10, 5
)

# -----------------------------
# Recommendation Button
# -----------------------------
if st.sidebar.button("🍴 Recommend"):
    results = recommend_restaurants(
        city=city,
        cuisine=cuisine,
        min_rating=min_rating,
        max_cost=max_cost,
        top_n=top_n
    )

    if results.empty:
        st.warning("😔 No restaurants found with these preferences")
    else:
        st.success("✅ Recommended Restaurants")
        st.dataframe(results, use_container_width=True)