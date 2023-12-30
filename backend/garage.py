import sqlite3
from flask import Flask,session,redirect,render_template,url_for,request
from icecream import ic 

app = Flask(__name__)
app.secret_key = "secret_shhhh"
user = []
con = sqlite3.connect("rafis_garage.db")
cur = con.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS cars (id INTEGER PRIMARY KEY AUTOINCREMENT, customer_id INTEGER,brand TEXT,model INTEGER,color TEXT, FOREIGN KEY(customer_id) REFERENCES customers(id) )""")
@app.route("/") 
def home():
    global user
    if "user" in session:
        user = session["user"]
        last_name = session["last_name"]
        return f"<h1>hello {user} {last_name} welcome to rafie's<h1>"
    else:
        
        return redirect(url_for("login"))

    
@app.route("/login" ,methods = ["GET","POST"])
def login():
    if request.method == "POST":
        user = request.form["username"]
        last_name = request.form["last_name"]
        # cur.execute("""INSERT INTO customers(name,last_name) VALUES(?,?)(user,lastname)""")
        session["user"] = user
        session["last_name"] = last_name
        ic(session["user"])
        return redirect(url_for("home"))

    return render_template("login.html")
@app.route("/signup", methods = ["GET","POST"])


def signup():
    if request.method == "POST":
        first_name = request.form["f_name"]
        last_name = request.form["l_name"]
    
        session["user"] = first_name
        session["last_name"] = last_name
        ic(session["user"],session["last_name"] )
        cur.execute("""INSERT INTO customers ("name","last_name") VALUES (?,?)""",(first_name,last_name))
        con.commit()
        return render_template("home.html")
    return render_template("signup.html")



if __name__ == "__main__":
    app.run(debug=True)
# cur.execute("""INSERT INTO customers ("name","lastname","country","city") VALUES ("Negev","Asaiag","Israel","Rehovot"),
#             ("shalom","haim","Israel","Natania" )""")
# cur.execute("""create table cars(id INTEGER PRIMARY KEY AUTOINCREMENT ,owner,color,brand,model)""")