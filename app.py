from streamlit_option_menu import option_menu
import streamlit as st
import pandas as pd

from app_home import app_home_run
from app_situation import app_situation_run
from app_prevention import app_prevention_run

def main() :
    st.title('시도별 교통사고')

    side_menu=['홈','현황', '사고 예방법']
    
    with st.sidebar:
        choice_menu = option_menu("Menu", side_menu,
                         icons=['house', 'kanban', 'car-front'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "4!important", "background-color": "#ccbc97"},
        "icon": {"color": "black", "font-size": "25px"},
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#efe2c4"},
        "nav-link-selected": {"font-color": "#000000","background-color": "#efe2c4"},
    }
    )

    if choice_menu == side_menu[0] :
        app_home_run()
    elif choice_menu == side_menu[1] :
        app_situation_run()
    elif choice_menu == side_menu[2] :
        app_prevention_run()


if __name__ == '__main__' :
    main()