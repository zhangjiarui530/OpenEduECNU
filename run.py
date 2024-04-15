import subprocess
import os


def run_command_new_window(cmd):
    """在新的命令行窗口中运行命令"""
    subprocess.run(f"start cmd.exe /k {cmd}", shell=True)


def main():
    base_dir = r"C:\OpenEduECNU"

    # 问答/出题
    os.chdir(os.path.join(base_dir, "class_assistant\\chat_question"))
    run_command_new_window("streamlit run OpenEduECNU1.py")
    # 大纲
    os.chdir(os.path.join(base_dir, "class_assistant\\courseware"))
    run_command_new_window("streamlit run OpenEduECNU2.py")

    # 恢复到原始工作目录
    os.chdir(base_dir)


if __name__ == "__main__":
    main()
