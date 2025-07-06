from dotenv import load_dotenv
import requests

load_dotenv()

import os
client_id = os.getenv('SPOTIFY_CLIENT_ID')
client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')

print("🔑 Client ID:", client_id)
print("🔑 Client Secret:", client_secret)


MOOD_TO_GENRE = {
    'happy': 'pop',
    'sad': 'acoustic',
    'angry': 'metal',
    'anxious': 'ambient',
    'excited': 'edm',
    'relaxed': 'chill'
}

def get_access_token():
    auth_url = 'https://accounts.spotify.com/api/token'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret
    }

    response = requests.post(auth_url, headers=headers, data=data)

    print("🔁 Spotify Token Status Code:", response.status_code)
    print("🔁 Spotify Token Raw Response:", response.text)

    if response.status_code != 200:
        print("Failed to get token")
        return None

    return response.json().get('access_token')

def get_recommendations(mood):
    access_token = get_access_token()
    if not access_token:
        return [{'error': 'Failed to fetch Spotify token'}]

    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    # Use mood as search keyword
    query = f"{mood} music"
    endpoint = "https://api.spotify.com/v1/search"
    params = {
        'q': query,
        'type': 'track',
        'limit': 5,
        'market': 'US'
    }

    response = requests.get(endpoint, headers=headers, params=params)
    print("🔍 Search Response URL:", response.url)
    print("🔍 Status:", response.status_code)
    print("🔍 Response:", response.text)

    try:
        data = response.json()
        tracks = data.get('tracks', {}).get('items', [])
        return [
            {
                'name': t['name'],
                'artist': t['artists'][0]['name'],
                'url': t['external_urls']['spotify']
            } for t in tracks
        ]
    except:
        return [{'error': 'Failed to decode response'}]



