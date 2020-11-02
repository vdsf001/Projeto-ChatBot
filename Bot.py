class Bot():
    def __init__(self, opcoes, respostas):
        self.opcoes = opcoes
        self.respostas = respostas

    def __word_exists(self, item, word):
        for index, array_index in enumerate(item):
            for palavra in array_index:
                if(palavra == word):
                    return index

    def find_word(self, word):
        found = self.__word_exists(self.opcoes, word)
        try:
            return self.respostas[found]
        except:
            return "Desculpe, poderia digitar novamente? Você pode tentar pesquisar pelos planos de saúde de diversas seguradoras ao redor do país ou até obter informações sobre o COVID-19"

