import pickle
import streamlit as st
import requests
import base64
import os

# Function to fetch movie poster using TMDB API
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        poster_path = data.get('poster_path', '')
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500/{poster_path}"
    return "https://via.placeholder.com/500x750?text=No+Image"

# Recommendation function
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    recommended_movie_names = []
    recommended_movie_posters = []
    recommended_movie_ids = []

    for i in distances[1:11]:  # Top 5 recommendations
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_ids.append(movie_id)
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters, recommended_movie_ids


# Function to set a local background image
def add_background_image_local(image_file):
    with open(image_file, "rb") as image:
        encoded_image = base64.b64encode(image.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/png;base64,{encoded_image});
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_background_image_local("3.jpg")

# Function to display the logo with a round effect
@st.cache_resource
def display_logo(logo_path,title):
    if os.path.exists(logo_path):
        with open(logo_path, "rb") as logo_file:
            encoded_logo = base64.b64encode(logo_file.read()).decode()

        st.sidebar.markdown(
            f"""
                    <div style="display: flex; align-items: center;">
                        <img src="data:image/png;base64,{encoded_logo}" style="border-radius: 50%; width: 60px; height: 60px; margin-right: 10px;">
                        <h3 style="margin: 0;">{title}</h3>
                    </div>
                    """,
            unsafe_allow_html=True
        )


logo_path = "wall.webp"
display_logo(logo_path,"POPCORN PIKS",)

st.sidebar.markdown("<hr style='margin: 20px 0;'>", unsafe_allow_html=True)

st.sidebar.header("Join Telegram")
st.sidebar.link_button("Download Movies", "https://t.me/+c-7dv7jB9dI3MTNl")
st.sidebar.title(" ")
st.sidebar.markdown("<hr style='margin: 20px 0;'>", unsafe_allow_html=True)

st.sidebar.header("Contact Us")
st.sidebar.write("Email: yuvrajkumarsingh303@gmail.com")
st.sidebar.write("Linkedin: https://www.linkedin.com/in/yuvraj-kumar-78a669323/")


# Streamlit app
st.title('Popcorn Piks')

# Load data
movies = pickle.load(open('movies.pkl', 'rb'))  # DataFrame with 'title' and 'movie_id'
similarity = pickle.load(open('similarity.pkl', 'rb'))  # Similarity matrix

# Dropdown for movie selection
movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

# Show recommendations when button is clicked
if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters, recommended_movie_ids = recommend(selected_movie)

    # Display recommendations in columns
    cols = st.columns(5)
    for i, col in enumerate(cols):
        with col:
            st.text(recommended_movie_names[i])
            st.image(recommended_movie_posters[i])
            st.caption(f"Movie ID: {recommended_movie_ids[i]}")

st.link_button("Download Movies", "https://t.me/+c-7dv7jB9dI3MTNl")