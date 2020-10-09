from Bot import Bot

lista = [["olá", "oi", "tudo bem?"], 
         ["oi, tudo bem?", "oi, como vai?"],
         ["qual o seu nome?"],
         ["consulta de preços", "consulta de preços de seguradoras", "gostaria de consultar os preços das seguradoras", "quero consultar os preços das seguradoras"],
         ["covid", "coronavirus", "covid-19", "corona", "corona virus"],
         ["cov_dt_br"],
         ["cov_dt_md"],
         ["cov_sint"],
         ["cov_prv"],
         ["vou sair","sair", "quero sair"]]

respostas = ["Olá, eu sou Nome, como posso ajudar?", 
             "Estou bem! Gostaria que eu te ajudasse em algo?",
             "Meu nome é Nome. Gostaria de ajuda com alguma coisa?",
             "Ok, aguarde só um momento enquanto pesquiso as informações",
             "\n\n\nO que gostaria de saber sobre o Covid-19?\n1 - Número de casos e mortes no Brasi\n2 - Número de casos e mortes no mundo\n3 - sintomas \n4 - Prevenção\n5 - Voltar para o menu anterior\n6 - Sair", 
             "\nDados Covid Brasil",
             "\nDados Covid Mundo",
             "\nOs principais sintomas do Covid-19 incluem: \n -Dificuldade de respirar; \n -Febre; \n -Tosse. \nSe apresentar estes sintomas, por favor, procure ajuda médica para fazer um exame que poderá comprovar se você tem o COVID-19.",
             "\nAlgumas das principais recomendações para a prevenção do Covid-19 incluem: \n -Higienizar bem as mãos com água e sabão ou álcool gel; \n -Quando sair de casa, usar uma  máscara que cubra o nariz e a boca; \n -Evitar aglomerações; \n -Manter uma distância mínima de ao menos 1 metro de outras pessoas.",
             "Tudo bem. Espero ter ajudado!"]

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
    
    elif pergunta in ['vou sair','sair', 'quero sair']:
        sair=0

