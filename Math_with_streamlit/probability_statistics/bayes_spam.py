import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.datasets import fetch_20newsgroups # 使用该数据集作为例子

# 加载数据
data = fetch_20newsgroups(subset='all', categories=['sci.med', 'soc.religion.christian'], remove=('headers', 'footers', 'quotes'))

X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=42)

# 特征提取
vectorizer = CountVectorizer(stop_words='english', max_features=5000)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# 训练朴素贝叶斯分类器
clf = MultinomialNB()
clf.fit(X_train_vec, y_train)

# 在Streamlit上创建UI
st.title('贝叶斯垃圾邮件分类器')

user_input = st.text_area("输入要分类的文本:")

if user_input:
    user_vec = vectorizer.transform([user_input])
    prediction = clf.predict(user_vec)
    
    if prediction[0] == 0:
        st.write("预测结果：科学医学文章")
    else:
        st.write("预测结果：宗教相关文章")

st.write("注意：这是一个基于‘sci.med’和‘soc.religion.christian’两个类别的简化版分类器，仅用于演示。")
