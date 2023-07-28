def valida_questao(questao):

    problemas = {}

    obrig = ['titulo', 'nivel', 'opcoes', 'correta']

    for chave in obrig:
        if chave not in questao:
            problemas[chave] = 'nao_encontrado'


    if len(questao) != 4:
        problemas['outro'] = 'numero_chaves_invalido'

    if "titulo" in questao and (not questao['titulo'].strip()):
        problemas['titulo'] = 'vazio'

    if 'nivel' in questao and questao['nivel'] not in ['facil', 'medio', 'dificil']:
        problemas['nivel'] = 'valor_errado'


    if "opcoes" in questao and len(questao["opcoes"]) != 4:
        problemas["opcoes"] = "tamanho_invalido"

    elif "opcoes" in questao:
        opcoes_certas = set(['A', 'B', 'C', 'D'])

        if set(questao["opcoes"].keys()) != opcoes_certas:
            problemas["opcoes"] = "chave_invalida_ou_nao_encontrada"
        else:
            for chave, resposta in questao["opcoes"].items():
                if not resposta.strip():
                    if "opcoes" not in problemas:
                        problemas["opcoes"] = {}
                    problemas["opcoes"][chave] = "vazia"

    if "correta" in questao and questao["correta"] not in ['A', 'B', 'C', 'D']:
        problemas["correta"] = "valor_errado"

    return problemas
