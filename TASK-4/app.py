import streamlit as st
import pickle
import pandas as pd
import gzip

# Function to load the compressed similarity matrix
def load_compressed_similarity(filename):
    with gzip.open(filename, 'rb') as f:
        similarity_matrix = pickle.load(f)
    return similarity_matrix

# Load precomputed and compressed movie similarity matrix
similarity = load_compressed_similarity('similarity.pkl.gz')

# Load movie data
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

# Function to recommend similar movies
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),
                            reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = [movies.iloc[i[0]].title for i in movies_list]
    return recommended_movies

# Streamlit app title
st.title('Movie Recommendation System')

# Dropdown menu to select a movie
selected_movie_name = st.selectbox(
    'Suggest movies similar to?', movies['title'].values)

# Button to trigger movie recommendations
if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)

    # Display the selected movie
    st.write(f"Movies similar to {selected_movie_name}:")

    # Display recommended movies
    for recommended_movie in recommendations:
        st.write(recommended_movie)
