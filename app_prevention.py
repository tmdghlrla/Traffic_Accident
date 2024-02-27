import streamlit as st

def app_prevention_run() :    
    
    transportation = ['운전자','보행자']
    selected_view = st.tabs(transportation)

    with selected_view[0] :
        st.text('출처:도로교통공단')
        st.image('https://news.nateimg.co.kr/orgImg/aj/2020/11/26/20201126002914995914.jpg', width=600)
        st.text('')
        st.text('')
        st.text('출처:도로교통공단')
        st.image('https://www.safetimes.co.kr/news/photo/202203/109177_92301_647.png', width=600)
        
    with selected_view[1] :
        st.text('출처 : 서울특별시')
        st.image('https://mediahub.seoul.go.kr/wp-content/uploads/2017/03/aaa0489b47474c59dcf61aff73a50eb1.jpg', width=600)