import os
import requests
import pandas as pd

DATA_URL = "https://raw.githubusercontent.com/OmkarPathak/Playing-with-datasets/master/Email%20Spam%20Filtering/emails.csv"
DATA_PATH = os.path.join("data", "emails.csv")

def load_data():
    if not os.path.exists("data"):
        os.makedirs("data")
        
    if not os.path.exists(DATA_PATH):
        print(f"Downloading data from {DATA_URL}...")
        try:
            response = requests.get(DATA_URL)
            response.raise_for_status()
            with open(DATA_PATH, "wb") as f:
                f.write(response.content)
            print("Download complete.")
        except Exception as e:
            print(f"Error downloading data: {e}")
            raise
            
    print("Loading dataset...")
    df = pd.read_csv(DATA_PATH)
    print(f"Dataset shape: {df.shape}")
    return df

if __name__ == "__main__":
    load_data()
