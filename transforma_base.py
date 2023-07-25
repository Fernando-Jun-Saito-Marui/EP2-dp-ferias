#transforma_base4
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
"""
O detalhe que falta é colocar uma forma
de se houver questões nível fácil, médio ou difícil, 
adicionar ao dicionário uma chave para a dificuldade
e o valor sendo uma lista
"""
entrada = [
  {
    'titulo': 'Qual o resultado da operação 57 + 32?',
    'nivel': 'facil',
    'opcoes': {'A': '-19', 'B': '85', 'C': '89', 'D': '99'},
    'correta': 'C'
  },
  {
    'titulo': 'Qual a capital do Brasil?',
    'nivel': 'facil',
    'opcoes': {'A': 'Brasília', 'B': 'Rio de janeiro', 'C': 'São Paulo', 'D': 'Osasco'},
    'correta': 'A'
  },
  {
    'titulo': 'Quem é considerada a primeira pessoa programadora do mundo?!',
    'nivel': 'medio',
    'opcoes': {'A': 'Marie Curie', 'B': 'Alan Turing', 'C': 'Ada Lovelace', 'D': 'Edsger Dijkstra'},
    'correta': 'C'
  }
]
print(transforma_base(entrada))