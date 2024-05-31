import re
from experta import *
import joblib
from models.bayesian_network import create_bayesian_network 

# Cargar el modelo entrenado
model_path = 'trained_model.pkl'
model = joblib.load(model_path)

inference = create_bayesian_network()

class PsychologicalSupport(KnowledgeEngine):

    @DefFacts()
    def initial_facts(self):
        yield Fact("Bienvenido al sistema experto de apoyo psicológico.")
        yield Fact(estado_animo="neutral")
        yield Fact(estrés="bajo")
        yield Fact(ansiedad="bajo")
        yield Fact(depresión="bajo")
        yield Fact(insomnio="no")
        yield Fact(soporte_familiar="suficiente")
        yield Fact(salud_física="buena")
        yield Fact(hábito_deporte="regular")
        yield Fact(actividades_ocio="frecuente")

    @Rule(Fact(estrés="alto"))
    def high_stress(self):
        self.declare(Fact(response="Es importante que busques técnicas de relajación y manejo del estrés."))

    @Rule(Fact(estado_animo="triste"), Fact(estrés="alto"))
    def sadness_and_stress(self):
        self.declare(Fact(response="La combinación de tristeza y estrés alto puede ser peligrosa. Considera buscar apoyo psicológico."))

    @Rule(Fact(insomnio="si"), Fact(depresión="alta"))
    def insomnia_and_depression(self):
        self.declare(Fact(response="El insomnio junto con la depresión requiere atención profesional inmediata."))

    @Rule(Fact(estado_animo="feliz"))
    def happy_mood(self):
        self.declare(Fact(response="Es genial que te sientas feliz. Sigue manteniendo un estilo de vida saludable."))

    @Rule(Fact(estrés="alto"), Fact(soporte_familiar="insuficiente"))
    def stress_and_low_support(self):
        self.declare(Fact(response="Considera buscar apoyo in amigos or profesionales para manejar tu estrés."))

    @Rule(Fact(ansiedad="alta"), salience=1)
    def manage_anxiety(self):
        result = inference.map_query(variables=['Insomnio'], evidence={'Ansiedad': 1})
        if result['Insomnio'] == 1:
            self.declare(Fact(response="Tu ansiedad alta podría estar contribuyendo a problemas de insomnio. Es recomendable buscar técnicas de manejo de la ansiedad."))
        else:
            self.declare(Fact(response="Aunque tienes ansiedad alta, no parece estar afectando tu sueño."))

    @Rule(Fact(depresión="alta"), salience=1)
    def manage_depression(self):
        result = inference.map_query(variables=['Insomnio'], evidence={'Depresión': 1})
        if result['Insomnio'] == 1:
            self.declare(Fact(response="Tu depresión alta podría estar contribuyendo a problemas de insomnio. Busca ayuda profesional."))
        else:
            self.declare(Fact(response="Aunque tienes depresión alta, no parece estar afectando tu sueño."))

    @Rule(Fact(estrés="alto"), Fact(ansiedad="alta"), salience=1)
    def high_stress_and_anxiety(self):
        result = inference.map_query(variables=['Depresión'], evidence={'Estrés': 1, 'Ansiedad': 1})
        if result['Depresión'] == 1:
            self.declare(Fact(response="El estrés y la ansiedad altos pueden llevar a la depresión. Es crucial abordar estos problemas lo antes posible."))
        else:
            self.declare(Fact(response="Aunque tienes estrés y ansiedad altos, no parece que estés desarrollando depresión, pero sigue siendo importante manejarlos."))

    @Rule(Fact(depresión="baja"), Fact(estado_animo="feliz"))
    def low_depression_and_happiness(self):
        self.declare(Fact(response="Es maravilloso que tengas un bajo nivel de depresión y te sientas feliz. Mantén tus hábitos saludables."))

    @Rule(Fact(input=MATCH.input))
    def process_user_input(self, input):
        processed_input = clean_text(input)
        prediction = model.predict([processed_input])
        self.declare(Fact(response=prediction[0]))

def clean_text(text):
    text = re.sub(r'\W', ' ', text)  # Eliminar caracteres especiales
    text = re.sub(r'\s+', ' ', text)  # Eliminar espacios adicionales
    text = text.lower()  # Convertir a minúsculas
    return text