import pandas as pd
import re
import os

# Define paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RAW_DATA_PATH = os.path.join(BASE_DIR, 'data', 'raw', 'redmi_market_data.csv')
PROCESSED_DATA_PATH = os.path.join(BASE_DIR, 'data', 'processed', 'cleaned_redmi_data.csv')

def clean_text(text):
    if not isinstance(text, str):
        return ""
    
    # 1. Convert to lowercase
    text = text.lower()
    
    # 2. Remove URLs (http://...)
    text = re.sub(r'http\S+|www\.\S+', '', text)
    
    # 3. Remove HTML tags (<div>, <br>)
    text = re.sub(r'<.*?>', '', text)
    
    # 4. Remove special characters and numbers (keep only words)
    # This regex keeps letters and spaces. Adjust if you need numbers.
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    
    # 5. Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

def preprocess_data():
    print("Loading raw data...")
    if not os.path.exists(RAW_DATA_PATH):
        print(f"Error: File not found at {RAW_DATA_PATH}")
        return

    df = pd.read_csv(RAW_DATA_PATH)
    
    # Create a new column 'cleaned_text' by combining title and description if available
    # For GoogleNews data, we usually have 'title' and sometimes 'desc'
    # Let's clean the 'title' column for now
    print("Cleaning text...")
    df['cleaned_title'] = df['title'].apply(clean_text)
    
    # Ensure processed directory exists
    os.makedirs(os.path.dirname(PROCESSED_DATA_PATH), exist_ok=True)
    
    # Save the cleaned data
    df.to_csv(PROCESSED_DATA_PATH, index=False)
    print(f"Success! Cleaned data saved to: {PROCESSED_DATA_PATH}")
    print(df[['title', 'cleaned_title']].head())

if __name__ == "__main__":
    preprocess_data()