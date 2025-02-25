from flask import Flask, render_template
import mysql.connector
app = Flask(__name__)


@app.route('/')
def index():
    conn =  mysql.connector.connect(
        host="localhost",
        user="root",
        password="trolleo27",
        database="db"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    cursor.close()
    return render_template('index.html', students=students)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
