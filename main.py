from flask import Flask
from lib import route

app =  Flask(__name__)
if __name__== "main":
    app.run()
















# import requests


# input_uf  = input('Digite a UF do estado que queira pesquisar: ')
# request = requests.get('https://covid19-brazil-api.now.sh/api/report/v1/brazil/uf/{}'.format(input_uf))

# datas = request.json()

# if 'erro' not in datas:
#     print('UF DIGITADA ENCONTRADA')

#     print('UF: {}'.format(datas['uf']))
#     print('ESTADO: {}'.format(datas['state']))  
#     print('CASOS: {}'.format(datas['cases']))      
#     print('MORTOS: {}'.format(datas['deaths'])) 
#     print('SUSPEITAS: {}'.format(datas['suspects']))
