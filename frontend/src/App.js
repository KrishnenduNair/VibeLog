import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

const moods = ['happy', 'sad', 'angry', 'anxious', 'excited', 'relaxed'];

function App() {
  const [username, setUsername] = useState('krishnendu'); // Replace with actual login system later
  const [mood, setMood] = useState('happy');
  const [journal, setJournal] = useState('');
  const [songs, setSongs] = useState([]);
  const [history, setHistory] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const BACKEND_URL = 'http://127.0.0.1:5000/'; // Flask backend running locally

  const submitMood = async () => {
    setLoading(true);
    setError('');
    try {
      const res = await axios.post(`${BACKEND_URL}/submit-mood`, {
        username,
        mood,
        journal,
      });
      setSongs(res.data.recommendations || []);
      setJournal('');
      await fetchHistory();
    } catch (err) {
      console.error('Submit error:', err.message);
      setError('Failed to submit mood. Make sure backend is running.');
    } finally {
      setLoading(false);
    }
  };

  const fetchHistory = async () => {
    try {
      const res = await axios.get(`${BACKEND_URL}/history/${username}`);
      setHistory(res.data);
    } catch (err) {
      console.error('Fetch history error:', err.message);
      setError('Failed to load mood history.');
    }
  };

  useEffect(() => {
    fetchHistory();
  }, []);

  return (
    <div className="App">
      <h1>Mood Journal</h1>

      <div>
        <label>Select your mood: </label>
        <select value={mood} onChange={e => setMood(e.target.value)}>
          {moods.map(m => <option key={m} value={m}>{m}</option>)}
        </select>
      </div>

      <textarea
        placeholder="Write how you're feeling..."
        value={journal}
        onChange={e => setJournal(e.target.value)}
      />

      <button onClick={submitMood} disabled={loading}>
        {loading ? 'Submitting...' : 'Submit Mood'}
      </button>

      {error && <p style={{ color: 'red' }}>{error}</p>}

      <h2>Recommended Songs</h2>
      <ul>
        {songs.map((s, i) => (
          <li key={i}>
            <a href={s.url} target="_blank" rel="noopener noreferrer">
              {s.name} – {s.artist}
            </a>
          </li>
        ))}
      </ul>

      <h2>Mood History</h2>
      <ul>
        {history.map((entry, i) => (
          <li key={i}>
            <strong>{entry.mood}</strong> ({new Date(entry.timestamp).toLocaleString()})<br />
            {entry.journal}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
