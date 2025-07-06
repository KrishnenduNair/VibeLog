from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
from datetime import datetime
from spotify import get_recommendations

app = Flask(__name__)
CORS(app)

# --- DB Setup ---
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS mood_entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            mood TEXT NOT NULL,
            journal TEXT,
            timestamp TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# --- Routes ---

@app.route('/submit-mood', methods=['POST'])
def submit_mood():
    data = request.json
    username = data.get('username')
    mood = data.get('mood')
    journal = data.get('journal')
    timestamp = datetime.utcnow().isoformat()

    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('INSERT INTO mood_entries (username, mood, journal, timestamp) VALUES (?, ?, ?, ?)',
              (username, mood, journal, timestamp))
    conn.commit()
    conn.close()

    recommendations = get_recommendations(mood)
    return jsonify({'status': 'success', 'recommendations': recommendations})


@app.route('/history/<username>', methods=['GET'])
def get_history(username):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT mood, journal, timestamp FROM mood_entries WHERE username=? ORDER BY timestamp DESC', (username,))
    rows = c.fetchall()
    conn.close()

    history = [{'mood': r[0], 'journal': r[1], 'timestamp': r[2]} for r in rows]
    return jsonify(history)

@app.route('/test-spotify')
def test_spotify():
    from spotify import get_recommendations
    results = get_recommendations('happy')
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
