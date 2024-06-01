from flask import Flask, render_template, request, redirect, url_for, flash, session,jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from models.users import User, db  
from chatbot.inference import PsychologicalSupport
from experta import Fact

load_dotenv('.env')

app = Flask(__name__)

chatbot = PsychologicalSupport()

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:admin@localhost/psychological_healthcare'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configuración de la clave secreta
app.config['SECRET_KEY'] = 'P4SSWORD_TORTICODE'  # Clave secreta para las sesiones

db.init_app(app)  # Inicializa la instancia de SQLAlchemy con la aplicación Flask

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
    response_text = ' '.join(responses)

    if 'citizenshipCard' in session:
        user = User.query.filter_by(citizenshipCard=session['citizenshipCard']).first()
        if user:
            new_conversation = Conversation(user_id=user.id, message=user_input, response=response_text)
            db.session.add(new_conversation)
            db.session.commit()

    return jsonify({'responses': responses})


@app.route('/chatbot')
def dashboard():
    if 'citizenshipCard' in session:
        return render_template('chatbot.html')
    else:
        flash('You are not logged in!', 'warning')
        return redirect(url_for('login'))

@app.route('/chatbot', methods=['POST'])

@app.route('/logout')
def logout():
    session.pop('citizenshipCard', None)
    flash('You have been logged out!', 'info')
    return redirect(url_for('login'))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

# Endpoint para crear tablas - eliminar después de crear la tabla
@app.route('/create_tables')
def create_tables():
    with app.app_context():
        db.create_all()
    return "Tables created", 200

if __name__ == '__main__':
    app.run(debug=True)