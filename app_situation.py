import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

def app_situation_run() :
    st.subheader('월별 교통사고 현황')

    df=pd.read_csv('data/Traffic_Accident.csv', index_col=0, encoding='cp949')
    
    radio_menu=['전체보기','도시별 보기', '월별 보기']

    selected_radio = st.radio('교통사고 현황', options=radio_menu)

    val_col = ['사고건수(건)','사망자수(명)','부상자수(명)']

    if selected_radio == radio_menu[0] :
        st.dataframe(df)
        selected_menu=st.selectbox('항목을 선택하세요', val_col)

        if selected_menu == val_col[0] : 
            chart=px.pie(data_frame= df, names= '시도별', values=val_col[0], title='2005년 ~ 2022년 교통 사고(건)')
            st.plotly_chart(chart)
        elif selected_menu == val_col[1] : 
            chart=px.pie(data_frame= df, names= '시도별', values=val_col[1], title='2005년 ~ 2022년 교통 사고(건)')
            st.plotly_chart(chart)
        elif selected_menu == val_col[2] : 
            chart=px.pie(data_frame= df, names= '시도별', values=val_col[2], title='2005년 ~ 2022년 교통 사고(건)')
            st.plotly_chart(chart)


    elif selected_radio == radio_menu[1] :
        city = df['시도별'].unique()
        
        selected_city=st.selectbox('시도별 현황', city)

        df_city = df.loc[df['시도별']==selected_city,].reset_index(drop=True)
        
        st.dataframe(df_city)

        chart2 = px.line(data_frame=df_city,x='월별', y=val_col, markers=True)

        st.plotly_chart(chart2)

    elif selected_radio == radio_menu[2] :
        month = df['월별'].unique()

        selected_month=st.selectbox('월별 현황', month)

        df_month = df.loc[df['월별']==selected_month,].reset_index(drop=True)

        st.dataframe(df_month)      
        chart3 = px.line(data_frame=df_month, x='시도별', y=val_col, markers=True)

        st.plotly_chart(chart3)

    else :
        st.text('')
    

    
        
    