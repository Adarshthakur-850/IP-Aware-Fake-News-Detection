# IP-Aware Fake News Detection System

A production-quality AI system that predicts whether a news article is **FAKE** or **REAL** using a combination of **Text Content** (NLP) and **Source IP Address** (Geolocation/Reputation).

## Features
- **Hybrid Analysis**: Combines TF-IDF text features with IP geolocation metadata (Country, ISP, etc.).
- **NLP Pipeline**: Uses `spaCy` for robust text cleaning and lemmatization.
- **FastAPI Backend**: Serves predictions via a REST API.
- **Streamlit UI**: User-friendly interface for real-time analysis.

## Project Structure
```
ip_fake_news_ai/
│
├── data/news.csv        # Synthetic training data
├── nlp/preprocess.py    # Text cleaning logic
├── ip/ip_features.py    # IP metadata extraction
├── training/train.py    # Model training script
├── models/model.pkl     # Saved Random Forest pipeline
├── api/app.py           # FastAPI backend
├── ui/streamlit_app.py  # Streamlit frontend
└── requirements.txt
```

## Setup

1.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    python -m spacy download en_core_web_sm
    ```

2.  **Train the Model**:
    ```bash
    python -m training.train_model
    ```
    *This will generate `models/model.pkl`.*

## Running the Application

### 1. Start the API (Backend)
```bash
uvicorn api.app:app --reload
```
The API will be available at `http://127.0.0.1:8000`.

### 2. Start the UI (Frontend)
Open a new terminal and run:
```bash
streamlit run ui/streamlit_app.py
```
The UI will open in your browser.

## API Usage
**POST** `/predict`
```json
{
  "text": "Aliens landed in New York!",
  "ip_address": "192.168.1.1"
}
```
**Response**:
```json
{
  "prediction": "FAKE",
  "confidence": 0.95,
  "ip_metadata": "..."
}
```
