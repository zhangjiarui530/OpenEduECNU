import dialogue
# import outlineGenerate
import question
# import pptGenerate
# import courseware
import streamlit as st
import os
from streamlit_option_menu import option_menu

# st.set_page_config(
#     "OpenEduECNU",
#     os.path.join("img", r"C:\开放原子\4.18\class_assistant\pic\logo.jpg"),
#     menu_items={
#         'About': f"""欢迎使用 OpenEduTech 1.0！"""
#     }
# )
#
# PAGES = {"智能问答": dialogue, "智能出题": question, "智慧大纲": outlineGenerate}
# st.sidebar.title('OpenEduTech')
# selection = st.sidebar.radio("", list(PAGES.keys()))
# page = PAGES[selection]
# page.app()

st.set_page_config(
    page_title="智能问答与出题",  # 页面标题
    page_icon=os.path.join("img", r"C:\开放原子\4.18\class_assistant\pic\logo.jpg"),  # 页面图标
    layout="wide",  # 页面布局
    initial_sidebar_state="expanded"  # 初始边栏状态
)


st.markdown("""
        <style>
            .sidebar.sidebar-content {
                background-color: #add8e6; /* 侧边栏背景颜色为淡蓝色 */
            }
        </style>

        """, unsafe_allow_html=True)

with st.sidebar:
    # 设置菜单项
    # st.title('OpenEduTech')
    st.image(
        os.path.join(
            "img",
            r"C:\开放原子\4.17\class_assistant\pic\title3.png"
        ),
        use_column_width=True
    )
    st.caption(
        f"""<p align="right">designed by OpenEduECNU</p>""",
        unsafe_allow_html=True,
    )
    # st.sidebar.markdown("## Menu")
    # selection = st.sidebar.radio("", ["智能问答", "智能出题", "智慧大纲"])
    pages = {
        "智能问答": {
            "icon": "chat",
        },
        "智能出题": {
            "icon": "hdd-stack",
            # "icon": "question-octagon",
        },
        # "智慧课件": {
        #     "icon": "book",
        # },
        # "智慧ppt": {
        #     "icon": "file-earmark-ppt"
        # }
    }
    options = list(pages)
    icons = [x["icon"] for x in pages.values()]
    selection = option_menu(
        "",
        options=options,
        icons=icons,
        menu_icon="chat-quote",
        default_index=0,
        styles={
            "container": {"padding": "5!important", "background-color": "#fafafa"},
            "icon": {"color": "orange", "font-size": "20px"},
            "nav-link": {"font-size": "18px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#043d6b"},
        }
    )

# 根据选择展示不同的页面
if selection == "智能问答":
    dialogue.app()
elif selection == "智能出题":
    question.app()
# elif selection == "智慧课件":
#     courseware.app()
# elif selection == "智慧ppt":
#     pptGenerate.app()
