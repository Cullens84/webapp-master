from flask import Flask, render_template, request
from db_routines import DbRoutines



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

@app.route('/home', methods=['POST', 'GET'])
def systems():
    if request.method == 'POST':
        if request.method == 'GET':
            cursor = dbRoutines.mysql.connection.cursor()
            cursor.execute(f"use webapp_db;")
            cursor.execute("SELECT * FROM `Books`")
            rows = cursor.fetchall()
            
            cursor.close() 
            return render_template('home.html')
        if request.form['Title'] != "" and request.form['Author'] != "":
            Title = request.form['Title']
            Author = request.form['Author']
            cursor = dbRoutines.mysql.connection.cursor()
            cursor.execute(f"use webapp_db;")
            cursor.execute(f"SELECT COUNT(*) FROM `Books` WHERE Author = '{Author}';")
            
            Books_list = cursor.fetchall()
            if Books_list[0]['COUNT(*)'] > 0:                     
                cursor.close()
                return render_template("message.html", message=f"A Book called '{Title}' already exists.")
            else:    
                cursor.execute (f"INSERT INTO `Books (`Title`, `Author`) VALUES ('{Title}', '{Author}');")
                dbRoutines.mysql.connection.commit()                                            
                cursor.close()          
                return render_template("home.html")

    return render_template("home.html")

# @app.route('/home', methods=['POST', 'GET'])
# def home():
#     if request.method == 'POST':
#         if request.form['title'] != "" and request.form['author'] != "":
#             title = request.form['title']
#             author = request.form['author']
#             cursor = dbRoutines.mysql.connection.cursor()
#             cursor.execute(f"use webapp_db;")
#             cursor.execute(f"SELECT * FROM `Books`;")
        
#             user_list = cursor.fetchall()
#             if user_list[0]['*'] < 0:                     
#                 cursor.close()
#                 return render_template("home.html")
#             else:
#                 cursor.execute(f"INSERT INTO `Books` (`Title`, `Author`) VALUES ('{title}','{author}');")
#                 dbRoutines.mysql.connection.commit()
#                 cursor.close()
#                 return render_template("home.html")
#         else:
#             return render_template("message.html")
#     else:
#         return render_template("home.html")           


@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/links')
def links():
    return render_template('links.html')

if __name__ == '__main__':
   app.run(host='0.0.0.0', debug=True)








