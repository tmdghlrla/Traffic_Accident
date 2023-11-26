import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

def app_situation_run() :
    st.subheader('월별 교통사고 현황')
    st.text('자료 출처 : 인천데이터포털(https://www.incheon.go.kr/data/DATA010301)')

    df=pd.read_csv('data/Traffic_Accident.csv', index_col=0, encoding='cp949')
    
    radio_menu=['전체보기','도시별 보기', '월별 보기']

    selected_radio = st.radio('교통사고 현황', options=radio_menu)

    val_col = ['사고건수(건)','사망자수(명)','부상자수(명)']

    if selected_radio == radio_menu[0] :
        pressed_ch=st.checkbox('자료')
        if pressed_ch :
            st.dataframe(df)
        else :
            st.text('')
        
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

        chart2 = px.line(data_frame=df_city,x='월별', y=[val_col[0],val_col[2]], markers=True)
        
        chart2.update_layout(
        title='{} 교통사고(사고, 부상자) 현황'.format(selected_city),
        xaxis_title='월별',
        yaxis_title='사고(건)/부상자(명)'
        )

        st.plotly_chart(chart2)
        

        chart2_1 = px.line(data_frame=df_city,x='월별', y=val_col[1], markers=True)
        chart2_1.update_layout(title='{} 교통사고 사망자 현황'.format(selected_city))
        st.plotly_chart(chart2_1)
     
    elif selected_radio == radio_menu[2] :
        month = df['월별'].unique()

        selected_month=st.selectbox('월별 현황', month)

        df_month = df.loc[df['월별']==selected_month,].reset_index(drop=True)

        st.dataframe(df_month)  

        chart3 = px.line(data_frame=df_month, x='시도별', y=[val_col[0],val_col[2]], markers=True)
        chart3.update_layout(
        title='{} 교통사고(사고, 부상자) 현황'.format(selected_month),
        xaxis_title='지역',
        yaxis_title='사고(건)/부상자(명)'
        )
        st.plotly_chart(chart3)
        chart3_1 = px.line(data_frame=df_month, x='시도별', y=val_col[1], markers=True)
        chart3_1.update_layout(title='{} 교통사고 사망자 현황'.format(selected_month))
        st.plotly_chart(chart3_1)

    else :
        st.text('')
    

    
        
    