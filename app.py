
from flask import Flask
from flask_mysqldb import MySQL
mysql = MySQL()
app = Flask(__name__)
# My SQL Instance configurations 
# Change the HOST IP and Password to match your instance configurations
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Lab3'
app.config['MYSQL_DB'] = 'studentbook'
app.config['MYSQL_HOST'] = '130.211.81.243'
mysql.init_app(app)

# The first route to access the webservice from http://external-ip:5000/ 
#@pp.route("/add") this will create a new endpoints that can be accessed using http://external-ip:5000/add
@app.route("/")
def hello(): # Name of the method
    cur = mysql.connection.cursor() #create a connection to the SQL instance
    cur.execute('''SELECT * FROM students''') # execute an SQL statment
    rv = cur.fetchall() #Retreive all rows returend by the SQL statment
    return str(rv)      #Return the data in a string format
if __name__ == "__main__":
        app.run(host='0.0.0.0', port='5000') #Run the flask app at port 5000

        
 #Route to add to table
@app.route("/")
def add():
    cur = mysql.connection.cursor()
    cur.execute('''INSERT student1 INTO students''')
    rv = cur.fetchall()
    return str(rv)
    if __name__ == "__main__":
        app.run(host='0.0.0.0', port='5000')
    
    #Route to update table
    @app.route("/")
def update():
    cur = mysql.connection.cursor()
    cur.execute('''UPDATE students SET student1 = student2''')
    rv = cur.fetchall()
    return str(rv)
    if __name__ == "__main__":
        app.run(host='0.0.0.0', port='5000')
    
    #Route to delete from table
    @app.route("/")
def delete():
    cur = mysql.connection.cursor()
    cur.execute('''DELETE student1 FROM students''')
    rv = cur.fetchall()
    return str(rv)
    if __name__ == "__main__":
        app.run(host='0.0.0.0', port='5000')
    
