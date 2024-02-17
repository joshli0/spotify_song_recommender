import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import streamlit as st

#set up Spotify credentials
client_id = st.secrets['client_id']
client_secret = st.secrets['client_secret']
client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_recommendations(track_name):
    #get track URI
    results = sp.search(q=track_name, type='track')
    track_uri = results['tracks']['items'][0]['uri']

    #get recommended tracks
    recommendations = sp.recommendations(seed_tracks=[track_uri])['tracks']
    return recommendations

st.title("Music Recommender")

track = st.text_input('Enter a song name: ')
if track:
    init_track = sp.search(q=track, type = 'track')
    st.write(init_track['tracks']['items'][0]['name'] + ' by ' + init_track['tracks']['items'][0]['artists'][0]['name'])
    st.image(init_track['tracks']['items'][0]['album']['images'][0]['url'], width = 200)
    st.divider()
    st.header('Recommended Songs:')
    for i in get_recommendations(track):
        st.subheader(i['name'])
        st.write(' by ' + i['artists'][0]['name'])
        st.link_button("Listen on Spotify", i['external_urls']['spotify'])
        st.image(i['album']['images'][0]['url'], width = 350)
        st.divider()
