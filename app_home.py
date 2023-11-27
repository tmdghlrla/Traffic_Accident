import streamlit as st
import base64
import PIL.Image as image
from urllib import request

def app_home_run() :        
    st.image('https://i.imgur.com/dJI9hii.jpg', width=700)
    st.text('2005년부터 2022년까지 시도별 교통사고 데이터입니다.')

    # st.markdown(
    #      f"""
    #      <style>
    #      .stApp {{
    #          background-image: url("https://i.imgur.com/dJI9hii.jpg");
    #          background-attachment: fixed;
    #          background-size: auto
             
    #      }}
    #      </style>
    #      """,
    #      unsafe_allow_html=True
    #  )