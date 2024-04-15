import fitz  # PyMuPDF
from collections import Counter
import jieba
import re

# 提取pdf关键词
def extract_high_freq_words_from_file(file_obj, top_n=20):
 
    stop_words = set(["的", "是", "在", "我", "有", "和", "就", "等", "可以", "了", "进行", "对", "都","功能","不同","图","认","人","从","型","时","结构","例如","数","描述","表示","于","类型","要",
                      "为", "与", "中", "通过", "使用", "上", "一个", "共", "或", "并", "将", "也","包括","年","指","被","不","一种","地","大","后","需要","应用","根据","方式","如图","请","步骤","一",
                        "它", "人们", "主要", "如", "单元","章节", "第", "由","下列","方面","一旦","而","以","其","具有","可","到","能","各种","所示","方法""常用","来","例","用","会","个","问题","分析"])

    def clean_and_split_text(text):
        words = jieba.cut(text)
        filtered_words = [word for word in words if word not in stop_words and re.match(r'[\u4e00-\u9fa5]+', word)]
        return filtered_words

    # 读取文件对象到内存
    file_content = file_obj.read()

    try:
        # 从内存中加载PDF
        doc = fitz.open(stream=file_content, filetype="pdf")
    except Exception as e:
        print("无法从文件对象加载PDF")
        print(e)
        return ""

    full_text = ""
    for page in doc:
        full_text += page.get_text()

    words = clean_and_split_text(full_text)
    word_counts = Counter(words)
    most_common_words = word_counts.most_common(top_n)

    doc.close()

    # 仅返回高频词，用顿号隔开
    return '、'.join([word for word, _ in most_common_words])
