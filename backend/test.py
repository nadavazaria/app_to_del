import sqlite3
from flask import Flask,session,redirect,render_template,url_for,request
from icecream import ic 

app = Flask(__name__)

con = sqlite3.connect("rafis_garage.db")
cur = con.cursor()
# cur.execute("""INSERT INTO customers("name","last_name") VALUES("admin","owner")""")
# cur.execute("""INSERT INTO cars("customer_id","brand","model","color") VALUES(1,"Mazda",2055,"Grey") """)
# cur.execute("""DROP TABLE IF EXISTS cars_old""")
# con.commit()
cur.execute("SELECT * FROM customers")
col = [des[0] for des in cur.description]
ic(cur.description)
table_info = cur.fetchall()

for row in table_info:
    ic(row[1])


    # col_name = col[1]
    # col_info = col[2]

    # if "FOREIGN KEY" in col_info:
    #      print(f"The column '{col_name}' references another table.")
# cur.execute("""INSERT INTO customers ("name","lastname","country","city") VALUES ("Negev","Asaiag","Israel","Rehovot"),
#             ("shalom","haim","Israel","Natania" )""")
# cur.execute("""create table cars(id INTEGER PRIMARY KEY AUTOINCREMENT ,owner,color,brand,model)""")