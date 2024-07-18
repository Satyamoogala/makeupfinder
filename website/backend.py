from flask import Flask, jsonify, request
import psycopg2

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="my_database",
        user="satya2302",
        password="Siri_2302"
    )
    return conn

@app.route('/recommend', methods=['POST'])
def recommend():
    skin_tone = request.json['skin_tone']
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT brand,product,hex FROM SHADE WHERE skin_tone_category = %s", (skin_tone,))
    products = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(products)

if __name__ == '__main__':
    app.run(debug=True)
