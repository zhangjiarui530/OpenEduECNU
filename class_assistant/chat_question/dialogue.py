import streamlit as st
import time
from localApp import Chat_Bot

chat_bot = Chat_Bot()


# Streamed response emulator
def response_generator(user_query):
    response = chat_bot.chat(user_query)
    for word in response.split():
        yield word + " "
        time.sleep(0.05)


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

    st.markdown('<h1 class="title">🚀智能问答助教</h1>', unsafe_allow_html=True)

    # with st.sidebar:
    # with st.form(key='dispatch_form'):
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

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if user_query := st.chat_input("请输入..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": user_query})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(user_query)

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            response = st.write_stream(response_generator(user_query))
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
