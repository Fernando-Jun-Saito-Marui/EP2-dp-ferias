import sorteia_questao
def sorteia_questao_inedita(questoes,nivel,questoes_sorteadas):
    x = sorteia_questao(questoes,nivel)
    for q in questoes_sorteadas:
        if q == x:
            x = sorteia_questao(questoes,nivel)#sorteia dnv
    questoes_sorteadas.append(x)
    return x
