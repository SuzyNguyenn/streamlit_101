import streamlit as st
import pandas as pd

st.write('Hello World')
st.header('First Webapp')

st.image('media/dog-beach-lifesaver.png')

menu = ['Home','About me','Read Data']

choice = st.sidebar.selectbox('Menu',menu)

if choice == ' Home':
    st.write('Hello World')
    st.header('First Webapp')

    st.image('streamlit_101/media/dog-beach-lifesaver.png')

    col1,col2 = st.columns(2)

    with col1:
        dog_name = st.text_input('What is your dog name?')
        st.write('Your dog name:',dog_name)
    with col2:
        age = st.slider('Dog age',min_value=1,max_value=100)
        st.write('Your dog age:',age)
elif choice == 'Read Data':
    df = pd.read_csv('media/AB_NYC_2019.csv')
    st.dataframe(df)

elif choice == 'About me':
    fileUp = st.file_uploader('Upload file',type=['jpg','png','jpeg'])
    st.image(fileUp)


    