import streamlit as st
# from creat_file1 import create_file
from creat_file1 import create_file
import time


# def main():
def app():
    start_time = time.time()

    # st.set_page_config(
    #     page_title="教学大纲智慧生成", page_icon=":rocket:")

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

    st.markdown('<h1 class="title">🚀教学大纲智慧生成</h1>', unsafe_allow_html=True)

    # logo_url = r"C:\Users\18017\Desktop\logo.png"

    # st.markdown(f'<img src="{logo_url}" alt="Logo" style="height:50px;"> <h1 class="title">课程智能助教-教学大纲智慧生成</h1>', unsafe_allow_html=True)

    # 创建输入表单
    with st.form(key='dispatch_form'):
        # 创建文本输入框
        course_name = st.text_input(label='课程名称')
        course_alltime = st.text_input(label='总学时')
        course_labtime = st.text_input(label='实验学时')
        course_sub = st.text_input(label='适用专业')

        # 创建下拉选择框
        course_type = st.selectbox(label='课程性质', options=['学科基础', '大类平台', '专业必修', '专业选修'])

        # 创建文件上传框
        file = st.file_uploader(label='参考教材', type=['pdf'])

        # 创建多行文本输入框
        other_condition = st.text_area(label='其他要求', placeholder='请输入其他要求，可空')

        # 创建提交按钮
        col1, col2, col3 = st.columns([2, 1, 2])
        with col2:
            submit_button = st.form_submit_button(label='提    交')
    if submit_button:
        create_file(course_name, course_alltime, course_labtime, course_sub, course_type, file)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(elapsed_time)


# if __name__ == '__main__':
#     main()
