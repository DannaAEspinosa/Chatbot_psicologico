from experta import *
from models.bayesian_network import create_bayesian_network 

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
        handled = False
        if "estresado" in input.lower() or "tengo estres" in input.lower() or "estresada" in input.lower() or "mucho estrés" in input.lower():
            self.modify(self.facts[3], estrés="alto")
            self.declare(Fact(response="Es importante que busques técnicas de relajación y manejo del estrés."))
            handled = True
        if "triste" in input.lower() or "me siento mal" in input.lower() or "deprimida" in input.lower() or "decaído" in input.lower():
            self.modify(self.facts[2], estado_animo="triste")
            self.declare(Fact(response="Es normal sentirse triste a veces, pero si persiste, considera hablar con un profesional de salud mental."))
            handled = True
        if "feliz" in input.lower() or "contento" in input.lower() or "alegre" in input.lower():
            self.modify(self.facts[2], estado_animo="feliz")
            self.declare(Fact(response="Es genial que te sientas feliz. Sigue manteniendo un estilo de vida saludable."))
            handled = True
        if "ansioso" in input.lower() or "tengo ansiedad" in input.lower() or "nervioso" in input.lower() or "nerviosa" in input.lower():
            self.modify(self.facts[4], ansiedad="alta")
            self.declare(Fact(response="La ansiedad puede ser difícil de manejar. Intenta técnicas de respiración y relajación."))
            handled = True
        if "deprimido" in input.lower() or "tengo depresion" in input.lower() or "depresión" in input.lower() or "decaído" in input.lower():
            self.modify(self.facts[5], depresión="alta")
            self.declare(Fact(response="La depresión es una condición seria. Busca ayuda profesional si sientes que no puedes manejarlo solo."))
            handled = True
        if "insomnio" in input.lower() or "no puedo dormir" in input.lower() or "dificultad para dormir" in input.lower():
            self.modify(self.facts[6], insomnio="si")
            self.declare(Fact(response="El insomnio puede ser debilitante. Intenta establecer una rutina de sueño regular y evita la cafeína antes de dormir."))
            handled = True
        if "soporte familiar" in input.lower() or "apoyo familiar" in input.lower() or "familia" in input.lower():
            self.modify(self.facts[7], soporte_familiar="insuficiente")
            self.declare(Fact(response="El apoyo familiar es importante. Intenta comunicarte con tus seres queridos sobre cómo te sientes."))
            handled = True
        if "salud física" in input.lower() or "estado físico" in input.lower() or "salud" in input.lower():
            self.modify(self.facts[8], salud_física="mala")
            self.declare(Fact(response="Mantener una buena salud física es crucial. Intenta incorporar ejercicio y una dieta balanceada in tu rutina."))
            handled = True
        if "deporte" in input.lower() or "ejercicio" in input.lower() or "actividad física" in input.lower():
            self.modify(self.facts[9], hábito_deporte="poco")
            self.declare(Fact(response="El ejercicio regular puede mejorar tu estado de ánimo y salud general. Intenta encontrar una actividad que disfrutes."))
            handled = True
        if "ocio" in input.lower() or "pasatiempos" in input.lower() or "tiempo libre" in input.lower():
            self.modify(self.facts[10], actividades_ocio="poco")
            self.declare(Fact(response="Tener tiempo para el ocio y pasatiempos es importante para el bienestar mental. Intenta dedicar tiempo a actividades que disfrutes."))
            handled = True
        
        if not handled:
            self.declare(Fact(response="Lo siento, no tengo una respuesta específica para eso. ¿Podrías describir más tu situación?"))
        else:
            self.declare(Fact(response=f"Recibí tu entrada: {input}"))


