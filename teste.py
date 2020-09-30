from Bot import Bot

lista = [["Edson", "Arão"], ["Vinicius", "Elias"]]

respostas = ["Achou Arão ou Edson", "Achou Vinicius ou Elias"]

bot = Bot(lista, respostas)

print(bot.find_word("fdsjfl"))