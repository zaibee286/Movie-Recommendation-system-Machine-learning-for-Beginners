import streamlit as st
import pickle

movies_list = pickle.load(open('practice areana/movies_list.pkl', 'rb'))
similarity = pickle.load(open('practice areana/similarity.pkl', 'rb'))

st.title('Movie Recommendation System')

selected_movie = st.selectbox(
    'Select a movie:', movies_list['title'].values)
if st.button('Recommend'):
    index = movies_list[movies_list['title'] == selected_movie].index[0]
    distances = similarity[index]
    movie_list = sorted(
        list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    st.subheader('Top 5 movie recommendations:')
    for i in movie_list:
        st.write(movies_list.iloc[i[0]].title)
