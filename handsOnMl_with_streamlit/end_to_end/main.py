import streamlit as st

import pandas as pd
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error


# 设置页面标题
st.title('机器学习项目教程')

# 定义加载数据的函数


@st.cache
def load_data():
   boston = load_boston()
   df = pd.DataFrame(boston.data, columns=boston.feature_names)
   df['MEDV'] = boston.target
   return df

# 数据加载与简要观察
if 'data' not in st.session_state:
    st.session_state.data = load_data()

st.markdown('### 加载数据')
st.write(st.session_state.data.head())

# 数据预处理函数


def process_data(data):
    X = data.drop(['target'], axis=1)
    y = data['target']
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test


# 执行数据预处理
process = st.button('执行数据预处理')
if process:
    X_train, X_test, y_train, y_test = process_data(st.session_state.data)

# 选择并训练模型
models = {
    '线性回归': linear_regression,
    '决策树': decision_tree
}
model_name = st.selectbox('选择模型', list(models.keys()))
model = models[model_name]()

if st.button('训练模型'):
    model.fit(X_train, y_train)

# 模型评估
if st.button('评估模型'):
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    st.write('MSE:', mse)

# 其他步骤如特征工程、超参数调优等

# import streamlit as st
# from sklearn.metrics import mean_squared_error
# from sklearn.model_selection import cross_val_score
# from sklearn.model_selection import GridSearchCV
# from utils import data_utils, ml_utils, plot_utils

# # Imaginary function to call OpenAI's API
# def explain(function_name):
#     explanation = "Explain the function and principle of " + function_name
#     return explanation

# # Load data
# if st.button('Load Data'):
#     data = data_utils.load_data()
#     st.write(data.head())
#     st.write(explain("load_data"))

# # Data exploration
# if st.button('Explore Data'):
#     st.subheader('Data Exploration and Visualization')
#     st.write(data.describe())
#     st.write(explain("describe"))

# # Plot
# if st.button('Visualize Data'):
#     fig = plot_utils.create_corr_plot(data)
#     st.pyplot(fig)
#     st.write(explain("create_corr_plot"))

# # Prepare data
# if st.button('Prepare Data'):
#     X_train, X_test, y_train, y_test = data_utils.prepare_data(data)
#     st.write(explain("prepare_data"))

# # Train model
# if st.button('Train Model'):
#     model = ml_utils.train_model(X_train, y_train)
#     st.write(explain("train_model"))

# # Fine tune model
# if st.button('Fine Tune Model'):
#     model = ml_utils.fine_tune_model(model, X_train, y_train)
#     st.write(explain("fine_tune_model"))

# # Present your solution
# if st.button('Evaluate Model'):
#     st.subheader('Model Performance')

#     # Predictions
#     y_pred = model.predict(X_test)
#     mse = mean_squared_error(y_test, y_pred)
#     st.write("Mean Squared Error on Test set : ", mse)
#     st.write(explain("predict and mean_squared_error"))

#     # Cross validation
#     cross_val = cross_val_score(model, X_train, y_train, cv=5)
#     st.write("Cross Validation Scores : ", cross_val)
#     st.write(explain("cross_val_score"))
