from flask import Flask, render_template, request
from forms import Leaderboard
import sqlite3
app=Flask(__name__)

app.secret_key='supersecretkey'
@app.route('/')
def home():
    return render_template("index.html")
@app.route('/submit', methods=['GET','POST'] )
def form():
    form=Leaderboard()
    if request.method == 'POST' and form.validate_on_submit():
        username = request.form['username']
        score=request.form['score']
        with sqlite3.connect("database.db") as users:
            cursor = users.cursor()
            cursor.execute("INSERT INTO LEADERBOARD \
            (username,score) VALUES (?,?)",
                           (username, score))
            users.commit()
        return render_template("index.html")
    else:
        return render_template('form.html', form=form)
@app.route('/leaderboard', methods=['GET','POST'] )
def leaderboard():
    connect = sqlite3.connect('scoreboard.db')
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM LEADERBOARD')

    data = cursor.fetchall()
    return render_template("leaderboard.html", data=data)

connect = sqlite3.connect('scoreboard.db')
connect.execute(
    'CREATE TABLE IF NOT EXISTS LEADERBOARD (username TEXT, score TEXT)'
)

#This if statement will ensure that the Flask app will only run if the script is executed directly and not when import is a module.
if __name__=='__main__':
    app.run(debug=True)
