from streamlit_option_menu import option_menu
import streamlit as st
import pandas as pd

from app_home import app_home_run
from app_situation import app_situation_run

def main() :
    st.title('시도별 교통사고')
    st.subheader('2005년~2022년 자료')


#     st.markdown(
#     """
#     <style>
#     .reportview-container {
#         background: url("https://black-jay.com/web/product/big/20200522/63d3974a6ecd92275e087b3b78b82fa0.jpg")
#     }
#    .sidebar .sidebar-content {
#         background: url("https://black-jay.com/web/product/big/20200522/63d3974a6ecd92275e087b3b78b82fa0.jpg")
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

    side_menu=['Home','현황']
    # choice_menu = st.sidebar.selectbox('메뉴', options=side_menu)
    # choice_menu = st.sidebar.selectbox('Menu', ('페이지1', '페이지2', '페이지3'))
    with st.sidebar:
        choice_menu = option_menu("Menu", ["Home", "현황", "페이지3"],
                         icons=['house', 'kanban', 'bi bi-robot'],
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


if __name__ == '__main__' :
    main()