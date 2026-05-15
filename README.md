## Project Overview
FlikPik is a hybrid movie recommendation app built with Streamlit. It recommends movies using collaborative filtering, matrix factorization, genre similarity, and popularity scoring.

## Features
- Personalized recommendations
- Similar movie search
- Movie title search
- User ratings/profile building
- TMDB posters
- YouTube trailers
- Streaming availability mockup
- Social buzz metrics
- AI-style movie chatbot

## Dataset
This project uses the MovieLens small dataset, including movies, ratings, links, and tags.

## Model Approach
The recommender combines:
- Collaborative filtering
- Matrix factorization
- Genre-based similarity
- Popularity fallback

## How to Run
pip install -r requirements.txt
streamlit run app/app.py

## Environment Variables
TMDB_API_KEY=your_key_here
YOUTUBE_API_KEY=your_key_here

## Future Improvements
- Real streaming availability API
- Real social media sentiment API
- Stronger actor/director search
- User login system
- Cloud database for ratings
