from flask import FLASK
import psycopg2

app = Flask(__name__)

def retrievedatabase():
    conn = psycopg2.connect
    	db='group8_structure',
    user='student',
    password='student',
    host='localhost'
    cur = conn.cursor()

cur.execute("SELECT * FROM faculty_list)
data = cur.fetchall()

cur.close()
conn.close()

return data

@app.route('/')
def index():
    data = retrievedatabase()
    return render_template('faculty_list.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
