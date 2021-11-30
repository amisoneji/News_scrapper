from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import requests
from pymongo import MongoClient
from flask_pymongo import PyMongo
import certifi

ca = certifi.where()
app = Flask(__name__)

CORS(app)

@app.route('/',methods=['GET']) #route to display homepage
@cross_origin()


def homepage():
    return render_template("index.html")

@app.route('/scrap_text',methods=['POST']) # route with allowed methods as POST and GET
def index():
    try:
        if request.method == 'POST':  # request hit API
            serchstring = request.form['text']
            client = MongoClient('mongodb+srv://root:root@cluster0.cgpw3.mongodb.net/myFirstDatabase?retryWrites=true&w=majority',tls=True, tlsAllowInvalidCertificates=True)
            results=[]
            data_base = "NewsDump"
            db = client[data_base]
            mng_db = client['db']
            collection_name = 'InfoQ'
            db_cm = mng_db[collection_name]
            db_cm.create_index([('Article Headline', 'text')])
            Records = db_cm.find({"$text": {"$search": serchstring}})

            for record in Records:
                print(record)
                results.append(record)
            return render_template('results.html', results=results)  # showing the review to the user

    except:
            return "Something Wrong"

if __name__ == '__main__':
    app.run()


