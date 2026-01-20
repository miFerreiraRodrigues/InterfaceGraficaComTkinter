import requests
from tkinter import *

def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

    texto_cotacoes['text'] = texto


janela = Tk()
janela.title('Cotação Atual das Moedas')
janela.geometry('400x300')
janela.config(bg="lightblue")


# Configura a grid para expandir e centralizar

janela.grid_rowconfigure(0, weight=1)
janela.grid_rowconfigure(1, weight=1)
janela.grid_rowconfigure(2, weight=1)
janela.grid_columnconfigure(0, weight=1)

texto_orientacao = Label(janela, text='Clique no botão para exibir as cotações das moedas')
texto_orientacao.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

botao = Button(janela, text='Buscar cotações Dólar/Euro/BTC', command=pegar_cotacoes)
botao.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

texto_cotacoes = Label(janela, text='', bg="lightblue")
texto_cotacoes.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")

janela.mainloop()