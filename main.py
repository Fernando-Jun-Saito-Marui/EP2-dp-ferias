##### JOGO FINALIZADO #####

#### FUNÇÕES ####


import transforma_base_certo
import valida_questao
import valida_questoes
import sorteia_questao
import sorteia_questao_inedita
import questao_para_texto
import gera_ajuda













###### LOOP PRINCIPAL ######


nome = input(str("Olá! Você está na Fortuna DesSoft e terá a oportunidade de enriquecer!\n\nQual seu nome? "))

nome_certo = nome.upper()

print(f"\n\nOk {nome_certo}, você tem direito a pular 3 vezes e 2 ajudas!")
print('As opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"!')
input("Aperte ENTER para continuar... ")
print("\n\nO jogo já vai começar! Lá vem a primeira questão!")
print("\n\nVamos começar com questões do nível FACIL!")
input("Aperte ENTER para continuar... ")


pulos = 3
ajudas = 2

if resposta == "pular":
    pulos -= 1

if resposta == "ajuda":
    ajudas -= 1

if pulos == 0 and resposta == "pular":
    print("você não tem mais ajudas")

if ajudas == 0 and resposta == "ajuda":
    print("você não tem mais pulos")