import random

def sorteia_questao(questoes, nivel):
    if nivel in questoes:
        nivel_q = questoes[nivel]
        sorteada = random.choice(nivel_q)
        return sorteada
    
    return None
