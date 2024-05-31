from flask import Flask, render_template, request, jsonify
from chatbot.inference import PsychologicalSupport
from experta import Fact
import joblib
import re

app = Flask(__name__)
chatbot = PsychologicalSupport()

# Cargar el modelo entrenado
model_path = 'trained_model.pkl'
model = joblib.load(model_path)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    chatbot.reset()
    chatbot.declare(Fact(input=user_input))
    chatbot.run()

    # Procesar la entrada del usuario con el modelo entrenado
    processed_input = clean_text(user_input)
    prediction = model.predict([processed_input])
    predicted_response = prediction[0]

    return jsonify({'response': predicted_response})

def clean_text(text):
    text = re.sub(r'\W', ' ', text)  # Eliminar caracteres especiales
    text = re.sub(r'\s+', ' ', text)  # Eliminar espacios adicionales
    text = text.lower()  # Convertir a minúsculas
    return text

if __name__ == "__main__":
    app.run(debug=True)
