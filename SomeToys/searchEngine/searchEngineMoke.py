import streamlit as st
from collections import defaultdict

# 建立简单的倒排索引
documents = [
    "apple orange banana",
    "apple juice",
    "orange juice",
    "banana split"
]

index = defaultdict(set)

for doc_id, doc in enumerate(documents):
    for word in doc.split():
        index[word].add(doc_id)


def search(query):
    results = []
    for word in query.split():
        results.extend(index.get(word, []))
    # 排名：基于查询词在文档中的出现次数
    results.sort(key=lambda doc_id: sum(
        word in documents[doc_id] for word in query.split()), reverse=True)
    return [documents[doc_id] for doc_id in results]


# Streamlit UI
st.title("Simple Search Engine")

query = st.text_input("Enter your query:")
if query:
    results = search(query)
    st.write("Results:")
    for doc in results:
        st.write(doc)
