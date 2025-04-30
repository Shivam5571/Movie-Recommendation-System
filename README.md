# 🎬 Movie Recommendation System

This is a Content-Based Movie Recommendation System built using Python. It suggests similar movies based on metadata such as genre, keywords, cast, and crew using techniques like TF-IDF vectorization and cosine similarity.

---

## 📌 Features

- Recommends similar movies based on your input
- Uses metadata like genres, keywords, cast, and crew
- Calculates similarity using cosine similarity
- Simple web interface (Streamlit or Flask)

---

## 🗃️ Dataset

The project uses movie data files (e.g., `movies.csv`, `credits.csv`) sourced from [TMDB (The Movie Database)](https://www.themoviedb.org/). These CSV files are used offline in the project.

---

## 🔌 APIs

- This version does **not use live APIs**.
- Movie data originally comes from the **TMDB API**, but it's used in CSV format for this project.
- You can later integrate the TMDB API to dynamically fetch posters and additional movie info.

---

## 📦 External Libraries & Dependencies

- **Python 3.7+**
- `pandas` – data manipulation
- `numpy` – numerical computations
- `scikit-learn` – machine learning tools
- `difflib` – fuzzy matching for user input
- `ast`, `json` – data parsing
- `streamlit` or `flask` – for web interface

---

## 🛠️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Shivam5571/Movie-Recommendation-System.git
cd Movie-Recommendation-System
