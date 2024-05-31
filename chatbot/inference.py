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

   