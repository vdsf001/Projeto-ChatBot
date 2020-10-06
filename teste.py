from Bot import Bot

lista = [["olá", "oi", "tudo bem?"], 
         ["oi, tudo bem?", "oi, como vai?"],
         ["consulta de preços","consulta de preços de seguradoras","gostaria de consultar os preços das seguradoras","quero consultar os preços das seguradoras"],
         ["vou sair","Sair", "quero sair"]]

respostas = ["Olá, como posso ajudar?", 
             "Estou bem! Gostaria que eu te ajudasse em algo?",
             "Ok, aguarde só um momento enquanto pesquiso as informações",
             "Tudo bem. Espero ter ajudado!"]

bot = Bot(lista, respostas)

pergunta=""

while pergunta!='quero sair':
    pergunta = input("\nDigite algo:")
    pergunta=pergunta.lower()
    print(bot.find_word(pergunta))
