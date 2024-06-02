from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

def create_bayesian_network():
    model = BayesianNetwork([

        ('Motivacion', 'Actividades Ocio'), 
        ('Motivacion', 'Hábito Deporte'), 
        ('Motivacion', 'Interacciones Sociales'), 

        ('Hábito Deporte', 'Salud Física'), 
        ('Alimentación', 'Salud Física'), 

        ('Interacciones Sociales', 'Soledad'), 
        ('Soporte Familiar', 'Soledad'), 

        ('Interacciones Sociales', 'Ansiedad'), 
        ('Preocupacion Academica', 'Ansiedad'), 
        ('Estrés', 'Ansiedad'),

        ('Sentimientos Suicidas', 'Depresión'), 
        ('Tristeza', 'Depresión'), 
        ('Soledad', 'Depresión'),

        ('Ansiedad', 'Insomnio'), 
        ('Depresión', 'Insomnio'), 
        ('Cansancio', 'Insomnio')
    ])

    # Definición de CPDs para cada nodo con probabilidades que tienen sentido.
    cpd_motivacion = TabularCPD(variable='Motivacion', variable_card=2, values=[[0.7], [0.3]])
    
    cpd_actividades_ocio = TabularCPD(variable='Actividades Ocio', variable_card=2, 
                                      values=[[0.9, 0.4], [0.1, 0.6]],
                                      evidence=['Motivacion'], evidence_card=[2])
    
    cpd_habito_deporte = TabularCPD(variable='Hábito Deporte', variable_card=2, 
                                    values=[[0.8, 0.3], [0.2, 0.7]],
                                    evidence=['Motivacion'], evidence_card=[2])
    
    cpd_interacciones_sociales = TabularCPD(variable='Interacciones Sociales', variable_card=2, 
                                            values=[[0.85, 0.4], [0.15, 0.6]],
                                            evidence=['Motivacion'], evidence_card=[2])
    
    cpd_alimentacion = TabularCPD(variable='Alimentación', variable_card=2, values=[[0.75], [0.25]])
    
    cpd_salud_fisica = TabularCPD(variable='Salud Física', variable_card=2, 
                                   values=[[0.9, 0.7, 0.6, 0.2], [0.1, 0.3, 0.4, 0.8]],
                                   evidence=['Hábito Deporte', 'Alimentación'], evidence_card=[2, 2])
    
    cpd_soporte_familiar = TabularCPD(variable='Soporte Familiar', variable_card=2, values=[[0.8], [0.2]])
    
    cpd_soledad = TabularCPD(variable='Soledad', variable_card=2, 
                             values=[[0.05, 0.4, 0.3, 0.8], [0.95, 0.6, 0.7, 0.2]],
                             evidence=['Interacciones Sociales', 'Soporte Familiar'], evidence_card=[2, 2])
    
    cpd_preocupacion_academica = TabularCPD(variable='Preocupacion Academica', variable_card=2, values=[[0.5], [0.5]])

    cpd_estres = TabularCPD(variable='Estrés', variable_card=2, values=[[0.6], [0.4]])
    
    
    cpd_ansiedad = TabularCPD(variable='Ansiedad', variable_card=2, 
                              values=[[0.8, 0.6, 0.7, 0.3, 0.8, 0.5, 0.6, 0.2], 
                                      [0.2, 0.4, 0.3, 0.7, 0.2, 0.5, 0.4, 0.8]],
                              evidence=['Interacciones Sociales', 'Preocupacion Academica', 'Estrés'], evidence_card=[2, 2, 2])
    
    cpd_sentimientos_suicidas = TabularCPD(variable='Sentimientos Suicidas', variable_card=2, values=[[0.95], [0.05]])
    
    cpd_tristeza = TabularCPD(variable='Tristeza', variable_card=2, values=[[0.8], [0.2]])
    
    cpd_depresion = TabularCPD(variable='Depresión', variable_card=2, 
                               values=[[0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2], 
                                       [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]],
                               evidence=['Sentimientos Suicidas', 'Tristeza', 'Soledad'], evidence_card=[2, 2, 2])
    
    cpd_cansancio = TabularCPD(variable='Cansancio', variable_card=2, values=[[0.7], [0.3]])
    
    cpd_insomnio = TabularCPD(variable='Insomnio', variable_card=2, 
                              values=[[0.9, 0.6, 0.7, 0.3, 0.8, 0.5, 0.6, 0.2], 
                                      [0.1, 0.4, 0.3, 0.7, 0.2, 0.5, 0.4, 0.8]],
                              evidence=['Ansiedad', 'Depresión', 'Cansancio'], evidence_card=[2, 2, 2])

    model.add_cpds(cpd_motivacion, cpd_actividades_ocio, cpd_habito_deporte, cpd_interacciones_sociales, 
                   cpd_alimentacion, cpd_salud_fisica, cpd_soporte_familiar, cpd_soledad, 
                   cpd_preocupacion_academica, cpd_estres, cpd_ansiedad, cpd_sentimientos_suicidas, 
                   cpd_tristeza, cpd_depresion, cpd_cansancio, cpd_insomnio)
    
    model.check_model()
    inference = VariableElimination(model)

    return inference
