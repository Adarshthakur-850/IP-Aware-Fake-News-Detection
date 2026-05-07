from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
import os
import sys

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Load model
MODEL_PATH = "models/model.pkl"
model = None

app = FastAPI(title="IP-Aware Fake News Detection API")

class NewsRequest(BaseModel):
    text: str
    ip_address: str

@app.on_event("startup")
def load_model():
    global model
    if os.path.exists(MODEL_PATH):
        model = joblib.load(MODEL_PATH)
        print("Model loaded successfully.")
    else:
        print(f"Warning: Model not found at {MODEL_PATH}. Prediction endpoint will fail.")

@app.post("/predict")
def predict(request: NewsRequest):
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded or path incorrect.")
    
    # Create DataFrame for pipeline - keys must match training columns
    input_df = pd.DataFrame([{
        'text': request.text,
        'ip_address': request.ip_address
    }])
    
    try:
        # The pipeline expects a DataFrame
        prediction = model.predict(input_df)[0]
        probabilities = model.predict_proba(input_df)[0]
        classes = model.classes_
        
        # Get confidence for the predicted class
        # classes is an array, finding index of prediction
        class_index = list(classes).index(prediction)
        confidence = float(probabilities[class_index])
        
        return {
            "prediction": prediction,
            "confidence": confidence,
            "ip_metadata": "Processed internally" 
        }
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")

@app.get("/")
def read_root():
    return {"message": "IP-Aware Fake News Detection API is running"}
