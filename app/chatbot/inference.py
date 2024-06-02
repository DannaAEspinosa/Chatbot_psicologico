from experta import *
from ..models.bayesian_network import create_bayesian_network

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
        yield Fact(actividades_ocio="si")
        yield Fact(alimentacion="buena")
        yield Fact(interacciones_sociales="si")
        yield Fact(motivacion="alta")
        yield Fact(fatiga="baja")
        yield Fact(sentimientos_suicidas="no")
        yield Fact(preocupacion_academica="baja")
        yield Fact(soledad="no")

    @Rule(Fact(estrés="alto"))
    def high_stress(self):
        self.declare(Fact(response="Parece que estás lidiando con un alto nivel de estrés. Sé que puede ser abrumador, pero hay varias técnicas que pueden ayudarte a manejarlo. La meditación y el yoga son excelentes maneras de reducir el estrés y calmar la mente. Te recomiendo este [video de meditación guiada](https://www.youtube.com/watch?v=inpok4MKVLM) para empezar. También, hacer ejercicio regularmente, como caminar o nadar, puede ayudar a liberar la tensión acumulada. Si sientes que necesitas más apoyo, hablar con un profesional puede ser muy beneficioso. [Aquí puedes encontrar atención psicológica gratuita](https://www.icesi.edu.co/centros-academicos/capsi/?start=2)."))

    @Rule(Fact(estado_animo="triste"))
    def high_sadness(self):
        self.declare(Fact(response="Lamento escuchar que te sientes triste. Es importante recordar que es normal tener días malos. Hablar con amigos o familiares sobre cómo te sientes puede ser muy reconfortante. Además, dedicar tiempo a actividades que disfrutes, como leer, pintar o escuchar música, puede ayudarte a mejorar tu estado de ánimo. Aquí tienes un [video de música relajante](https://www.youtube.com/watch?v=1ZYbU82GVz4) que podría gustarte. Si la tristeza persiste, considera buscar el apoyo de un terapeuta. [Aquí puedes encontrar atención psicológica gratuita](https://www.icesi.edu.co/centros-academicos/capsi/?start=2)."))

    @Rule(Fact(estado_animo="triste"), Fact(estrés="alto"))
    def sadness_and_stress(self):
        self.declare(Fact(response="Noto que estás lidiando con tristeza y un alto nivel de estrés al mismo tiempo. Esta combinación puede ser especialmente difícil. Es crucial que te tomes un tiempo para cuidarte. Practicar técnicas de respiración y relajación puede ayudarte a calmarte. Aquí tienes un [video de técnicas de respiración](https://www.youtube.com/watch?v=aNXKjGFUlMs). Además, hablar con un terapeuta puede proporcionarte estrategias efectivas para manejar estas emociones. Recuerda que está bien pedir ayuda. [Aquí puedes encontrar atención psicológica gratuita](https://www.icesi.edu.co/centros-academicos/capsi/?start=2)."))

    @Rule(Fact(insomnio="si"))
    def high_insomnia(self):
        self.declare(Fact(response="Parece que estás teniendo problemas para dormir. El insomnio puede afectar seriamente tu bienestar. Intenta establecer una rutina de sueño regular, y evita el uso de dispositivos electrónicos al menos una hora antes de dormir. Un ambiente oscuro y tranquilo puede mejorar la calidad del sueño. Aquí tienes un [video con sonidos relajantes](https://www.youtube.com/watch?v=vs2U6BvZ4U4) que podría ayudarte a dormir mejor. Si el insomnio persiste, te recomendaría hablar con un profesional de la salud. [Aquí puedes encontrar atención psicológica gratuita](https://www.icesi.edu.co/centros-academicos/capsi/?start=2)."))

    @Rule(Fact(insomnio="si"), Fact(depresión="alta"))
    def insomnia_and_depression(self):
        self.declare(Fact(response="El insomnio junto con la depresión es una combinación que requiere atención inmediata. Es vital que busques ayuda profesional lo antes posible. Un terapeuta puede ofrecerte estrategias específicas para manejar estos síntomas. Además, mantener una rutina diaria y evitar la cafeína en la tarde puede mejorar tu sueño. Aquí tienes un [video sobre técnicas para mejorar el sueño](https://www.youtube.com/watch?v=inpok4MKVLM). No estás solo/a, hay recursos y personas dispuestas a ayudarte. [Aquí puedes encontrar atención psicológica gratuita](https://www.icesi.edu.co/centros-academicos/capsi/?start=2)."))

    @Rule(Fact(salud_física="mala"))
    def poor_physical_health(self):
        self.declare(Fact(response="Veo que tu salud física no está en su mejor estado. Es fundamental cuidar de nuestro cuerpo para mantener también una buena salud mental. Intenta incorporar ejercicio regular en tu rutina diaria, aunque sea una caminata corta. Además, una dieta balanceada rica en frutas y verduras puede marcar una gran diferencia. Aquí tienes un [video sobre alimentación saludable](https://www.youtube.com/watch?v=vs2U6BvZ4U4). No dudes en consultar a un profesional de la salud para obtener más orientación."))

    @Rule(Fact(estado_animo="feliz"))
    def happy_mood(self):
        self.declare(Fact(response="Me alegra saber que te sientes feliz. Mantén esos buenos hábitos que te han llevado a este estado. Continúa cuidando de tu salud física y mental, y sigue disfrutando de tus actividades favoritas. Es un excelente momento para compartir tu felicidad con los demás y fortalecer tus relaciones sociales. ¡Sigue así!"))

    @Rule(Fact(soporte_familiar="insuficiente"))
    def low_support(self):
        self.declare(Fact(response="Noto que sientes que el apoyo familiar es insuficiente. Es importante comunicarte con tus seres queridos sobre cómo te sientes. A veces, las personas no saben cómo apoyar hasta que se lo decimos. Busca actividades que puedan disfrutar juntos, como una cena familiar o una salida al parque. Si sientes que necesitas más apoyo, no dudes en buscar grupos de apoyo o hablar con un terapeuta. Aquí tienes un [video sobre la importancia del apoyo familiar](https://www.youtube.com/watch?v=bDQ-HAwhrl4)."))

    @Rule(Fact(ansiedad="alta"), salience=1)
    def manage_anxiety(self):
        self.declare(Fact(response="Parece que estás lidiando con un alto nivel de ansiedad. La ansiedad puede ser difícil de manejar, pero hay varias estrategias que pueden ayudarte. Intenta técnicas de respiración y relajación, como la respiración profunda y la meditación. Aquí tienes un [video sobre técnicas de relajación](https://www.youtube.com/watch?v=aNXKjGFUlMs). Además, llevar un diario donde anotes tus pensamientos puede ayudarte a procesarlos mejor. Si la ansiedad persiste, considera hablar con un profesional. [Aquí puedes encontrar atención psicológica gratuita](https://www.icesi.edu.co/centros-academicos/capsi/?start=2)."))

    @Rule(Fact(depresión="alta"), salience=1)
    def manage_depression(self):
        self.declare(Fact(response="Noto que estás lidiando con una alta depresión. La depresión es una condición seria, y es importante que busques ayuda profesional si sientes que no puedes manejarlo solo/a. Hablar con un terapeuta puede ser muy beneficioso. Además, intenta mantener una rutina diaria y realizar actividades que disfrutes, aunque sea difícil.Recuerda que no estás solo/a, y hay ayuda disponible para ti. [Aquí puedes encontrar atención psicológica gratuita](https://www.icesi.edu.co/centros-academicos/capsi/?start=2)."))

    @Rule(Fact(hábito_deporte="poco"))
    def low_exercise(self):
        self.declare(Fact(response="Veo que no haces mucho ejercicio. La actividad física regular es crucial para mejorar tu estado de ánimo y salud general. Intenta encontrar una actividad física que disfrutes, como caminar, nadar o bailar, y hazla parte de tu rutina diaria. Aquí tienes un [video sobre los beneficios del ejercicio](https://www.youtube.com/watch?v=8GBpkWOk0bs)."))

    @Rule(Fact(actividades_ocio="poco"))
    def low_leisure_activities(self):
        self.declare(Fact(response="Noto que no estás dedicando mucho tiempo a actividades de ocio. Tener tiempo para el ocio y los pasatiempos es importante para tu bienestar mental. Intenta dedicar tiempo a actividades que disfrutes, como leer, pintar o escuchar música. Aquí tienes información sobre [Actividades o hobbies](https://psicologiaymente.com/social/hobbies-para-hacer-en-casa)."))

    @Rule(Fact(alimentacion="mala"))
    def poor_diet(self):
        self.declare(Fact(response="Parece que tu alimentación no es la mejor. Una dieta balanceada es crucial para tu salud mental y física. Intenta mejorar tus hábitos alimenticios incluyendo más frutas y verduras en tu dieta. Aquí tienes un [video sobre alimentación saludable](https://www.youtube.com/watch?v=vs2U6BvZ4U4&t=20s)."))

    @Rule(Fact(interacciones_sociales="poco"))
    def low_social_interactions(self):
        self.declare(Fact(response="Noto que no tienes muchas interacciones sociales. Las interacciones sociales son importantes para tu bienestar emocional. Intenta pasar tiempo con amigos y familiares, o únete a grupos o clubes que te interesen. Aquí tienes un [video sobre la importancia de las relaciones sociales](https://www.youtube.com/watch?v=eZJ46ab0S_o)."))

    @Rule(Fact(motivacion="baja"))
    def low_motivation(self):
        self.declare(Fact(response="Parece que te sientes desmotivado/a. Sentirse desmotivado puede ser una señal de estrés o depresión. Intenta establecer pequeñas metas diarias y recompénsate por lograrlas. Aquí tienes un [video sobre cómo aumentar la motivación](https://www.youtube.com/watch?v=On5HMOwvy9o). Si necesitas más apoyo, considera hablar con un profesional. [Aquí puedes encontrar atención psicológica gratuita](https://www.icesi.edu.co/centros-academicos/capsi/?start=2)."))

    @Rule(Fact(fatiga="alta"))
    def high_fatigue(self):
        self.declare(Fact(response="Veo que te sientes muy fatigado/a. La fatiga puede ser un signo de problemas de salud física o mental. Asegúrate de descansar lo suficiente y mantener una buena rutina de sueño. Aquí tienes un [video sobre cómo combatir la fatiga](https://www.youtube.com/watch?v=YNwrqOdlrxE). Si la fatiga persiste, consulta a un profesional de la salud."))

    @Rule(Fact(sentimientos_suicidas="si"))
    def suicidal_thoughts(self):
        self.declare(Fact(response="Por favor, busca ayuda inmediata de un profesional de salud mental o llama a la línea de ayuda '123'. Tu vida es valiosa y hay personas dispuestas a ayudarte. No enfrentes esto solo/a. [Aquí puedes encontrar atención psicológica gratuita](https://www.icesi.edu.co/centros-academicos/capsi/?start=2)."))

    @Rule(Fact(preocupacion_academica="alta"))
    def high_academic_stress(self):
        self.declare(Fact(response="Veo que el estrés académico es un gran desafío para ti. Intenta organizar tu tiempo de manera efectiva y establecer un horario de estudio. Aquí tienes un [video sobre técnicas de estudio](https://www.youtube.com/watch?v=Bnlp1EWDqdU). Si necesitas más ayuda, no dudes en buscar apoyo en tutores o compañeros de clase."))

    @Rule(Fact(soledad="si"))
    def feeling_lonely(self):
        self.declare(Fact(response="Noto que te sientes solo/a. La soledad puede afectar tu bienestar emocional. Intenta conectar con amigos o participar en actividades sociales. Aquí tienes un [video sobre cómo combatir la soledad](https://www.youtube.com/watch?v=kPqvrcm8hWM). Si sientes que necesitas más apoyo, considera hablar con un terapeuta. [Aquí puedes encontrar atención psicológica gratuita](https://www.icesi.edu.co/centros-academicos/capsi/?start=2)."))

    @Rule(Fact(estrés="alto"), Fact(ansiedad="alta"), salience=1)
    def high_stress_and_anxiety(self):
        result = inference.map_query(variables=['Depresión'], evidence={'Estrés': 1, 'Ansiedad': 1})
        if result['Depresión'] == 1:
            self.declare(Fact(response="El estrés y la ansiedad altos pueden llevar a la depresión. Es crucial abordar estos problemas lo antes posible. Intenta practicar técnicas de relajación y busca el apoyo de un profesional. Aquí tienes un [video sobre cómo manejar el estrés y la ansiedad](https://www.youtube.com/watch?v=w2wxI5iHDgs). [Aquí puedes encontrar atención psicológica gratuita](https://www.icesi.edu.co/centros-academicos/capsi/?start=2)."))
        else:
            self.declare(Fact(response="Aunque tienes estrés y ansiedad altos, no parece que estés desarrollando depresión, pero sigue siendo importante manejarlos. Intenta técnicas de relajación y busca apoyo si es necesario. Aquí tienes un [video sobre cómo manejar el estrés y la ansiedad](https://www.youtube.com/watch?v=w2wxI5iHDgs)."))

    @Rule(Fact(depresión="baja"), Fact(estado_animo="feliz"))
    def low_depression_and_happiness(self):
        self.declare(Fact(response="Es maravilloso saber que tienes un bajo nivel de depresión y te sientes feliz. Mantén tus hábitos saludables y sigue cuidando de tu bienestar emocional. Comparte tu felicidad con los demás y fortalece tus relaciones sociales. ¡Sigue así!"))

    @Rule(Fact(estrés="alto"), Fact(ansiedad="alta"))
    def high_stress_and_anxiety(self):
        self.declare(Fact(response="El estrés y la ansiedad altos pueden ser una combinación difícil de manejar. Es importante que te tomes un tiempo para relajarte y practiques técnicas de manejo del estrés. Aquí tienes un [video sobre técnicas de relajación](https://www.youtube.com/watch?v=aNXKjGFUlMs). Si sientes que necesitas más apoyo, no dudes en hablar con un profesional. [Aquí puedes encontrar atención psicológica gratuita](https://www.icesi.edu.co/centros-academicos/capsi/?start=2)."))

    @Rule(Fact(estado_animo="triste"), Fact(depresión="alta"))
    def sadness_and_high_depression(self):
        self.declare(Fact(response="La tristeza y la alta depresión son señales de que necesitas apoyo inmediato. Es esencial que busques ayuda profesional para manejar estos sentimientos.[Aquí puedes encontrar atención psicológica gratuita](https://www.icesi.edu.co/centros-academicos/capsi/?start=2)."))

    @Rule(Fact(insomnio="si"), Fact(fatiga="alta"))
    def insomnia_and_high_fatigue(self):
        self.declare(Fact(response="El insomnio y la alta fatiga pueden afectar gravemente tu bienestar. Establecer una rutina de sueño y practicar técnicas de relajación puede ayudarte a mejorar la calidad del sueño. Aquí tienes un [video sobre cómo mejorar el sueño](https://www.youtube.com/watch?v=ks03wMzEQC0). Si los problemas persisten, busca ayuda profesional. [Aquí puedes encontrar atención psicológica gratuita](https://www.icesi.edu.co/centros-academicos/capsi/?start=2)."))

    @Rule(Fact(soporte_familiar="insuficiente"), Fact(soledad="si"))
    def low_support_and_loneliness(self):
        self.declare(Fact(response="La falta de apoyo familiar y la soledad pueden ser muy difíciles de manejar. Es importante comunicarte con tus seres queridos y buscar actividades sociales. Aquí tienes un [Guía sobre cómo comunicarse mejor con tu familia(https://psicologiaymente.com/social/como-comunicarnos-mejor-con-familia). Si necesitas más apoyo, considera hablar con un terapeuta. [Aquí puedes encontrar atención psicológica gratuita](https://www.icesi.edu.co/centros-academicos/capsi/?start=2)."))

    @Rule(Fact(alimentacion="mala"), Fact(salud_física="mala"))
    def poor_diet_and_physical_health(self):
        self.declare(Fact(response="Una mala alimentación y una salud física deficiente pueden afectar tu bienestar general. Intenta mejorar tus hábitos alimenticios y hacer ejercicio regularmente. Aquí tienes un [Guía para mantener habitos saludables](https://vidasaludable.udec.cl/node/239). Si necesitas más orientación, consulta a un profesional de la salud."))

    @Rule(Fact(actividades_ocio="poco"), Fact(motivacion="baja"))
    def low_leisure_and_motivation(self):
        self.declare(Fact(response="La falta de actividades de ocio y baja motivación pueden afectar tu bienestar emocional. Intenta dedicar tiempo a pasatiempos que disfrutes y establece pequeñas metas diarias para mantenerte motivado/a. Aquí tienes un [video sobre cómo aumentar la motivación](https://www.youtube.com/watch?v=mb6UAPGTvIU)."))

    @Rule(Fact(estrés="alto"), Fact(fatiga="alta"))
    def high_stress_and_fatigue(self):
        self.declare(Fact(response="El alto estrés y la fatiga pueden ser una combinación agotadora. Es importante que te tomes un tiempo para descansar y practiques técnicas de manejo del estrés. Aquí tienes un [video sobre cómo combatir la fatiga](https://www.youtube.com/watch?v=YNwrqOdlrxE). Si sientes que necesitas más apoyo, habla con un profesional. [Aquí puedes encontrar atención psicológica gratuita](https://www.icesi.edu.co/centros-academicos/capsi/?start=2)."))

    @Rule(Fact(ansiedad="alta"), Fact(preocupacion_academica="alta"))
    def high_anxiety_and_academic_stress(self):
        self.declare(Fact(response="La alta ansiedad y el estrés académico pueden ser difíciles de manejar juntos. Intenta organizar tu tiempo de manera efectiva y practica técnicas de relajación. Aquí tienes un [video sobre Cómo manejar la ansiedad en la universidad](https://www.youtube.com/watch?v=Ctd3gH4O4Bc). Si necesitas más ayuda, busca apoyo en tutores o compañeros de clase y considera hablar con un profesional. [Aquí puedes encontrar atención psicológica gratuita](https://www.icesi.edu.co/centros-academicos/capsi/?start=2)."))

    @Rule(Fact(depresión="alta"), Fact(fatiga="alta"))
    def high_depression_and_fatigue(self):
        self.declare(Fact(response="La alta depresión y la fatiga pueden ser una combinación peligrosa. Es esencial que busques ayuda profesional para manejar estos síntomas. [Aquí puedes encontrar atención psicológica gratuita](https://www.icesi.edu.co/centros-academicos/capsi/?start=2)."))

    @Rule(Fact(sentimientos_suicidas="si"), Fact(depresión="alta"))
    def suicidal_thoughts_and_depression(self):
        self.declare(Fact(response="Por favor, busca ayuda inmediata de un profesional de salud mental o llama a la línea de ayuda '123'. La combinación de pensamientos suicidas y alta depresión requiere atención urgente. Tu vida es valiosa y hay personas dispuestas a ayudarte. No enfrentes esto solo/a. [Aquí puedes encontrar atención psicológica gratuita](https://www.icesi.edu.co/centros-academicos/capsi/?start=2)."))

    @Rule(Fact(soporte_familiar="suficiente"), Fact(interacciones_sociales="frecuente"))
    def good_support_and_social_interactions(self):
        self.declare(Fact(response="Es excelente saber que tienes suficiente apoyo familiar y frecuentes interacciones sociales. Mantén estos hábitos, ya que son muy beneficiosos para tu bienestar emocional. Sigue disfrutando de tu tiempo con seres queridos y fortaleciendo tus relaciones. ¡Sigue así!"))

    @Rule(Fact(hábito_deporte="poco"), Fact(salud_física="mala"))
    def low_exercise_and_poor_health(self):
        self.declare(Fact(response="La falta de ejercicio y una salud física deficiente pueden afectar tu bienestar general. Intenta incorporar más actividad física en tu rutina diaria y mejorar tu alimentación. Aquí tienes un [video sobre cómo empezar a hacer ejercicio](https://www.youtube.com/watch?v=UItWltVZZmE)."))

    @Rule(Fact(motivacion="baja"), Fact(estado_animo="triste"))
    def low_motivation_and_sadness(self):
        self.declare(Fact(response="La baja motivación y sentirte triste pueden ser señales de que necesitas apoyo adicional. Intenta establecer pequeñas metas diarias para mantenerte motivado/a. Aquí tienes un [video sobre cómo aumentar la motivación](https://www.youtube.com/watch?v=On5HMOwvy9o)."))

    @Rule(Fact(fatiga="alta"), Fact(salud_física="mala"))
    def high_fatigue_and_poor_health(self):
        self.declare(Fact(response="La alta fatiga y una salud física deficiente pueden afectar gravemente tu bienestar. Asegúrate de descansar lo suficiente y mejorar tus hábitos alimenticios. Aquí tienes un [video sobre cómo combatir la fatiga](https://www.youtube.com/watch?v=YNwrqOdlrxE)."))

    @Rule(Fact(ansiedad="alta"), Fact(fatiga="alta"))
    def high_anxiety_and_fatigue(self):
        self.declare(Fact(response="La alta ansiedad y la fatiga pueden ser una combinación agotadora. Practicar técnicas de relajación y asegurarte de descansar lo suficiente puede ayudarte a sentirte mejor. Aquí tienes un [video sobre técnicas de relajación](https://www.youtube.com/watch?v=aNXKjGFUlMs)."))

    @Rule(Fact(salud_física="mala"), Fact(alimentacion="mala"), Fact(hábito_deporte="poco"))
    def high_physical_health_risk(self):
        self.declare(Fact(response="Veo que tienes una mala salud física, una alimentación inadecuada y haces poco ejercicio. Esto puede aumentar el riesgo de problemas de salud físicos. Te recomiendo mejorar tu dieta y aumentar tu actividad física. Aquí tienes un [video sobre hábitos saludables](https://www.youtube.com/watch?v=vs2U6BvZ4U4)."))

    @Rule(Fact(estrés="alto"), Fact(estado_animo="triste"), Fact(ansiedad="alta"), Fact(depresión="alta"))
    def poor_mental_state(self):
        self.declare(Fact(response="Parece que estás experimentando altos niveles de estrés, tristeza, ansiedad y depresión. Es importante buscar ayuda profesional para manejar estos sentimientos. Aquí tienes un [video sobre técnicas para mejorar la salud mental](https://www.youtube.com/watch?v=w2wxI5iHDgs)."))

    @Rule(Fact(interacciones_sociales="poco"), Fact(soledad="si"))
    def poor_social_relationships(self):
        self.declare(Fact(response="Observo que tienes pocas interacciones sociales y te sientes solo/a. Intenta conectar más con amigos o participar en actividades grupales. Aquí tienes un [video sobre cómo mejorar las relaciones sociales](https://www.youtube.com/watch?v=eZJ46ab0S_o)."))

    @Rule(Fact(insomnio="si"), Fact(fatiga="alta"))
    def poor_sleep_quality(self):
        self.declare(Fact(response="Parece que tienes problemas para dormir y te sientes muy fatigado/a. Te recomiendo establecer una rutina de sueño y evitar el uso de dispositivos electrónicos antes de dormir. Aquí tienes un [video sobre cómo mejorar la calidad del sueño](https://www.youtube.com/watch?v=ks03wMzEQC0)."))
    
    @Rule(Fact(estado_animo="feliz"), Fact(interacciones_sociales="frecuente"), Fact(soporte_familiar="suficiente"))
    def high_general_satisfaction(self):
        self.declare(Fact(response="Observo que te sientes feliz y tienes buenas interacciones sociales y apoyo familiar. Es excelente que mantengas estos hábitos. Sigue cuidando de tu bienestar y fortaleciendo tus relaciones. ¡Sigue así!"))

    @Rule(Fact(estrés="alto"), Fact(ansiedad="alta"), Fact(insomnio="si"))
    def high_burnout_risk(self):
        self.declare(Fact(response="Noto que tienes un alto nivel de estrés, ansiedad y problemas para dormir, lo cual puede indicar un riesgo de burnout. Te recomiendo tomar medidas para reducir el estrés y mejorar tu calidad de sueño. Aquí tienes un [video sobre cómo manejar el burnout](https://www.youtube.com/watch?v=bzjWzzrbQWk)."))


    @Rule(Fact(input=MATCH.input))
    def process_user_input(self, input):
        handled = False
        if any(word in input.lower() for word in ["estresado", "tengo estrés", "estresada", "mucho estrés", "estres", "estresante", "estresarme", "me siento estresado", "me siento estresada"]):
            self.modify(self.facts[3], estrés="alto")
            handled = True
        if any(word in input.lower() for word in ["mal","triste", "me siento mal", "deprimida", "decaído", "decaída", "depresivo", "desanimado", "desanimada", "melancólico", "melancólica", "abatido", "abatida"]):
            self.modify(self.facts[2], estado_animo="triste")
            handled = True
        if any(word in input.lower() for word in ["bien","feliz", "contento", "contenta", "alegre", "animado", "animada", "eufórico", "eufórica", "satisfecho", "satisfecha"]):
            self.modify(self.facts[2], estado_animo="feliz")
            handled = True
        if any(word in input.lower() for word in ["ansioso", "tengo ansiedad", "nervioso", "nerviosa", "ansiedad", "inquieto", "inquieta", "preocupado", "preocupada", "angustiado", "angustiada"]):
            self.modify(self.facts[4], ansiedad="alta")
            handled = True
        if any(word in input.lower() for word in ["deprimido", "tengo depresión", "depresión", "decaído", "desmotivado", "sin ánimos", "abatido", "desesperanzado", "sin esperanza", "abatida", "desesperanzada"]):
            self.modify(self.facts[5], depresión="alta")
            handled = True
        if any(word in input.lower() for word in ["insomnio", "no puedo dormir", "dificultad para dormir", "sueño interrumpido", "me cuesta dormir", "problemas de sueño", "no duermo bien"]):
            self.modify(self.facts[6], insomnio="si")
            handled = True
        if any(word in input.lower() for word in ["soporte familiar", "apoyo familiar", "familia", "relaciones familiares", "apoyo de mi familia", "mi familia no me apoya", "problemas familiares"]):
            self.modify(self.facts[7], soporte_familiar="insuficiente")
            handled = True
        if any(word in input.lower() for word in ["salud física", "estado físico", "salud", "me siento enfermo", "me siento débil", "enfermedad", "problemas de salud", "me siento mal físicamente"]):
            self.modify(self.facts[8], salud_física="mala")
            handled = True
        if any(word in input.lower() for word in ["deporte", "ejercicio", "actividad física", "hacer ejercicio", "entrenar", "no hago ejercicio", "poco ejercicio", "no me muevo mucho", "sedentario", "sedentaria"]):
            self.modify(self.facts[9], hábito_deporte="poco")
            handled = True
        if any(word in input.lower() for word in ["ocio", "pasatiempos", "tiempo libre", "hobbies", "actividades recreativas", "no tengo tiempo libre", "no hago nada divertido"]):
            self.modify(self.facts[10], actividades_ocio="poco")
            handled = True
        if any(word in input.lower() for word in ["alimentación", "dieta", "comida", "hábitos alimenticios", "nutrición", "mala alimentación", "como mal", "no como bien", "dieta poco saludable"]):
            self.modify(self.facts[11], alimentacion="mala")
            handled = True
        if any(word in input.lower() for word in ["interacciones sociales", "vida social", "amigos", "socializar", "relaciones sociales", "no tengo amigos", "me siento solo", "me siento sola", "no socializo"]):
            self.modify(self.facts[12], interacciones_sociales="poco")
            handled = True
        if any(word in input.lower() for word in ["desmotivado", "sin motivación", "perdí el interés", "sin ánimo", "falta de interés", "no tengo ganas de hacer nada", "no me siento motivado", "no me siento motivada"]):
            self.modify(self.facts[13], motivacion="baja")
            handled = True
        if any(word in input.lower() for word in ["cansado", "fatigado", "sin energía", "agotado", "cansancio extremo", "me siento exhausto", "me siento exhausta", "no tengo energía", "me siento fatigado", "me siento fatigada"]):
            self.modify(self.facts[14], fatiga="alta")
            handled = True
        if any(word in input.lower() for word in ["suicidio", "quiero morir", "quiero matarme", "sin sentido vivir", "terminar mi vida", "no quiero vivir", "me quiero suicidar", "me quiero matar", "pensamientos suicidas"]):
            self.modify(self.facts[15], sentimientos_suicidas="si")
            handled = True
        if not handled:
            self.declare(Fact(response="Lo siento, no tengo una respuesta específica para eso. ¿Podrías describir más tu situación?"))