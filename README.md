# 📈 AI-Enabled Market Trend and Consumer Sentiment Forecaster

![Infosys SpringBoard](https://img.shields.io/badge/Infosys_SpringBoard-Internship_6.0-blue?style=for-the-badge&logo=infosys)
![Python](https://img.shields.io/badge/Python-3.8%2B-yellow?style=for-the-badge&logo=python&logoColor=white)
![Machine Learning](https://img.shields.io/badge/Machine_Learning-Scikit_Learn-orange?style=for-the-badge)

## 📋 Project Overview

This project was developed as part of the **Infosys SpringBoard Virtual Internship 6.0 (AI/ML)**.

The **AI-Enabled Market Trend and Consumer Sentiment Forecaster** is a machine learning solution designed to analyze historical market data alongside consumer sentiment from unstructured text sources (such as news headlines, social media, or product reviews). By integrating time-series analysis with Natural Language Processing (NLP), this tool aims to provide actionable insights into future market behaviors and consumer trends.

### 🎯 Key Objectives
* **Forecast Market Trends:** Utilize historical numerical data to predict future stock prices or sales trends.
* **Analyze Sentiment:** Process textual data to gauge positive, negative, or neutral consumer sentiment.
* **Correlate Data:** Identify relationships between public sentiment and market movements.
* **Visualize Insights:** Provide clear, interactive dashboards for stakeholders.

---

## 👥 Team Members

This project was collaboratively designed and implemented by:

| Name | Role |
| :--- | :--- |
| **Nelluri Dolendra Sai Teja** | Team Member / Developer |
| **Shivani Patil** | Team Member / Developer |
| **Harshit Manish Pande** | Team Member / Developer |
| **Praveenkumar Yetigadda** | Team Member / Developer |
| **Shridula Bandari** | Team Member / Developer |

### 🎓 Mentorship
* **Program:** Infosys SpringBoard Virtual Internship 6.0
* **Mentor Email:** springboardmentor537@gmail.com

---

## ⚙️ Features

* **Data Ingestion:** Automated fetching of stock market data (via APIs like Yahoo Finance) and scraping of relevant news/social media data.
* **Preprocessing Pipeline:**
    * *Text Cleaning:* Stop-word removal, tokenization, and lemmatization.
    * *Data Normalization:* Scaling numerical data for model training.
* **Sentiment Analysis Module:** Uses NLP techniques (e.g., VADER, TextBlob, or BERT) to score text data.
* **Trend Prediction Model:** Implements algorithms such as LSTM (Long Short-Term Memory) or ARIMA for time-series forecasting.
* **Interactive Dashboard:** Visualizes predictions vs. actuals and sentiment distribution over time.

---

## 🛠️ Tech Stack

* **Programming Language:** Python
* **Data Analysis:** Pandas, NumPy
* **Visualization:** Matplotlib, Seaborn, Plotly
* **Machine Learning:** Scikit-learn, TensorFlow / Keras
* **NLP:** NLTK, Spacy, Transformers (Hugging Face)
* **IDE:** Jupyter Notebook / Google Colab

---

## 🚀 Installation & Usage

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/your-username/market-trend-sentiment-forecaster.git](https://github.com/your-username/market-trend-sentiment-forecaster.git)
    cd market-trend-sentiment-forecaster
    ```

2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Project:**
    * For the notebook analysis:
        ```bash
        jupyter notebook
        ```
    * (Optional) If using a Streamlit/Flask app:
        ```bash
        streamlit run app.py
        ```

---

## 📊 Project Workflow

1.  **Input:** User selects a stock ticker or product category.
2.  **Processing:** System fetches the last 30-90 days of data and recent news.
3.  **Analysis:** The model calculates a "Sentiment Score" and forecasts the "Trend Line."
4.  **Output:** A graph displaying the predicted trend adjusted for current sentiment.

---

## 📜 Acknowledgments

* **Infosys SpringBoard** for providing the platform and learning resources.
* **Mentors and Guides** for their valuable feedback during Internship 6.0.
