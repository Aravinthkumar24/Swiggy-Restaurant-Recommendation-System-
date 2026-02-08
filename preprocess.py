import pandas as pd
import pickle
from sklearn.preprocessing import OneHotEncoder

# -----------------------------
# Load dataset
# -----------------------------
df = pd.read_csv("swiggy.csv")

print("Initial rows:", df.shape[0])

# -----------------------------
# Remove duplicates
# -----------------------------
df = df.drop_duplicates()

# Keep required columns
df = df[['id', 'name', 'city', 'rating', 'rating_count',
         'cost', 'cuisine', 'address']]

# -----------------------------
# Clean COST
# -----------------------------
df['cost'] = (
    df['cost']
    .astype(str)
    .str.replace('₹', '', regex=False)
    .str.replace(',', '', regex=False)
    .str.replace('--', '', regex=False)
    .str.strip()
)

df['cost'] = pd.to_numeric(df['cost'], errors='coerce')

# Fill missing cost with median
df['cost'] = df['cost'].fillna(df['cost'].median())

# -----------------------------
# Clean RATING
# -----------------------------
df['rating'] = (
    df['rating']
    .astype(str)
    .str.replace('--', '', regex=False)
    .str.replace('NEW', '', regex=False)
    .str.strip()
)

df['rating'] = pd.to_numeric(df['rating'], errors='coerce')

# Fill missing rating with mean
df['rating'] = df['rating'].fillna(df['rating'].mean())

# -----------------------------
# Clean RATING COUNT
# -----------------------------
df['rating_count'] = (
    df['rating_count']
    .astype(str)
    .str.replace('K+', '000', regex=False)
    .str.replace('+', '', regex=False)
    .str.replace('--', '', regex=False)
    .str.replace('NEW', '', regex=False)
    .str.replace(',', '', regex=False)
    .str.strip()
)

df['rating_count'] = pd.to_numeric(df['rating_count'], errors='coerce')

# Fill missing rating_count with median
df['rating_count'] = df['rating_count'].fillna(df['rating_count'].median())

# -----------------------------
# Handle categorical NaNs
# -----------------------------
df['city'] = df['city'].fillna('Unknown')
df['cuisine'] = df['cuisine'].fillna('Unknown')

# Reset index
df = df.reset_index(drop=True)

print("Rows after cleaning:", df.shape[0])

# -----------------------------
# Save cleaned data
# -----------------------------
df.to_csv("cleaned_data.csv", index=False)

# -----------------------------
# Encoding
# -----------------------------
categorical_cols = ['city', 'cuisine']
numerical_cols = ['rating', 'rating_count', 'cost']

encoder = OneHotEncoder(
    sparse_output=False,
    handle_unknown='ignore'
)

encoded_cat = encoder.fit_transform(df[categorical_cols])

encoded_cat_df = pd.DataFrame(
    encoded_cat,
    columns=encoder.get_feature_names_out(categorical_cols)
)

encoded_num_df = df[numerical_cols].copy()
encoded_num_df = encoded_num_df.fillna(0)

encoded_df = pd.concat(
    [encoded_num_df, encoded_cat_df],
    axis=1
)

encoded_df = encoded_df.fillna(0)


# -----------------------------
# Save encoded data
# -----------------------------
encoded_df.to_csv("encoded_data.csv", index=False)

# -----------------------------
# Save encoder
# -----------------------------
with open("encoder.pkl", "wb") as f:
    pickle.dump(encoder, f)

print("✅ Preprocessing completed successfully")
