from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse
from flask_pymongo import PyMongo
from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)

#Cria conexao com o MongoDB
app.config['MONGO_URI'] = 'mongodb://meli_challenge:MELI123@mongodb:27017/meli_challenge'
app.config['MONGO_DBNAME'] = "meli_challenge"
mongo = PyMongo(app)

#Executa 
class Search(Resource):
    def get(self):
        mongodb = mongo.db.meli_challenge

        output = []
        
        arquivo = request.args.get('arquivo')
        palavra = request.args.get('palavra')

        #Busca o registro com base no nome do arquivo e a palavra buscada e retorna a quantidade
        for q in mongodb.find({"$and": [{"arquivo":arquivo}, {"palavra":palavra}]}):
            output.append({'quantidade' : q['quantidade']})
            return {'quantidade': output}

api.add_resource(search, '/search')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)