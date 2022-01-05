from django.http.response import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import parsers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
import json

import sqlite3
import os
two_up = os.path.dirname(os.path.dirname(__file__))

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

#This command allows for http requests without auth
@csrf_exempt

def getProducts(request):

    def connect_to_db():
        conn = sqlite3.connect('db.sqlite3')
        return conn

    conn = connect_to_db()
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    products = []
    if request.method == 'GET':
        try:
            cur.execute("SELECT * FROM store_product")
            rows = cur.fetchall()

            print('Prods look like', rows)
            
            # convert row objects to dictionary
            for i in rows:
                product = {}
                product["name"] = i["name"] 
                product["id"] = i["id"]
                product['category'] = i['category']
                product['price'] = i['price']
                products.append(product)

            #By default, the JsonResponse’s first parameter, data, should be a dict instance. To pass any other JSON-serializable object you must set the safe parameter to False.
            return JsonResponse(products, safe=False)

        except:
            products = []

    elif request.method == 'POST':
        newEntry = json.loads(request.body)
        
        try:
            sqlite_insert_query = f"""INSERT INTO store_product (name, price, category) VALUES 
            ('{newEntry['name']}', '{newEntry['price']}','{newEntry['category']}')"""

            count = cur.execute(sqlite_insert_query)
            conn.commit()
            print("Record inserted successfully into SqliteDb_developers table ", cur.rowcount)
            cur.close()

            products.append(newEntry)

            return JsonResponse(products, safe=False)

        except sqlite3.Error as error:
            return print("Failed to insert data into sqlite table", error)

