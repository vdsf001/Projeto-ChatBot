lista = [["Edson", "Arão"], ["Vinicius", "Elias"]]

respostas = ["Achou Arão ou Edson", "Achou Vinicius ou Elias"]

def word_exists(item, word):
    for index, array_index in enumerate(item):
        for palavra in array_index:
            if(palavra == word):
                return index
                
    

def find_word(word, lista):
    found = word_exists(lista, word)
    return found

x = find_word("Arão", lista)

print(respostas[x])

