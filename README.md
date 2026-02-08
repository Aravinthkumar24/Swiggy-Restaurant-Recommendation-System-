🍽️ Swiggy Restaurant Recommendation System using Streamlit
📌 Project Overview
This project implements a Restaurant Recommendation System using Swiggy restaurant data. The system recommends restaurants to users based on preferences such as city, cuisine, rating, and cost. It demonstrates an end-to-end data science workflow including data preprocessing, feature encoding, similarity-based recommendation, and deployment using Streamlit.
________________________________________
🧠 Domain
Recommendation Systems | Data Analytics | Machine Learning
________________________________________
🛠️ Skills & Technologies Used
•	Python
•	Pandas & NumPy
•	Scikit-learn
•	One-Hot Encoding
•	Cosine Similarity
•	Streamlit
•	Pickle
•	Git & GitHub
________________________________________
📂 Dataset Description
The dataset is provided in CSV format and contains the following columns:
•	Categorical Features: name, city, cuisine
•	Numerical Features: rating, rating_count, cost
•	Other Columns: id, lic_no, link, address, menu
________________________________________
🔧 Project Workflow
1️⃣ Data Cleaning
•	Removed duplicate records
•	Cleaned currency symbols and text-based numeric fields
•	Handled missing values using mean/median imputation
•	Filled missing categorical values with Unknown
Output: cleaned_data.csv
________________________________________
2️⃣ Data Preprocessing
•	Applied One-Hot Encoding to city and cuisine
•	Ensured all features are numerical
•	Maintained index alignment between cleaned and encoded data
Outputs: - encoded_data.csv - encoder.pkl
________________________________________
3️⃣ Recommendation Engine
•	Used Cosine Similarity to find similar restaurants
•	Recommendations generated from encoded feature space
•	Results mapped back to cleaned dataset for readability
________________________________________
4️⃣ Streamlit Application
User Inputs: - City - Cuisine - Minimum Rating - Maximum Cost (capped at ₹1000) - Number of recommendations
Output: - Recommended restaurants with name, cuisine, rating, and cost
________________________________________
📊 Evaluation Metrics
•	Recommendation relevance and diversity
•	Application usability
•	Data consistency between processed datasets
________________________________________
🗂️ Project Structure
Swiggy-Recommendation/
│
├── swiggy.csv
├── preprocess.py
├── recommender.py
├── app.py
├── cleaned_data.csv
├── encoded_data.csv
├── encoder.pkl
├── requirements.txt
└── README.md
________________________________________
▶️ How to Run the Project
pip install -r requirements.txt
python preprocess.py
streamlit run app.py
________________________________________
🚀 Conclusion
This project demonstrates how machine learning and data analytics techniques can be applied to build a real-world recommendation system. The Streamlit interface makes the system interactive, user-friendly, and deployment-ready.
________________________________________
