# 📌 Sentiment Analysis on Amazon Fine Food Reviews  
### Using VADER + RoBERTa Transformers + NLTK    

---

## 🧠 Project Overview  
This project performs **end-to-end sentiment analysis** on the **Amazon Fine Food Reviews** dataset using:

- **NLTK Tokenization & POS tagging**
- **Named Entity Recognition (Chunking)**
- **VADER Sentiment Analyzer (Rule-based)**
- **RoBERTa Transformer Model (cardiffnlp/twitter-roberta-base-sentiment)**
- **Data Visualizations (Seaborn + Matplotlib)**
- **Comparison of two sentiment models**

The main goal is to understand how **rule-based** and **transformer-based** sentiment models behave on the same dataset.

All logic is implemented inside the file:

📄 `sentiment_analysis_python.py`

---

## 📂 Dataset  
We use the **Amazon Fine Food Reviews (Kaggle)** dataset.  
From the full dataset, the script loads:

- `Reviews.csv`  
- First **500 reviews** sampled for faster processing  
- Contains columns such as:  
  - `Id`  
  - `ProductId`  
  - `UserId`  
  - `Score`  
  - `Summary`  
  - `Text`

---



