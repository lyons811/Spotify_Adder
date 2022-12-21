Spotify Top 100 Replayd Songs

This code uses the Spotify Web API and the Spotipy Python library to create a playlist with the user's top 100 replayed songs in the short term.
Prerequisites

    You need to have a Spotify Developer account and create a new app to obtain a client ID and client secret.
    You need to have Spotipy installed. You can install it using pip install spotipy.

Usage

    Replace client_id and client_secret with your own client ID and client secret.
    Replace redirect_uri with the redirect URI you specified in your Spotify app.
    Run the code. You will be prompted to log in and grant permission to access your Spotify data.
    Once you have granted permission, the code will create a playlist with the user's top 100 replayed songs and add the tracks to the playlist.

Notes

    The code uses the user-library-read and user-top-read scopes to access the user's top replayed songs and playlist-modify-public scope to create a playlist and add tracks to it.
    The code uses the Spotify Web API's current_user_top_tracks and user_playlist_create endpoints.
