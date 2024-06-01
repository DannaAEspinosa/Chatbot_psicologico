import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib
import nltk
from nltk.corpus import stopwords
from data_preprocessing import load_and_clean_data

nltk.download('stopwords')

# Cargar y limpiar los datos
data = load_and_clean_data('data/train.csv')

# Dividir el dataset en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(data['Context'], data['Response'], test_size=0.2, random_state=42)

# Crear un pipeline de procesamiento y modelo
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words=stopwords.words('english'))),
    ('nb', MultinomialNB())
])

# Entrenar el modelo
pipeline.fit(X_train, y_train)

# Evaluar el modelo
accuracy = pipeline.score(X_test, y_test)
print(f'Model Accuracy: {accuracy}')

# Guardar el modelo entrenado
joblib.dump(pipeline, 'trained_model.pkl')
