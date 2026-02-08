import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Load data
cleaned_df = pd.read_csv("cleaned_data.csv")
encoded_df = pd.read_csv("encoded_data.csv")

# Memory optimization
encoded_df = encoded_df.fillna(0).astype(np.float32)

def recommend_restaurants(city, cuisine, min_rating, max_cost, top_n=5):

    # Step 1: Filter FIRST (very important)
    filtered = cleaned_df[
        (cleaned_df['city'] == city) &
        (cleaned_df['rating'] >= min_rating) &
        (cleaned_df['cost'] <= max_cost)
    ]

    if filtered.empty:
        return pd.DataFrame()

    # Get indices of filtered rows
    filtered_indices = filtered.index.tolist()

    # Step 2: Select reference restaurant
    ref_idx = filtered_indices[0]

    # Step 3: Compute similarity ONLY on filtered data
    similarity = cosine_similarity(
        encoded_df.loc[[ref_idx]],
        encoded_df.loc[filtered_indices]
    ).ravel()

    # Step 4: Attach similarity safely
    filtered = filtered.copy()
    filtered['similarity'] = similarity

    # Step 5: Cuisine filtering + sorting
    results = filtered[
        filtered['cuisine'].str.contains(cuisine, case=False, na=False)
    ].sort_values(
        by='similarity',
        ascending=False
    ).head(top_n)

    return results[['name', 'city', 'cuisine', 'rating', 'cost', 'address']]
