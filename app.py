from flask import Flask, render_template, request, jsonify
import sqlite3
app=Flask(__name__)

app.secret_key='supersecretkey'

@app.route('/')
def home():
    return render_template("index.html")
@app.route('/leaderboard', methods=['GET','POST'] )
def leaderboard():
    connect = sqlite3.connect('scoreboard.db')
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM LEADERBOARD ORDER BY score ASC;')

    data = cursor.fetchall()
    return render_template("leaderboard.html", data=data)

@app.route('/info')
def info():
    return render_template("info.html")
@app.route("/info/levels")
def levels():
    return render_template("levels.html")
@app.route("/info/enemies")
def enemies():
    return render_template("enemies.html")
@app.route("/info/scoring")
def scoring():
    return render_template("scoring.html")
@app.route("/add", method='GET')
def autoadd():
    with sqlite3.connect("scoreboard.db") as users:
        cursor = users.cursor()
        cursor.execute("INSERT OR REPLACE INTO LEADERBOARD \
        (username,score) VALUES (?,?)",
                       (username, score))
        users.commit()
    return render_template("index.html")
connect = sqlite3.connect('scoreboard.db')
connect.execute(
    'CREATE TABLE IF NOT EXISTS LEADERBOARD (username TEXT, score TEXT)'
)

#This if statement will ensure that the Flask app will only run if the script is executed directly and not when import is a module.
if __name__=='__main__':
    app.run(port=3000, debug=True)
