# import streamlit as st
# from data import load_data
# from model import train_model, predict
# from plot import plot_decision_boundary
# import numpy as np
# st.title("Iris Classifier")

# X, y = load_data()

# clf = train_model(X, y)

# fig = plot_decision_boundary(clf, X, y)
# st.pyplot(fig)

# st.subheader("Make Prediction")
# X_new = np.array([[st.number_input("Petal Length", 1.0, 7.0),
#                    st.number_input("Petal Width", 0.1, 2.0)]])

# y_pred = predict(clf, X_new)
# st.write(y_pred)

import streamlit as st

import numpy as np

from data import load_data
from model import train_model, predict  
from plot import plot_decision_boundary

st.title("Iris Classifier")

if st.button('Load Data'):
    st.session_state.X, st.session_state.y = load_data()
    st.write('Dataset loaded')
    
if st.button('Train Model'):
    if st.session_state.X is not None:
        st.session_state.clf = train_model(st.session_state.X, st.session_state.y)
        st.write('Model trained')
    else:
        st.warning('Please load data first')

if st.button('Visualize'):
    if st.session_state.clf is not None:
        fig = plot_decision_boundary(st.session_state.clf, st.session_state.X, st.session_state.y)
        st.pyplot(fig)
    else:
        st.warning('Please train model first')
        
if st.button('Predict'):
    st.session_state.pl = st.number_input('Petal Length', min_value=0.0, max_value=5.0) 
    st.session_state.pw = st.number_input('Petal Width', min_value=0.0, max_value=3.0)
    
    X_new = np.array([[st.session_state.pl, st.session_state.pw]])
    if st.session_state.clf is not None:
        pred = predict(st.session_state.clf, X_new)
        st.write(pred)
    else:
        st.warning('Please train model first')