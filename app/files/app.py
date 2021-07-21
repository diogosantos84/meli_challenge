import glob, os, sys, re, pymongo
from pymongo import MongoClient

#Conecta com MongoDB
client = MongoClient("mongodb://meli_challenge:MELI123@mongodb:27017/meli_challenge")
db = client['meli_challenge']

#Busca arquivos *.txt no diretório
os.chdir("coleccion_2020")
for file in glob.glob("*.txt"):
    frequency = {}

    #Abre documento como ReadOnly
    document_text = open(file, 'r')

    #Converte as strings do documento para caixa baixa
    text = document_text.read().lower()

    #Analisa as palavras encontradas
    words = re.findall(r'\b[a-z]\b', text)

    #Calcula a frequencia em que cada palavra aparece no arquivo
    for word in words:
        count = frequency.get(word, 0)
        frequency[word] = count + 1
        frequency_list = frequency.keys()

    #Para cada palavra, adiciona o registro no MongoDB com o nome do arquivo, a palavra e a frequencia que aparece em cada arquivo
    for words in frequency_list:
        db.meli_challenge.insert( { "arquivo": file, "palavra": words, "quantidade": frequency[words] } )