import requests
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

def get_ip_info(ip):
    try:
        # Use ip-api.com (free, rate limited)
        response = requests.get(f"http://ip-api.com/json/{ip}", timeout=5)
        if response.status_code == 200:
            data = response.json()
            if data['status'] == 'success':
                return {
                    'country': data.get('country', 'Unknown'),
                    'city': data.get('city', 'Unknown'),
                    'isp': data.get('isp', 'Unknown'),
                    'org': data.get('org', 'Unknown')
                }
    except Exception as e:
        print(f"Error fetching IP info for {ip}: {e}")
    
    return {
        'country': 'Unknown',
        'city': 'Unknown',
        'isp': 'Unknown',
        'org': 'Unknown'
    }

class IPFeatureExtractor(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        features = []
        for ip in X:
            info = get_ip_info(ip)
            # Simple feature: Is the ISP a common residential one? (Simplified logic)
            # In a real system, you'd OHE the country/ISP, but for Demo we'll just return lengths or simple indicators
            # to keep the vector size manageable without a fitted encoder here (best handled in main pipeline)
            # ACTUALLY: Let's just return the raw dictionary, and let a DictVectorizer handle it in the pipeline if possible,
            # BUT: sklearn pipelines prefer array-like.
            # Let's return a DataFrame for compatibility with ColumnTransformer if we were using it, 
            # or just a list of dicts if we use DictVectorizer.
            features.append(info)
        return features
