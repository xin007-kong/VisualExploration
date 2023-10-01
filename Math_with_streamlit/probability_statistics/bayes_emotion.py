import numpy as np
import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.datasets import fetch_20newsgroups
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
import random


def load_data():
    return fetch_20newsgroups(subset='all', categories=['rec.autos', 'comp.graphics'], remove=('headers', 'footers', 'quotes'))


def display_sample_reviews(data, num_samples=3):
    positive_indices = [i for i, t in enumerate(data.target) if t == 0]
    negative_indices = [i for i, t in enumerate(data.target) if t == 1]
    selected_positive = random.sample(positive_indices, num_samples)
    selected_negative = random.sample(negative_indices, num_samples)

    st.write("### 正面评论：")
    for i in selected_positive:
        st.write(data.data[i])
        st.write("---")

    st.write("### 负面评论：")
    for i in selected_negative:
        st.write(data.data[i])
        st.write("---")


def plot_data_distributions(data):
    df = pd.DataFrame(data.target, columns=["category"])

    fig, ax = plt.subplots()
    sns.countplot(data=df, x="category", ax=ax, palette="viridis")
    ax.set_xticklabels(data.target_names)
    ax.set_ylabel("Count")
    ax.set_title("Number of documents per category")
    st.pyplot(fig)


def plot_top_words(data, n=20):
    vectorizer = CountVectorizer(stop_words='english', max_features=n)
    data_vec = vectorizer.fit_transform(data.data)
    sum_words = data_vec.sum(axis=0)
    words_freq = [(word, sum_words[0, idx])
                  for word, idx in vectorizer.vocabulary_.items()]
    words_freq = sorted(words_freq, key=lambda x: x[1], reverse=True)
    df_words = pd.DataFrame(words_freq, columns=["word", "count"])

    fig, ax = plt.subplots(figsize=(12, 8))
    sns.barplot(x="count", y="word", data=df_words, palette="viridis", ax=ax)
    ax.set_title(f"Top {n} words by frequency")
    st.pyplot(fig)


def train_bayes_classifier(X_train, y_train):
    vectorizer = CountVectorizer(stop_words='english', max_features=5000)
    X_train_vec = vectorizer.fit_transform(X_train)
    clf = MultinomialNB()
    clf.fit(X_train_vec, y_train)
    return vectorizer, clf


def display_bayes_analysis(user_input, vectorizer, clf):
    user_vec = vectorizer.transform([user_input]).toarray()[0]

    st.write("### 输入句子的词频统计")
    for word, count in zip(vectorizer.get_feature_names_out(), user_vec):
        if count > 0:
            st.write(f"{word}: {count}")

    st.write("### 输入句子的条件概率")
    prob_word_given_class = np.exp(clf.feature_log_prob_)
    class_probs = np.exp(clf.class_log_prior_)
    product_probs = class_probs.copy()

    st.markdown("#### 计算后验概率")
    st.markdown(f"\[ P(正面|句子) = P(正面) \]")
    st.markdown(f"\[ P(负面|句子) = P(负面) \]")

    for word, count in zip(vectorizer.get_feature_names_out(), user_vec):
        if count > 0:
            word_prob = prob_word_given_class[:,
                                              vectorizer.vocabulary_[word]]
            st.write(
                f"P({word}|正面) = {word_prob[0]:.4f}, P({word}|负面) = {word_prob[1]:.4f}")
            st.markdown(f"\[ P(正面|句子) = P(正面|句子) \times P({word}|正面) \]")
            st.markdown(f"\[ P(负面|句子) = P(负面|句子) \times P({word}|负面) \]")
            product_probs *= word_prob

    total_prob = np.sum(product_probs)
    post_probs = product_probs / total_prob

    st.markdown("#### 归一化后验概率")
    st.markdown(
        f"\[ P(正面|句子) = \frac{{P(正面|句子)}}{{P(正面|句子) + P(负面|句子)}} = {post_probs[0]:.4f} \]")
    st.markdown(
        f"\[ P(负面|句子) = \frac{{P(负面|句子)}}{{P(正面|句子) + P(负面|句子)}} = {post_probs[1]:.4f} \]")

    prediction = np.argmax(post_probs)
    if prediction == 0:
        st.write("预测结果：正面评论")
    else:
        st.write("预测结果：负面评论")


def main():
    st.title('基于朴素贝叶斯的情感分析')
    st.write("朴素贝叶斯计算公式: \( P(y|X) = \frac{P(X|y) \times P(y)}{P(X)} \)")

    # Load data
    data = load_data()

    # Display some positive and negative reviews
    display_sample_reviews(data)

    # Plot data distributions
    plot_data_distributions(data)
    plot_top_words(data)

    # Train Naive Bayes Classifier
    X_train, _, y_train, _ = train_test_split(
        data.data, data.target, test_size=0.2, random_state=42)
    vectorizer, clf = train_bayes_classifier(X_train, y_train)

    # Get user input and analyze
    user_input = st.text_area("输入要分类的文本:")
    if user_input:
        display_bayes_analysis(user_input, vectorizer, clf)


if __name__ == "__main__":
    main()
