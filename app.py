import streamlit as st
import pandas as pd
import requests
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Function to fetch poster using Saavn API
def fetch_poster(music_title):
    response = requests.get("https://saavn.dev/api/search?query={}&page=1&limit=2".format(music_title))
    data = response.json()
    return data['data']['topQuery']['results'][0]['image'][2]['url']

# Read the CSV file containing music data
df = pd.read_csv(r"C:\Users\santhoshi\OneDrive\Desktop\Santhoshi_Projects\Ml Projects\Music_recommendation\ex.csv")

# Set the title of the web app
st.title("Music Recommendation System")

# Display a dropdown to select a song
selected_option = st.selectbox('Select a song:', df['Song-Name'].unique())

# Show the selected song
st.write('Your selected Song is:', selected_option)

# Drop any NaN values and duplicates from the dataframe
df.dropna(inplace=True)
df = df.drop_duplicates()

# Preprocessing: Extract first three characters from 'User-Rating' column
df['User-Rating'] = df['User-Rating'].apply(lambda x: x[:3])

# Preprocessing: Remove spaces from 'Album/Movie' and 'Singer/Artists' columns
df['Album/Movie'] = df['Album/Movie'].str.replace(" ", "")
df['Singer/Artists'] = df['Singer/Artists'].str.replace(" ", "")

# Create tags based on 'Singer/Artists', 'Genre', 'Album/Movie', and 'User-Rating' columns
df['tags'] = df['Singer/Artists'] + ' ' + df['Genre'] + ' ' + df['Album/Movie'] + ' ' + df['User-Rating']
updated_df = df[['Song-Name', 'tags']]

# Lowercase and replace commas in 'tags' column
updated_df['tags'] = updated_df['tags'].apply(lambda x: x.lower())
updated_df['tags'] = updated_df['tags'].str.replace(",", " ")

# Vectorize tags using CountVectorizer
cv = CountVectorizer(max_features=2000)
vectors = cv.fit_transform(updated_df['tags']).toarray()

# Calculate cosine similarity between vectors
similarity = cosine_similarity(vectors)

# Rename the 'Song-Name' column to 'title'
updated_df.rename(columns={'Song-Name': 'title'}, inplace=True)

# Function to recommend similar songs
def recommend(music):
    music_index = updated_df[updated_df['title'] == music].index[0]
    distances = similarity[music_index]
    music_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:7]
    recommended_song=[]
    recommended_poster= []
    for i in music_list:
        a = updated_df.iloc[i[0]].title
        recommended_song.append( updated_df.iloc[i[0]].title)
        recommended_poster.append(fetch_poster(a))
    return recommended_song, recommended_poster

# Example usage: When the 'Show Recommendation' button is clicked
if st.button('Show Recommendation'):
    recommended_music_name, poster = recommend(selected_option)
    # Split the recommendations into two columns for better layout
    col1, col2, col3 = st.columns(3)
    col4, col5, col6 = st.columns(3)
    # Display the recommended songs and their posters
    with col1:
        st.text(recommended_music_name[0])
        st.image(poster[0])
    with col2:
        st.text(recommended_music_name[1])
        st.image(poster[1])
    with col3:
        st.text(recommended_music_name[2])
        st.image(poster[2])
    with col4:
        st.text(recommended_music_name[3])
        st.image(poster[3])
    with col5:
        st.text(recommended_music_name[4])
        st.image(poster[4])
    with col6:
        st.text(recommended_music_name[5])
        st.image(poster[5])
