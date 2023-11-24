import streamlit as st
import base64
import PIL.Image as image

def app_home_run() :    
    st.image('https://i.imgur.com/dJI9hii.jpg')
    st.text('2005년부터 2022년까지 시도별 교통사고 데이터에 대한 내용입니다.')
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