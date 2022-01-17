from flask import Flask, render_template, request
from flask_table import Table, Col, LinkCol
from db_routines import DbRoutines
from table import Books1



########################################################
# TODO: Make server production grade using 'waitress'  #
########################################################

app = Flask(__name__)
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root_password'
app.config['MYSQL_HOST'] = 'db'
app.config['MYSQ_PORT'] = 3306
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

dbRoutines = DbRoutines(app)

is_registed_user = False

@app.route('/')
def index():
    return render_template("login.html")

@app.route('/login', methods=['POST', 'GET'])
def login():
    return render_template("login.html")

@app.route('/home', methods=['POST', 'GET'])
def systems():
        if request.method == 'GET':
            cursor = dbRoutines.mysql.connection.cursor()
            cursor.execute(f"use webapp_db;")
            cursor.execute("SELECT * FROM `Books`")
            rows = cursor.fetchall()
            Table = Books1(rows)
            return render_template('index.html', Table = Books1)
        if request.method == 'POST':
            Title = request.form['Title']
            Author = request.form['Author']  
            cursor = dbRoutines.mysql.connection.cursor()
            cursor.execute(f"use webapp_db;")
            cursor.execute (f"INSERT INTO Books (`Title`, `Author`) VALUES ('{Title}', '{Author}');")
            dbRoutines.mysql.connection.commit()                                            
            cursor.close()          
            return render_template("home.html")

        return render_template("home.html")


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        if request.form['uname'] != "" and request.form['pwd'] != "" and request.form['repwd'] != "" and request.form['pwd'] == request.form['repwd']:
            userName = request.form['uname']
            userPwd = request.form['pwd']
            cursor = dbRoutines.mysql.connection.cursor()
            cursor.execute(f"use webapp_db;")
            cursor.execute(f"SELECT COUNT(*) FROM `Credentials` WHERE uname = '{userName}' AND pwd = '{userPwd}';")
        
            user_list = cursor.fetchall()
            if user_list[0]['COUNT(*)'] > 0:                     
                cursor.close()
                return render_template("message.html", message=f"User '{userName}' already registed.")
            else:
                cursor.execute(f"INSERT INTO `Credentials` (`uname`, `pwd`) VALUES ('{userName}','{userPwd}');")
                dbRoutines.mysql.connection.commit()
                cursor.close()
                return render_template("login.html")
        else:
            return render_template("message.html", message="Invalid input.")

    return render_template("register.html")


@app.route('/verify', methods=['POST'])
def verify():
    if request.method == 'POST':
        if request.form['uname'] != "" and request.form['pwd'] != "":
            userName = request.form['uname']
            userPwd = request.form['pwd']
            cursor = dbRoutines.mysql.connection.cursor()
            cursor.execute(f"use webapp_db;")
            cursor.execute(f"SELECT COUNT(*) FROM `Credentials` WHERE uname = '{userName}' AND pwd = '{userPwd}';")
        
            user_list = cursor.fetchall()
            if user_list[0]['COUNT(*)'] > 0:                     
                cursor.close()
                return render_template("home.html")
                                      
    return render_template("login.html")


          


@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/links')
def links():
    return render_template('links.html')

if __name__ == '__main__':
   app.run(host='0.0.0.0', debug=True)








