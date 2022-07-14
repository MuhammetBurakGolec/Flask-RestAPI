# flask_restful: REST API’larının hızlı bir şekilde oluşturulması için destek ekleyen bir Flask uzantısıdır.

# flask_script: Flask’ta harici komut dosyaları yazmak için destek sağlayan bir uzantıdır.

# flask_migrate: Alembic kullanan Flask uygulamaları için SQLAlchemy veritabanı geçişlerini işleyen bir uzantıdır.

# marshmallow: Nesneler gibi karmaşık veri türlerini yerel Python veri türlerine dönüştürmek için bir ORM /ODM agnostik kitaplıktır. Bunu doğrulama için kullanacağız. Nesneleri serileştirmek ve seriyi kaldırmak için kullanılır.

# flask_sqlalchemy: SQLAlchemy için destek ekleyen Flask için bir uzantıdır.

# flask_marshmallow: Ek özellikler ekleyen Flask ve nesne serileştirme / seriyi kaldırma kitaplığı için bir entegrasyon katmanıdır.

# marshmallow-sqlalchemy: Ek özellikler ekler.

# psycopg: Python programlama dili için bir PostgreSQL bağdaştırıcısıdır

from flask import Flask, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

city = {
    '1':'Adana',
    '2':'Adiyaman',
    '3':'Afyon'
}

class City(Resource):

    def get(self, id):

        if id =="all":
            return jsonify(data = city), 200

        return jsonify(data = city[id]), 201

class Math(Resource):

    def topla( self, num1,num2,islem):

        if islem =='topla':
                num = num1 + num2
                return jsonify(data=num), 202 

        if islem =='cikar': 
            num = num1 - num2       
            return jsonify(data=num), 202 
        
        if islem =='carp':         
            num = num1 * num2   
            return jsonify(data=num), 202 
        
        if islem =='bol': 
            num = num1 / num2
            return jsonify(data=num), 202 

api.add_resource(City, "/city/<id>")
api.add_resource(Math,"/math/<islem>/<num1>/<num2>")


if __name__ == '__main__':
    app.run()

    
