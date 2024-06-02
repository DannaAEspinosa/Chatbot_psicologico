from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from .models.users import User, db  
from .chatbot.inference import PsychologicalSupport
from experta import Fact
from flask_migrate import Migrate
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
            flash('User with this citizenship card already exists', 'danger')
            return redirect(url_for('register'))
        
        # Crea un nuevo usuario
        new_user = User(citizenshipCard=citizenship_card, name=name, lastName=last_name, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')


@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    user_choice = request.form['user_choice']
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

@app.route('/start_assessment', methods=['POST'])
def start_assessment():
    questions = [
        "¿Cómo describirías tu estado de ánimo en las últimas semanas?",
        "¿Has tenido dificultades para dormir?",
        "¿Te has sentido muy ansioso o preocupado recientemente?",
        "¿Has perdido interés en actividades que solías disfrutar?",
        "¿Te sientes agotado sin motivo aparente?",
        "¿Has tenido pensamientos suicidas o de autolesión?"
    ]
    return jsonify({'questions': questions})

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        citizenship_card = request.form['citizenshipCard']
        password = request.form['password']
        
        try:
            user = User.query.filter_by(citizenshipCard=citizenship_card).first()  # Usa citizenshipCard
            
            if user and user.password == password:
                session['citizenshipCard'] = citizenship_card
                flash('Login successful!', 'success')
                return redirect(url_for('dashboard'))
            else:
                flash('Invalid citizenship card or password', 'danger')
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


if __name__ == '__main__':
    app.run(debug=True)
