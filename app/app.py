from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from .models.users import User, db
from .chatbot.inference import PsychologicalSupport
from experta import Fact
from flask_migrate import Migrate
from .models.bayesian_network import create_bayesian_network
from pgmpy.inference import VariableElimination
from .models.conversation import Conversation

load_dotenv('.env')

app = Flask(__name__)
# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:admin@localhost/psychological_healthcare'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configuración de la clave secreta
app.config['SECRET_KEY'] = 'P4SSWORD_TORTICODE'  # Clave secreta para las sesiones

db.init_app(app)  # Inicializa la instancia de SQLAlchemy con la aplicación Flask
migrate = Migrate(app, db)
chatbot = PsychologicalSupport()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        citizenship_card = request.form['citizenshipCard']
        name = request.form['name']
        last_name = request.form['lastName']
        email = request.form['email']
        password = request.form['password']
        
        # Verifica si el usuario ya existe
        existing_user = User.query.filter_by(citizenshipCard=citizenship_card).first()
        if existing_user:
            flash('Un usuario con esta cédula ya existe', 'danger')
            return redirect(url_for('register'))
        
        # Crea un nuevo usuario
        new_user = User(citizenshipCard=citizenship_card, name=name, lastName=last_name, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        
        flash('¡Registro exitoso! Por favor, inicia sesión.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')


@app.route('/start_assessment', methods=['POST'])
def start_assessment():
    return jsonify({'status': 'assessment_started'})

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    user_choice = request.form.get('user_choice', '')  # Utiliza .get para evitar KeyError si no está presente
    chatbot.reset()
    chatbot.declare(Fact(input=user_input))
    chatbot.run()

    responses = [fact['response'] for fact in chatbot.facts.values() if 'response' in fact]
    response_text = ' '.join(responses)
    
    show_options = False
    show_initial_options = False
    if user_choice == "feelings":
        if "Lo siento, no tengo una respuesta específica para eso. ¿Podrías describir más tu situación?" in responses:
            show_options = False
        else:
            show_options = True
    elif user_choice == "options":
        if user_input == "1":
            responses.append("Perfecto, cuéntame cómo te sientes.")
        elif user_input == "2":
            show_initial_options = True
        elif user_input == "3":
            responses.append("Gracias por hablar conmigo. ¡Cuídate mucho!")
        else:
            responses.append("Por favor, elige una opción válida: 1) Decir algo más 2) Volver al inicio 3) Finalizar chat")
    
    if 'citizenshipCard' in session:
        user = User.query.filter_by(citizenshipCard=session['citizenshipCard']).first()
        if user:
            new_conversation = Conversation(user_id=user.id, message=user_input, response=response_text)
            db.session.add(new_conversation)
            db.session.commit()
            
    return jsonify({'responses': responses, 'show_options': show_options, 'show_initial_options': show_initial_options})
@app.route('/save_conversation', methods=['POST'])
def save_conversation():
    user_input = request.form['user_input']
    response_text = request.form['response_text']
    if 'citizenshipCard' in session:
        user = User.query.filter_by(citizenshipCard=session['citizenshipCard']).first()
        if user:
            new_conversation = Conversation(user_id=user.id, message=user_input, response=response_text)
            db.session.add(new_conversation)
            db.session.commit()
            return jsonify({'status': 'success'})
    return jsonify({'status': 'failed'})

@app.route('/process_assessment', methods=['POST'])
def process_assessment():
    data = request.get_json()
    
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    # Mapeo de preguntas a claves de evidencia
    question_to_evidence_map = {
        '¿Te sientes motivado últimamente?': 'Motivacion',
        '¿Cómo describirías tu alimentación?': 'Alimentación',
        '¿Recibes suficiente apoyo familiar?': 'Soporte Familiar',
        '¿Tienes preocupaciones académicas?': 'Preocupacion Academica',
        '¿Has tenido sentimientos suicidas?': 'Sentimientos Suicidas',
        '¿Te sientes triste con frecuencia?': 'Tristeza',
        '¿Te sientes cansado la mayor parte del tiempo?': 'Cansancio',
        '¿Tienes un hábito regular de hacer deporte?': 'Hábito Deporte',
        '¿Participas en actividades de ocio?': 'Actividades Ocio',
        '¿Tienes interacciones sociales frecuentes?': 'Interacciones Sociales',
        '¿Te sientes estresado con frecuencia?': 'Estrés'
    }
    
    assessment_evidence = {}
    for question, response in data.items():
        if question in question_to_evidence_map:
            evidence_key = question_to_evidence_map[question]
            if response.lower() in ['sí', 'buena', 'suficiente']:
                assessment_evidence[evidence_key] = 1
            else:
                assessment_evidence[evidence_key] = 0

    print('Assessment Evidence:', assessment_evidence)
    
    # Realizar la inferencia en la red bayesiana
    inference = create_bayesian_network()
    
    try:
        r1 = inference.query(variables=['Depresión'], evidence=assessment_evidence)
        r2 = inference.query(variables=['Ansiedad'], evidence=assessment_evidence)
        r3 = inference.query(variables=['Soledad'], evidence=assessment_evidence)
        r4 = inference.query(variables=['Insomnio'], evidence=assessment_evidence)
        r5 = inference.query(variables=['Salud Física'], evidence=assessment_evidence)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    responses = []
    facts = []
    
    if r1.values[1] >= 0.6:
        responses.append(f"Probabilidad de padecer Depresión: {r1.values[1] * 100:.2f}%")
        facts.append({"depresión": "alta"})
    else:
        responses.append(f"Probabilidad de padecer Depresión: {r1.values[1] * 100:.2f}%")
        facts.append({"depresión": "baja"})

    if r2.values[1] >= 0.6:
        responses.append(f"Probabilidad de padecer Ansiedad: {r2.values[1] * 100:.2f}%")
        facts.append({"ansiedad": "alta"})
    else:
        responses.append(f"Probabilidad de padecer Ansiedad: {r2.values[1] * 100:.2f}%")
        facts.append({"ansiedad": "baja"})
        
    if r3.values[1] >= 0.6:
        responses.append(f"Probabilidad de sentir Soledad: {r3.values[1] * 100:.2f}%")
        facts.append({"soledad": "si"})
    else:
        responses.append(f"Probabilidad de sentir Soledad: {r3.values[1] * 100:.2f}%")
        facts.append({"soledad": "no"})
        
    if r4.values[1] >= 0.6:
        responses.append(f"Probabilidad de padecer Insomnio: {r4.values[1] * 100:.2f}%")
        facts.append({"insomnio": "si"})
    else:    
        responses.append(f"Probabilidad de padecer Insomnio: {r4.values[1] * 100:.2f}%")
        facts.append({"insomnio": "no"})
        
    if r5.values[0] >= 0.6:
        responses.append(f"Probabilidad de tener problemas de Salud Física futuras: {r5.values[0] * 100:.2f}%")
        facts.append({"salud_fisica": "mala"})
    else:    
        responses.append(f"Probabilidad de tener problemas de Salud Física futuras: {r5.values[0] * 100:.2f}%")
        facts.append({"salud_fisica": "buena"})

    # Obtener recomendaciones del motor de inferencia
    recommendations = chatbot.get_recommendations(facts)

    return jsonify({'responses': responses + recommendations})

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        citizenship_card = request.form['citizenshipCard']
        password = request.form['password']
        
        try:
            user = User.query.filter_by(citizenshipCard=citizenship_card).first()  # Usa citizenshipCard
            
            if user and user.password == password:
                session['citizenshipCard'] = citizenship_card
                flash('¡Inicio de sesión exitoso!', 'success')
                return redirect(url_for('dashboard'))
            else:
                flash('Cédula o contraseña inválida', 'danger')
                return redirect(url_for('login'))
        except Exception as e:
            flash(str(e), 'danger')
            return redirect(url_for('login'))
    
    return render_template('login.html')

@app.route('/chatbot')
def dashboard():
    if 'citizenshipCard' in session:
        return render_template('chatbot.html')
    else:
        flash('¡No has iniciado sesión!', 'warning')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('citizenshipCard', None)
    flash('¡Has cerrado sesión!', 'info')
    return redirect(url_for('login'))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
