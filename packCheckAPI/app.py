import sys
path = '/home/yourusername/mysite'
if path not in sys.path:
   sys.path.insert(0, path)

from flask import Flask, jsonify, request
import mysql.connector
mydb = mysql.connector.connect(
            host="packcheck.mysql.pythonanywhere-services.com",
            user="packcheck",
            password="graphic123",
            database="packcheck_data"
        )

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def productinfo(id):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM product_info where bar_id ="+id)
    product_result = mycursor.fetchone()
    return jsonify(product_result)

def chemicalinfo(chemical_name):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM chemical_name_mapping where chemical_name = '"+chemical_name+"'")
    chemical_name_standard = mycursor.fetchone()[1]

    mycursor.execute("SELECT * FROM risk_index where chemical_name = '" + chemical_name_standard+"'")
    chemical_result = mycursor.fetchone()
    return jsonify(chemical_result)

def searchproduct(productname):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT product_name FROM product_info where product_name = '" +"%"+productname+"%"+"'")
    itemresult=mycursor.fetchall()
    itemlist = []
    for i in itemresult:
        itemlist.append(itemresult[1][0])
    return jsonify(itemlist)
if __name__ == '__main__':
    app.run()

