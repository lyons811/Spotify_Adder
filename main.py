import spotipy
from spotipy.oauth2 import SpotifyOAuth

client_id = 'client_id'
client_secret = 'client_secret'
redirect_uri = 'http://localhost/'

scope = 'user-library-read playlist-modify-public user-top-read '

sp_oauth = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope)

# Use get_cached_token() to try to retrieve an access token from the cache
token_info = sp_oauth.get_cached_token()

# If the cache is empty or the access token has expired, get_cached_token() will return None
if not token_info:
    # In that case, open the authorization URL in the default web browser and prompt the user to log in and grant permission
    auth_url = sp_oauth.get_authorize_url()
    print(f'Please log in and grant permission at the following URL: {auth_url}')
    # Wait for the user to grant permission
    input("Press enter once you have granted permission")
    # Retrieve the access token
    token_info = sp_oauth.get_access_token()

# Extract the access token and refresh token from the response
access_token = token_info['access_token']
refresh_token = token_info['refresh_token']

# Create a Spotify client
spotify = spotipy.Spotify(auth=access_token)

# Get the user's top 100 replayed songs
results = spotify.current_user_top_tracks(time_range="short_term", limit=100)
tracks = results["items"]

# Extract the track IDs
track_ids = [t["id"] for t in tracks]

# Get the user's profile information
profile = spotify.current_user()

# Get the user's display name (will be used to create the playlist)
username = profile["display_name"]
playlist_name = "Top 100 Replayd Songs"

# Create the playlist
playlist = spotify.user_playlist_create(username, playlist_name)
playlist_id = playlist["id"]


# Add the tracks to the playlist
for i in range(0, len(track_ids), 100):
    spotify.user_playlist_add_tracks(username, playlist_id, track_ids[i:i+100])


print(f"Successfully created playlist '{playlist_name}' with the user's top 100 replayed songs.")
