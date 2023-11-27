import streamlit as st

def app_prevention_run() :    
    
    transportation = ['운전자','보행자']
    selected_view = st.selectbox('예방법', transportation)

    if selected_view == transportation[0] :
        st.text('출처:전라북도교육청')
        st.image('https://news.jbe.go.kr/upload_data/board_data/BBS_0000191/162365714867017.jpg', width=600)
        st.text('')
        st.text('')
        st.text('출처:도로교통공단')
        st.image('https://www.safetimes.co.kr/news/photo/202203/109177_92301_647.png', width=600)
        
    elif selected_view == transportation[1] :
        st.text('출처 : 한국교통안전공단')
        st.image('https://savethelife.kr/wp-content/uploads/2020/09/%EB%B3%B4%ED%96%89_800-1000-1-1.png', width=600)
    else : 
        st.text('')