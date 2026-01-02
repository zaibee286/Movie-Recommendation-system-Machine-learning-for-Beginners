from unicodedata import name
import requests
import streamlit as st
import pickle
import pandas as pd


import streamlit as st

st.set_page_config(
    page_title="Movie Recomendation App",
    page_icon="🎥",
    
)


def fetch_poster(movie_id):
    response=requests.get("https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']
    

def recommend(movie):
    movie_index=movies[movies["title"]==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommend_moives=[]
    movie_id=[]
    for i in movies_list:
        movie_id.append(movies.iloc[i[0]].movie_id)
        recommend_moives.append(movies.iloc[i[0]].title)
    return recommend_moives, movie_id
   

###   set your files path here   ###

movies_list=pickle.load(open("movies_list.pkl","rb"))
movies=pd.DataFrame(movies_list)

similarity=pickle.load(open("similarity.pkl","rb")) 





st.title("Movie Recommendation System")


def rcmd(id):

    name = st.selectbox("Search here !",movies["title"].values,)
    current_movie_id=movies[movies["title"]==name].iloc[0].movie_id
    

   

    st.image(fetch_poster(current_movie_id), caption=name)    
    if st.button("RECOMMENDATIONS"):

        recom, movie_ids = recommend(name)
    
    


        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.text(recom[0])
            st.image(fetch_poster(movie_ids[0]))

        with col2:
            st.text(recom[1])
            st.image(fetch_poster(movie_ids[1]))

        with col3:
            st.text(recom[2])
            st.image(fetch_poster(movie_ids[2]))
        with col4:
            st.text(recom[3])
            st.image(fetch_poster(movie_ids[3]))
        with col5:
            st.text(recom[4])
            st.image(fetch_poster(movie_ids[4]))
rcmd(name)
        
