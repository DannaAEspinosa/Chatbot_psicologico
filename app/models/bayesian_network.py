from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

def create_bayesian_network():
    model = BayesianNetwork([('Estrés', 'Ansiedad'),
                             ('Estrés', 'Depresión'),
                             ('Ansiedad', 'Insomnio'),
                             ('Depresión', 'Insomnio')])

    cpd_estrés = TabularCPD(variable='Estrés', variable_card=2, values=[[0.7], [0.3]])
    cpd_ansiedad = TabularCPD(variable='Ansiedad', variable_card=2, 
                              values=[[0.9, 0.4], [0.1, 0.6]],
                              evidence=['Estrés'], evidence_card=[2])
    cpd_depresión = TabularCPD(variable='Depresión', variable_card=2, 
                               values=[[0.9, 0.3], [0.1, 0.7]],
                               evidence=['Estrés'], evidence_card=[2])
    cpd_insomnio = TabularCPD(variable='Insomnio', variable_card=2, 
                              values=[[0.9, 0.5, 0.5, 0.1], [0.1, 0.5, 0.5, 0.9]],
                              evidence=['Ansiedad', 'Depresión'], evidence_card=[2, 2])

    model.add_cpds(cpd_estrés, cpd_ansiedad, cpd_depresión, cpd_insomnio)
    model.check_model()
    inference = VariableElimination(model)

    return inference
