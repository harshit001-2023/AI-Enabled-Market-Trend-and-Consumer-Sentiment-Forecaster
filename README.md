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

# AI-Enabled Market Trend & Consumer Sentiment Forecaster

An AI-powered platform that aggregates social media posts, product reviews, and news data to generate real-time consumer trend and sentiment insights.

## 📂 Project Structure
```text
AI-Market-Trend-Forecaster/
├── data/                      # Data storage
│   ├── raw/                   # Raw collected data (CSVs)
│   └── processed/             # Cleaned data for AI
├── src/                       # Source code
│   ├── ingestion/             # Scripts to fetch data (Scrapy/APIs)
│   ├── preprocessing/         # Cleaning & Normalization
│   ├── models/                # AI Models (Sentiment, Topic, RAG)
│   └── dashboard/             # Streamlit Frontend
└── requirements.txt           # Project dependencies
```

🚀 Progress Log
Phase 1: Data Ingestion & Setup
Objective: Build scraping and ingestion layer.

Status: In Progress

Tasks Completed:

[x] Defined Project Architecture.

[x] Created Directory Structure.

[x] Created requirements.txt.

[x] Implemented collect_redmi_data.py to fetch market news via GoogleNews.