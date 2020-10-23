from Bot import Bot

from Textos import lista, respostas

bot = Bot(lista, respostas)

pergunta=''
sair=1

while sair!=0:
    pergunta = input("\nDigite algo: ")
    pergunta=pergunta.lower()
    print(bot.find_word(pergunta))

    if pergunta in ['covid' , 'coronavirus' ,'covid-19' , 'corona' , 'corona virus']:
        pergunta = input("\nEscolha uma opção: ")
        pergunta=pergunta.lower()
        print(bot.find_word(pergunta))
    
    elif pergunta in ['vou sair' , 'sair', 'quero sair', 'obrigado pela ajuda', 'obrigada pela ajuda', 'agradeço pela ajuda', 'estarei saindo agora']:
        sair=0
