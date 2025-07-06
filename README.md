## VibeLog

VibeLog is a mood journaling web app that integrates with Spotify to recommend music based on your mood. Users can log how they're feeling, write journal entries, and get personalized song recommendations to match their emotional state.

## Features

- Select your mood from a predefined list
- Write a daily journal entry
- Get music recommendations based on mood using the Spotify API
- View mood history with timestamps

## Project Structure

```

VibeLog/
├── backend/           # Flask backend
│   ├── app.py
│   ├── spotify.py
│   ├── requirements.txt
├── frontend/          # React frontend
│   ├── public/
│   ├── src/
│   ├── package.json
├── README.md

````

## Getting Started

### Prerequisites

- Python 3.10+
- Node.js and npm
- Spotify Developer account (for Client ID & Secret)

---

### 1. Clone the Repository

```bash
git clone https://github.com/KrishnenduNair/VibeLog.git
cd VibeLog
````

---

### 2. Setup Backend

```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Create a `.env` file in the backend directory with your Spotify credentials:

```
SPOTIFY_CLIENT_ID=your_client_id
SPOTIFY_CLIENT_SECRET=your_client_secret
```

Run the Flask backend server:

```bash
python app.py
```

The backend will run at `http://localhost:5000`

---

### 3. Setup Frontend

```bash
cd ../frontend
npm install
npm start
```

The frontend will run at `http://localhost:3000`

---

## Example Usage

1. Open the frontend in the browser.
2. Select a mood (e.g., happy).
3. Write a journal entry about your current feeling.
4. Submit to get mood-based Spotify music recommendations.
5. Scroll to see mood history with timestamps.

---

## Built With

* React (Frontend)
* Flask (Backend)
* Axios (HTTP Requests)
* Spotify Web API
* SQLite (Database)

---

## License

This project is for educational and non-commercial use.

##Created By
Krishnendu Nair
