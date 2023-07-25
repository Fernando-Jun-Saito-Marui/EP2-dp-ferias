#3
def transforma_base(questoes):
    lista_questoes = {}
    for q in questoes:
        if q['nivel'] == 'facil':
            lista_questoes['facil'] = []
            lista_questoes['facil'].append(q)
        elif q['nivel'] == 'medio':
            lista_questoes['medio'] = []
            lista_questoes['medio'].append(q)
        elif q['nivel'] == 'dificil':
            lista_questoes['dificil'] = []
            lista_questoes['dificil'].append(q)
    return lista_questoes
