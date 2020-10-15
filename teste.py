from Bot import Bot

from Textos import lista, respostas

bot = Bot(lista, respostas)

pergunta=''
voltar=1
sair=1

while sair!=0:
    voltar=1
    pergunta = input("\nDigite algo: ")
    pergunta=pergunta.lower()
    print(bot.find_word(pergunta))

    if pergunta in ['covid' , 'coronavirus' ,'covid-19' , 'corona' , 'corona virus']:
        while voltar!=0:
            pergunta = input("\nEscolha uma alternativa: ")
            if pergunta=="1":
                pergunta="cov_dt_br"
                print(bot.find_word(pergunta))

                pergunta="covid"
                print(bot.find_word(pergunta))

            elif pergunta=="2":
                pergunta="cov_dt_md"
                print(bot.find_word(pergunta))

                pergunta="covid"
                print(bot.find_word(pergunta))

            elif pergunta=="3":
                pergunta="cov_sint"
                print(bot.find_word(pergunta))

                pergunta="covid"
                print(bot.find_word(pergunta))

            elif pergunta=="4":
                pergunta="cov_prv"
                print(bot.find_word(pergunta))

                pergunta="covid"
                print(bot.find_word(pergunta))

            elif pergunta=="5":
                voltar=0

            elif pergunta=="6":
                pergunta="vou sair"
                print(bot.find_word(pergunta))
                sair=0
                break
    
    elif pergunta in ['vou sair' , 'sair', 'quero sair', 'obrigado pela ajuda', 'obrigada pela ajuda', 'agradeço pela ajuda', 'estarei saindo agora']:
        sair=0
