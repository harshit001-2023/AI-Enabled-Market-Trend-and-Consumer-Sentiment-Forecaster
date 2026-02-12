import pandas as pd  # Like Java's data handling libs
import os

# Function to load data from CSV (your clean_stage_1.csv)
def load_raw_data(file_path):
    if not os.path.exists(file_path):
        print("Error: File not found! Check path.")
        return []
    
    df = pd.read_csv(file_path)  # Pandas reads CSV like a table
    data_list = []
    for index, row in df.iterrows():  # Loop like in Java
        data = ConsumerData(
            source=row['Source'],
            text=row['Comment'],
            date=row['PublishedAt']
        )
        data_list.append(data)
    
    return data_list

# Example usage (test this!)
if __name__ == "__main__":  # Like Java's main()
    raw_data = load_raw_data("data/raw/clean_stage_1.csv")  # Put your CSV in data/raw/
    print(f"Loaded {len(raw_data)} items.")
    print(raw_data[0].to_dict())  # Print first one