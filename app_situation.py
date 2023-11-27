import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

def app_situation_run() :
    st.subheader('월별 교통사고 현황')
    st.text('자료 출처 : 인천데이터포털(https://www.incheon.go.kr/data/DATA010301)')

    df=pd.read_csv('data/Traffic_Accident.csv', index_col=0, encoding='cp949')
    
    radio_menu=['전체보기','도시별 보기', '월별 보기']

    selected_tabs = st.tabs(radio_menu)

    val_col = ['사고건수(건)','사망자수(명)','부상자수(명)']

    with selected_tabs[0] :        
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

    with selected_tabs[1] :
        city = df['시도별'].unique()
        
        selected_city=st.selectbox('시도별 현황', city)

        df_city = df.loc[df['시도별']==selected_city,].reset_index(drop=True)
        
        st.dataframe(df_city)
        st.text("{}에는 {}에 {}건으로 가장 많이 사고가 발생했고,".format(selected_city, list(df_city.loc[df_city[val_col[0]]==df_city[val_col[0]].max(),'월별'])[0],str(df_city[val_col[0]].max())))
        st.text("사망자수는 {}에 {}명,".format(list(df_city.loc[df_city[val_col[1]] == df_city[val_col[1]].max(),'월별'])[0],str(df_city[val_col[1]].max())))
        st.text("부상자수는 {}에 {}명으로 가장 많이 발생했습니다.".format(list(df_city.loc[df_city[val_col[2]] == df_city[val_col[2]].max(),'월별'])[0],str(df_city[val_col[2]].max())))

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
     
    with selected_tabs[2] :
        month = df['월별'].unique()

        selected_month=st.selectbox('월별 현황', month)

        df_month = df.loc[df['월별']==selected_month,].reset_index(drop=True)

        st.dataframe(df_month)
        st.text('{}에는 {}에서 {}건으로 가장 많이 사고가 발생했고,'.format(selected_month,list(df_month.loc[df_month[val_col[0]]==df_month[val_col[0]].max(),'시도별'])[0],df_month[val_col[0]].max()))
        st.text('사망자수는 {}에서 {}명,'.format(list(df_month.loc[df_month[val_col[1]]==df_month[val_col[1]].max(),'시도별'])[0],df_month[val_col[1]].max()))
        st.text('부상자수는 {}에서 {}명으로 가장 많이 발생했습니다.'.format(list(df_month.loc[df_month[val_col[2]]==df_month[val_col[2]].max(),'시도별'])[0],df_month[val_col[2]].max()))

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