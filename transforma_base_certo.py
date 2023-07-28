def transforma_base(questoes):
    lista_questoes = {}

    for q in questoes:
        dificuldade = q["nivel"]

        if dificuldade in lista_questoes:
            lista_questoes[dificuldade].append(q)
        else:
            lista_questoes[dificuldade] = [q]

    return lista_questoes