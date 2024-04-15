import streamlit as st
import time
from localApp import Chat_Bot

chat_bot = Chat_Bot()


# Streamed response emulator
# def response_generator(q, type, num):
#     response = chat_bot.question(q, type, num)
#     for word in response.split():
#         yield word + " "
#         time.sleep(0.05)


def app():
    # 设置页面标题
    st.markdown("""
                <style>
                .title {
                    color: #ea580c;  # 颜色代码
                    font-size:50px;
                }
                /* 调整按钮样式 */
                .stButton>button {
                    width: 100%;
                    border: none;
                    color: #ffedd5; /* 按钮文字颜色改为深色以保持对比 */
                    padding: 10px;
                    text-align: center;
                    text-decoration: none;
                    display: inline-block;
                    font-size: 20px;
                    margin: 4px 2px;
                    transition-duration: 0.4s;
                    cursor: pointer;
                    background-color: #f97d1c; /* 按钮背景颜色改为橙色 */
                    border-radius: 20px;
                    border: 1px solid #ccc; /* 添加边框以在白色背景中区分按钮 */
                }
                .stButton>button:hover {
                    background-color: #f2cac9; /* 鼠标悬停时按钮颜色变为灰色，以便用户感知到交互效果 */
                    transform: scale(1.1); /* 轻微放大 */
                }
                </style>

                """, unsafe_allow_html=True)

    st.markdown('<h1 class="title">🚀智能出题助教</h1>', unsafe_allow_html=True)

    with st.sidebar:
        # with st.form(key='dispatch_form'):
        # input_file = st.file_uploader("", accept_multiple_files=True)
        input_file = st.file_uploader(label='参考教材', type=['pdf'])
        if input_file is not None:
            # if st.button("Upload"):
            # cols = st.columns(3)
            # with cols[1]:
            #     submit_button = st.button(label='提交')
            submit_button = st.button(label='提交')
            if submit_button:
                with st.spinner("Processing"):
                    time.sleep(2)
                    chat_bot.createVectorDB(input_file)

    with st.form(key='dispatch_form'):
        types = ["选择题",
                 "判断题",
                 "问答题",
                 ]
        type = st.selectbox("请选择题目类型：",
                            types,
                            index=0,
                            # on_change=on_mode_change,
                            key="type",
                            )
        num = st.slider("请选择题目数量：", 0, 3, 2)

        user_query = st.text_area("", placeholder='请输入...')
        if user_query is not None:
            cols = st.columns(3)
            with cols[1]:
                submit_button2 = st.form_submit_button(label='提交')
            if submit_button2:
                response_placeholder = st.empty()
                st.warning("题目生成中，请稍候...")
                response = chat_bot.question(user_query, type, num)
                response_placeholder.empty()
                st.success(response)
