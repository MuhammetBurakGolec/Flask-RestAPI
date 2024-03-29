# flask_restful: REST API’larının hızlı bir şekilde oluşturulması için destek ekleyen bir Flask uzantısıdır.

# flask_script: Flask’ta harici komut dosyaları yazmak için destek sağlayan bir uzantıdır.

# flask_migrate: Alembic kullanan Flask uygulamaları için SQLAlchemy veritabanı geçişlerini işleyen bir uzantıdır.

# marshmallow: Nesneler gibi karmaşık veri türlerini yerel Python veri türlerine dönüştürmek için bir ORM /ODM agnostik kitaplıktır. Bunu doğrulama için kullanacağız. Nesneleri serileştirmek ve seriyi kaldırmak için kullanılır.

# flask_sqlalchemy: SQLAlchemy için destek ekleyen Flask için bir uzantıdır.

# flask_marshmallow: Ek özellikler ekleyen Flask ve nesne serileştirme / seriyi kaldırma kitaplığı için bir entegrasyon katmanıdır.

# marshmallow-sqlalchemy: Ek özellikler ekler.

# psycopg: Python programlama dili için bir PostgreSQL bağdaştırıcısıdır

from crypt import methods

try:
    from flask import Flask, jsonify, request
    from flask_restful import Resource, Api

except ImportError:
    print("Import Error")

from flask import Flask, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

city = {
    '1':'Adana',
    '2':'Adiyaman',
    '3':'Afyon',
    '4':'',
    '5':'',
    '6':'Ankara',
    '7':'Antalya',
    '8':'',
    '9':'',
    '10':'',
    '11':'',
    '12':'',
    '13':'',
    '14':'',
    '15':'',
    '16':'',
    '17':'',
    '18':'',
    '19':'',
    '20':'',
    '21':'',
    '22':'',
    '23':'',
    '24':'',
    '25':'',
    '26':'',
    '27':'',
    '28':'',
    '29':'',
    '30':'',
    '31':'',
    '32':'',
    '33':'',
    '34':'Istanbul',
    '35':'',
    '36':'',
    '37':'',
    '38':'',
    '39':'',
    '40':'',
    '41':'Kocaeli',
    '42':'Konya',
    '43':'',
    '44':'',
    '45':'',
    '46':'',
    '47':'',
    '48':'',
    '49':'',
    '50':'',
    '51':'',
    '52':'',
    '53':'',
    '54':'',
    '55':'',
    '56':'',
    '57':'',
    '58':'',
    '59':'',
    '60':'',
    '61':'',
    '62':'',
    '63':'',
    '64':'',
    '65':'',
    '66':'',
    '67':'',
    '68':'Aksaray',
    '69':'',
    '70':'Karaman',
    '71':'',
    '72':'',
    '73':'',
    '74':'',
    '75':'',
    '76':'',
    '77':'',
    '78':'',
    '79':'',
    '80':'',
    '81':'',
}

class City(Resource):

    def get(self, id):

        if id =="all":
            return city, 200
        elif int(id)>0 and int(id)<82:
            return city[id]
        else:
            return "Not Found", 404

class Math(Resource):

    def topla( self, num1,num2,islem):

        if islem =='topla':
                num = num1 + num2
                return num, 202 

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
api.add_resource(Math,"/math/<islem>/<int:num1>/<int:num2>")


if __name__ == '__main__':
    app.run()

    
