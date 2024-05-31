import pandas as pd
import re
import nltk
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

def load_and_clean_data(filepath):
    data = pd.read_csv(filepath)
    data.dropna(subset=['Context', 'Response'], inplace=True)
    data['Context'] = data['Context'].apply(clean_text)
    return data

def clean_text(text):
    text = re.sub(r'\W', ' ', text)  # Eliminar caracteres especiales
    text = re.sub(r'\s+', ' ', text)  # Eliminar espacios adicionales
    text = text.lower()  # Convertir a minúsculas
    return text

if __name__ == "__main__":
    data = load_and_clean_data('data/train.csv')
    print(data.head())
