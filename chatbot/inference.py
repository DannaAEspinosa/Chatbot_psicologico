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

    @Rule(Fact(hábito_deporte="poco"))
    def low_exercise(self):
        self.declare(Fact(response="El ejercicio regular puede mejorar tu estado de ánimo y salud general. Intenta encontrar una actividad física que disfrutes y hazla parte de tu rutina."))

    @Rule(Fact(actividades_ocio="poco"))
    def low_leisure_activities(self):
        self.declare(Fact(response="Tener tiempo para el ocio y los pasatiempos es importante para el bienestar mental. Intenta dedicar tiempo a actividades que disfrutes, como leer, pintar or escuchar música."))

    @Rule(Fact(alimentacion="mala"))
    def poor_diet(self):
        self.declare(Fact(response="Una alimentación balanceada es crucial para tu salud mental y física. Intenta mejorar tus hábitos alimenticios incluyendo más frutas y verduras in tu dieta."))

    @Rule(Fact(interacciones_sociales="poco"))
    def low_social_interactions(self):
        self.declare(Fact(response="Las interacciones sociales son importantes para tu bienestar emocional. Intenta pasar tiempo con amigos y familiares, or únete a grupos or clubes que te interesen."))

    @Rule(Fact(motivacion="baja"))
    def low_motivation(self):
        self.declare(Fact(response="Sentirse desmotivado puede ser una señal de estrés or depresión. Intenta establecer pequeñas metas diarias y buscar apoyo si es necesario."))

    @Rule(Fact(fatiga="alta"))
    def high_fatigue(self):
        self.declare(Fact(response="La fatiga puede ser un signo de problemas de salud física or mental. Asegúrate de descansar lo suficiente y consulta a un profesional si la fatiga persiste."))

    @Rule(Fact(sentimientos_suicidas="si"))
    def suicidal_thoughts(self):
        self.declare(Fact(response="Los pensamientos suicidas son muy serios. Por favor, busca ayuda inmediata de un profesional de salud mental or llama a una línea de ayuda."))

    @Rule(Fact(preocupacion_academica="alta"))
    def high_academic_stress(self):
        self.declare(Fact(response="El estrés académico puede ser muy desafiante. Intenta organizar tu tiempo y buscar ayuda in tutores or compañeros de clase."))

    @Rule(Fact(soledad="si"))
    def feeling_lonely(self):
        self.declare(Fact(response="La soledad puede afectar tu bienestar emocional. Intenta conectar con amigos or participar in actividades sociales."))

    @Rule(Fact(estrés="alto"), Fact(ansiedad="alta"), salience=1)
    def high_stress_and_anxiety(self):
        result = inference.map_query(variables=['Depresión'], evidence={'Estrés': 1, 'Ansiedad': 1})
        if result['Depresión'] == 1:
            self.declare(Fact(response="El estrés y la ansiedad altos pueden llevar a la depresión. Es crucial abordar estos problemas lo antes posible."))
        else:
            self.declare(Fact(response="Aunque tienes estrés y ansiedad altos, no parece que estés desarrollando depresión, pero sigue siendo importante manejarlos."))

    @Rule(Fact(depresión="baja"), Fact(estado_animo="feliz"))
    def low_depression_and_happiness(self):
        self.declare(Fact(response="Es maravilloso que tengas un bajo nivel de depresión y te sientas feliz. Mantén tus hábitos saludables y sigue cuidando de tu bienestar emocional."))

    @Rule(Fact(input=MATCH.input))
    def process_user_input(self, input):
        handled = False
        if "estresado" in input.lower() or "tengo estres" in input.lower() or "estresada" in input.lower() or "mucho estrés" in input.lower():
            self.modify(self.facts[3], estrés="alto")
            handled = True
        if "triste" in input.lower() or "me siento mal" in input.lower() or "deprimida" in input.lower() or "decaído" in input.lower():
            self.modify(self.facts[2], estado_animo="triste")
            handled = True
        if "feliz" in input.lower() or "contento" in input.lower() or "alegre" in input.lower():
            self.modify(self.facts[2], estado_animo="feliz")
            handled = True
        if "ansioso" in input.lower() or "tengo ansiedad" in input.lower() or "nervioso" in input.lower() or "nerviosa" in input.lower():
            self.modify(self.facts[4], ansiedad="alta")
            handled = True
        if "deprimido" in input.lower() or "tengo depresion" in input.lower() or "depresión" in input.lower() or "decaído" in input.lower():
            self.modify(self.facts[5], depresión="alta")
            handled = True
        if "insomnio" in input.lower() or "no puedo dormir" in input.lower() or "dificultad para dormir" in input.lower():
            self.modify(self.facts[6], insomnio="si")
            handled = True
        if "soporte familiar" in input.lower() or "apoyo familiar" in input.lower() or "familia" in input.lower():
            self.modify(self.facts[7], soporte_familiar="insuficiente")
            handled = True
        if "salud física" in input.lower() or "estado físico" in input.lower() or "salud" in input.lower():
            self.modify(self.facts[8], salud_física="mala")
            handled = True
        if "deporte" in input.lower() or "ejercicio" in input.lower() or "actividad física" in input.lower():
            self.modify(self.facts[9], hábito_deporte="poco")
            handled = True
        if "ocio" in input.lower() or "pasatiempos" in input.lower() or "tiempo libre" in input.lower():
            self.modify(self.facts[10], actividades_ocio="poco")
            handled = True
        if "alimentacion" in input.lower() or "dieta" in input.lower() or "comida" in input.lower():
            self.modify(self.facts[11], alimentacion="mala")
            handled = True
        if "interacciones sociales" in input.lower() or "vida social" in input.lower() or "amigos" in input.lower():
            self.modify(self.facts[12], interacciones_sociales="poco")
            handled = True
        if "desmotivado" in input.lower() or "sin motivación" in input.lower() or "perdí el interés" in input.lower() or "sin animo" in input.lower():
            self.modify(self.facts[13], motivacion="baja")
            handled = True
        if "cansado" in input.lower() or "fatigado" in input.lower() or "sin energía" in input.lower():
            self.modify(self.facts[14], fatiga="alta")
            handled = True
        if "suicidio" in input.lower() or "quiero morir" in input.lower() or "quiero matarme" in input.lower() or "sin sentido vivir" in input.lower():
            self.modify(self.facts[15], sentimientos_suicidas="si")
            handled = True
        if not handled:
            self.declare(Fact(response="Lo siento, no tengo una respuesta específica para eso. ¿Podrías describir más tu situación?"))
