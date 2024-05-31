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
        yield Fact(alimentacion="buena")
        yield Fact(interacciones_sociales="frecuente")
        yield Fact(motivacion="alta")
        yield Fact(fatiga="baja")
        yield Fact(sentimientos_suicidas="no")
        yield Fact(preocupacion_academica="baja")
        yield Fact(soledad="no")

    @Rule(Fact(estrés="alto"))
    def high_stress(self):
        self.declare(Fact(response="Es importante que busques técnicas de relajación y manejo del estrés, como la meditación or el yoga."))

    @Rule(Fact(estado_animo="triste"))
    def high_sadness(self):
        self.declare(Fact(response="Es normal sentirse triste a veces. Hablar con amigos or familiares puede ayudarte a sentirte mejor."))

    @Rule(Fact(estado_animo="triste"), Fact(estrés="alto"))
    def sadness_and_stress(self):
        self.declare(Fact(response="La combinación de tristeza y estrés alto puede ser peligrosa. Considera buscar apoyo psicológico."))

    @Rule(Fact(insomnio="si"))
    def high_insomnia(self):
        self.declare(Fact(response="El insomnio puede ser debilitante. Intenta establecer una rutina de sueño regular y evitar el uso de dispositivos electrónicos antes de dormir."))

    @Rule(Fact(insomnio="si"), Fact(depresión="alta"))
    def insomnia_and_depression(self):
        self.declare(Fact(response="El insomnio junto con la depresión requiere atención profesional inmediata. Busca ayuda lo antes posible."))

    @Rule(Fact(salud_física="mala"))
    def poor_physical_health(self):
        self.declare(Fact(response="Mantener una buena salud física es crucial. Intenta incorporar ejercicio y una dieta balanceada in tu rutina diaria."))

    @Rule(Fact(estado_animo="feliz"))
    def happy_mood(self):
        self.declare(Fact(response="Es genial que te sientas feliz. Sigue manteniendo un estilo de vida saludable y equilibrado."))

    @Rule(Fact(soporte_familiar="insuficiente"))
    def low_support(self):
        self.declare(Fact(response="El apoyo familiar es importante. Intenta comunicarte con tus seres queridos sobre cómo te sientes y busca actividades que puedan disfrutar juntos."))

    @Rule(Fact(ansiedad="alta"), salience=1)
    def manage_anxiety(self):
        self.declare(Fact(response="La ansiedad puede ser difícil de manejar. Intenta técnicas de respiración y relajación, y considera hablar con un profesional si la ansiedad persiste."))

    @Rule(Fact(depresión="alta"), salience=1)
    def manage_depression(self):
        self.declare(Fact(response="La depresión es una condición seria. Busca ayuda profesional si sientes que no puedes manejarlo solo. Hablar con un terapeuta puede ser muy beneficioso."))

    