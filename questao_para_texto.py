def questao_para_texto(questao,id):
    titulo = questao['titulo']
    A = questao['opcoes']['A']
    B = questao['opcoes']['B']
    C = questao['opcoes']['C']
    D = questao['opcoes']['D']
    saida = f'----------------------------------------\nQUESTAO {id}\n\n{titulo}\n\nRESPOSTAS:\nA: {A}\nB: {B}\nC: {C}\nD: {D}\n'
    return saida
