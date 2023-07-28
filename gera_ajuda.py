from random import *
def gera_ajuda(questao):
    erradas = []
    ajuda = randint(1,2)
    for opcao in questao['opcoes']:
        if opcao != questao['correta']:
            erradas.append(questao['opcoes'][opcao])
    if ajuda == 1:
        e1 = choice(erradas)
        saida = f'DICA:\nOpções certamente erradas: {e1}'
    elif ajuda == 2:
        e1 = choice(erradas)
        e2 = choice(erradas)
        saida = f'DICA:\nOpções certamente erradas: {e1} | {e2}'
    return saida
    