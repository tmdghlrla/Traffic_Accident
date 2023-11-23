import streamlit as st
import base64

def app_home_run() :
    url = 'http://jeski.org/data/cheditor4/1901/1546660848_%EA%B3%BC%EC%86%8D%EC%9C%84%EB%B0%98%EC%9A%A9%20%EA%B0%9C%EB%85%90%EB%8F%84%20.jpg'    
    st.text('')
    st.text('이 앱은 2005년부터 2022년까지 시도별 교통사고 데이터에 대한 내용입니다.')
    st.text('')
    st.image(url,output_format='auto')