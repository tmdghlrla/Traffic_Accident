import streamlit as st
import pandas as pd

from app_home import app_home_run
from app_situation import app_situation_run

def main() :
    st.title('2005년~2022년 시도별 교통사고')

    side_menu=['Home','현황']
    choice_menu=st.sidebar.selectbox('메뉴', options=side_menu)

    if choice_menu == side_menu[0] :
        app_home_run()
    elif choice_menu == side_menu[1] :
        app_situation_run()


if __name__ == '__main__' :
    main()