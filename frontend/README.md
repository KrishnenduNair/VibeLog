##VibeLog

VibeLog is a full-stack web application that allows users to log their daily moods and receive personalized music recommendations from Spotify based on their emotional state. It also keeps a history of past entries to help users reflect on their well-being over time.

Project Structure:
- Frontend: React 
- Backend: Flask + SQLite + Spotify API 

Features:
- Mood selection from a predefined list
- Journal input field for thoughts and reflections
- Song recommendations from Spotify based on mood
- Mood history view with timestamps
- Integration between frontend and backend via Axios
- Spotify access token management and API handling

------------------------------------------------------------
Setup Instructions

1. Clone the repository
   git clone https://github.com/your-username/mood-journal.git
   cd mood-journal

------------------------------------------------------------
Backend Setup (Flask + Spotify API)

1. Navigate to backend directory
   cd backend

2. Create a virtual environment
   python3 -m venv venv
   source venv/bin/activate   (or venv\Scripts\activate on Windows)

3. Install dependencies
   pip install -r requirements.txt

4. Create a .env file with your Spotify credentials
   SPOTIFY_CLIENT_ID=your_client_id
   SPOTIFY_CLIENT_SECRET=your_client_secret

5. Run the Flask app
   python app.py

The backend will run on http://localhost:5000

------------------------------------------------------------
Frontend Setup (React)

1. Open a new terminal window
2. Navigate to frontend directory
   cd frontend

3. Install dependencies
   npm install

4. Start the frontend React app
   npm start

The frontend will run on http://localhost:3000

Make sure the backend is running in parallel on port 5000

------------------------------------------------------------
API Endpoints

POST /submit-mood
  Request JSON:
    {
      "username": "your_username",
      "mood": "happy",
      "journal": "Had a great day!"
    }
  Response:
    {
      "status": "success",
      "recommendations": [
        {
          "name": "Song Title",
          "artist": "Artist",
          "url": "https://open.spotify.com/..."
        }
      ]
    }

GET /history/<username>
  Returns all mood entries submitted by the given user.

GET /test-spotify
  Sends a test request for mood-based song recommendations.

------------------------------------------------------------
Deployment (Optional)

You can deploy the app using Render, Railway, or any hosting of your choice.

1. Push the code to GitHub
2. Deploy backend as a web service
3. Add required environment variables:
   - SPOTIFY_CLIENT_ID
   - SPOTIFY_CLIENT_SECRET

4. For frontend, build using
   npm run build
   Then deploy with services like Netlify or Vercel

------------------------------------------------------------
Credits

Developed by Krishnendu as part of a full-stack side project.
