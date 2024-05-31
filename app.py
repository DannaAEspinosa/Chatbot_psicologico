from flask import Flask, render_template, request, jsonify
from chatbot.inference import PsychologicalSupport
from experta import Fact

app = Flask(__name__)
chatbot = PsychologicalSupport()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    chatbot.reset()
    chatbot.declare(Fact(input=user_input))
    chatbot.run()

    responses = [fact['response'] for fact in chatbot.facts.values() if 'response' in fact]
    return jsonify({'responses': responses})

if __name__ == "__main__":
    app.run(debug=True)
