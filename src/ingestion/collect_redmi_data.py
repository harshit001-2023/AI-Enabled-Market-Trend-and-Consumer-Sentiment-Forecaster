# Save this as collect_redmi_data.py
# Prerequisite: pip install GoogleNews pandas

from GoogleNews import GoogleNews
import pandas as pd

def fetch_redmi_data():
    googlenews = GoogleNews(lang='en', region='IN')

    # Define keywords based on your teammate's request
    keywords = ['Redmi Buds 8 Lite review', 'Redmi Buds 6 Pro problems', 'Redmi SonicBass Wireless 2 review']
    all_data = []

    print("Fetching data...")
    for key in keywords:
        googlenews.search(key)
        results = googlenews.result()
        for item in results:
            all_data.append({
                'source': item['media'],
                'date': item['date'],
                'title': item['title'],
                'link': item['link'],
                'keyword_tag': key
            })
        googlenews.clear()

    # Save to CSV for the project
    df = pd.DataFrame(all_data)
    df.to_csv('redmi_market_data.csv', index=False)
    print(f"Successfully saved {len(df)} records to redmi_market_data.csv")

if __name__ == "__main__":
    fetch_redmi_data()