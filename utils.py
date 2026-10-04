#Bibliotecas
import requests
from dotenv import load_dotenv 
import os 


#carregar as variáveis de ambiente do arquivo .env
load_dotenv()

if not load_dotenv():
    print("Erro ao carregar o arquivo .env")
    exit(1) # encerra o programa com código de erro 1

#Variáveis

chave_api = os.getenv("CHAVE_API") # pegar a chave da API do arquivo .env
requisicao = requests.get(f"https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL?token={chave_api}")
dicionario_requisicao = requisicao.json()

def verificarCotacaoDinheiro():

    if requisicao.status_code == 200:
        print(f"Cotação atual do Dolar: $ {dicionario_requisicao["USDBRL"]["bid"]}")
        print(f"Cotação atual do Euro: € {dicionario_requisicao["EURBRL"]["bid"]}")
        print(f"Cotação atual do Bitcoin: ₿ {dicionario_requisicao["BTCBRL"]["bid"]}")

def conversorMoeda(valor, opcao, moeda):

    cotacao = float(dicionario_requisicao[moeda]["bid"])

    if opcao == 1:
        resultado = cotacao * valor

        if moeda == "BTCBRL":
            print (f"{resultado:.9f}" )
        else:
            print (f"{resultado:.2f}" )

    elif opcao == 2:
        resultado = valor / cotacao

        if moeda == "BTCBRL":
            print (f"{resultado:.9f}" )
        else:
            print (f"{resultado:.2f}" )

    return resultado
            