# IP-Aware Fake News Detection

An intelligent fake news detection system that combines **Natural Language Processing (NLP)** and **IP-aware tracking mechanisms** to identify misleading news articles and analyze the source of suspicious content.

This project helps users verify whether a news article is **real or fake** by analyzing textual content and tracking source-related metadata such as IP/location details for enhanced transparency.


---

## Features

- Detects fake vs real news articles
- Text preprocessing and cleaning
- TF-IDF / NLP-based feature extraction
- Machine Learning classification model
- IP-aware source tracking
- News credibility prediction
- User-friendly interface for news input
- Real-time prediction output

---

## Tech Stack

- Python
- Machine Learning
- Scikit-learn
- Pandas
- NumPy
- NLP
- Flask / Streamlit *(update based on your actual frontend)*
- IP Geolocation APIs *(if used)*

---

## Project Workflow

1. Collect fake and real news dataset  
2. Perform data cleaning and preprocessing  
3. Apply NLP techniques:
   - Tokenization
   - Stopword removal
   - Stemming/Lemmatization
4. Convert text into numerical vectors using TF-IDF
5. Train machine learning model
6. Detect fake news
7. Track source metadata/IP information
8. Display final prediction

---

## Dataset

This project uses fake and real news datasets for training the model.

Common datasets used:
- Fake.csv
- True.csv
- Kaggle Fake News Dataset

Example dataset source: Kaggle fake news datasets are commonly used in fake news classification projects. :contentReference[oaicite:1]{index=1}

---

## Machine Learning Models

Possible models used:

- Logistic Regression
- Naive Bayes
- Random Forest
- Passive Aggressive Classifier

You can update this section with your exact model.

---

## Project Structure

```bash
IP-Aware-Fake-News-Detection/
│
├── dataset/
├── model/
├── notebooks/
├── app.py
├── train.py
├── requirements.txt
├── templates/
├── static/
└── README.md
````

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Adarshthakur-850/IP-Aware-Fake-News-Detection.git
cd IP-Aware-Fake-News-Detection
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python app.py
```

---

## Example Input

```text
Breaking News: Government announces new economic policy...
```

## Example Output

```text
Prediction: Fake News
Source Risk Level: Medium
IP Origin: Detected
```

---

## Future Improvements

* Deep learning integration (LSTM/BERT)
* Real-time news scraping
* Browser extension integration
* Blockchain-based news verification
* Better source authentication

---

## Applications

* Journalism verification
* Social media monitoring
* Cybersecurity
* News validation platforms
* Government misinformation tracking

---

## Author

**Adarsh Thakur**

GitHub: [Adarshthakur-850](https://github.com/Adarshthakur-850?utm_source=chatgpt.com)

---

## License

This project is licensed under the MIT License.
