# Movie Recommendation System

This project is a movie recommendation system that suggests movies to users based on their past preferences.

## Features

- Provides movie recommendations based on user preferences.
- Uses machine learning techniques, including content-based filtering.
- Utilizes Python, Pandas, and Scikit-learn.
- Includes a Streamlit web application for user interaction.

## Setup and Run Instructions
### 1. Prerequisites:
- Python 3.x
- pip (Python package installer)
### 2. Install Dependencies:
- Clone the repository to your local machine.
- Navigate to the project directory:
- Run the following command to install the required Python libraries:
- pip install pandas scikit-learn streamlit requests


### 3. Download Data Files:
- Ensure the following data files are in the same directory as the application:
  - tmdb_5000_movies.csv
  - tmdb_5000_credits.csv
  - movies.pkl
  - similarity.pkl
- Also, make sure you have the image files 3.jpg and wall.webp in the same directory.

### 4. Run the Application:
  - Open a terminal in the project directory.
  - Run the Streamlit application:
  streamlit run app.py


### 5. Usage:
   
- Open the web application in your browser (usually at http://localhost:8501).
- Select a movie from the dropdown menu.
- Click the "Show Recommendation" button to see the top 10 recommended movies.
### Data Sources
- TMDB 5000 Movies Dataset
- TMDB 5000 Credits Dataset
- TMDB API (for fetching movie posters)
### Project Structure
The project structure is as follows:
- app.py: The main Streamlit application.
- Movie_Recommendation_System (2).ipynb: Jupyter Notebook containing the data processing and model building code.
- tmdb_5000_movies.csv: Movie details dataset.
- tmdb_5000_credits.csv: Movie credits dataset.
- movies.pkl: Pickled Pandas DataFrame.
- similarity.pkl: Pickled similarity matrix.
3.jpg: Background image.
wall.webp: Logo image.
### Additional Information
The Streamlit app includes a sidebar with links to download movies from a Telegram channel, contact information, and a custom logo.
### Note
Ensure that all data files and dependencies are correctly set up for the application to run properly.
