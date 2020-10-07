from Bot import Bot

lista = [["olá", "oi", "tudo bem?"], 
         ["oi, tudo bem?", "oi, como vai?"],
         ["qual o seu nome?"],
         ["consulta de preços", "consulta de preços de seguradoras", "gostaria de consultar os preços das seguradoras", "quero consultar os preços das seguradoras"],
         ["covid", "coronavirus", "covid-19", "corona", "corona virus"],
         ["vou sair","sair", "quero sair"]]

respostas = ["Olá, eu sou Nome, como posso ajudar?", 
             "Estou bem! Gostaria que eu te ajudasse em algo?",
             "Meu nome é Nome. Gostaria de ajuda com alguma coisa?",
             "Ok, aguarde só um momento enquanto pesquiso as informações",
             "O que gostaria de saber sobre o Covid-19?\n1 - Número de casos e mortes no Brasi\n2 - Número de casos e mortes no mundo\n3 - sintomas\n4 - Sair", 
             "Tudo bem. Espero ter ajudado!"]

bot = Bot(lista, respostas)

pergunta=''

while pergunta!='quero sair':
    pergunta = input("\nDigite algo: ")
    pergunta=pergunta.lower()

    if pergunta in ['covid' , 'coronavirus' ,'covid-19' , 'corona' , 'corona virus']:
        print(bot.find_word(pergunta))
        pergunta=pergunta.lower()
        pergunta = input("\nEscolha uma alternativa: ")

        if pergunta=="1":
            print("\nDados Covid Brasil")
        elif pergunta=="2":
            print("\nDados Covid mundo")
        elif pergunta=="3":
            print("\nOs principais sintomas do Covid-19 incluem: \n -Dificuldade de respirar; \n -Febre; \n -Tosse. \nSe apresentar estes sintomas, por favor, procure ajuda médica para fazer um exame que poderá comprovar se você tiver o COVID-19.")
        elif pergunta=="4":
            pergunta="vou sair"
            print(bot.find_word(pergunta))
            break
    else:
        print(bot.find_word(pergunta))
