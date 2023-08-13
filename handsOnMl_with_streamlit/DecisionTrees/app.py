import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from matplotlib.colors import ListedColormap

st.title("Iris Dataset Classification with Decision Tree") 

if st.button('Load Data'):
    # Load iris dataset
    iris = load_iris(as_frame=True)  
    X_iris = iris.data[["petal length (cm)", "petal width (cm)"]].values 
    y_iris = iris.target

# Create sidebar to control Decision Tree hyperparameters
st.sidebar.header('Model Hyperparameters')
max_depth = st.sidebar.slider("Max Depth", 2, 10, 3)

clf = DecisionTreeClassifier(max_depth=max_depth, random_state=42)

if st.button('Train Model'):
    # Train model on load iris data
    clf.fit(X_iris, y_iris)

# Create custom color map 
custom_cmap = ListedColormap(['#fafab0','#9898ff','#a0faa0'])

if st.button('Plot Decision Boundary'):
    # Plot decision boundary of trained model
    x_min, x_max = X_iris[:,0].min()-1, X_iris[:,0].max()+1
    y_min, y_max = X_iris[:,1].min()-1, X_iris[:,1].max()+1
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100),
                        np.linspace(y_min, y_max, 100))

    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)

    fig,ax = plt.subplots()  
    cntr = ax.contourf(xx, yy, Z, alpha=0.3, cmap=custom_cmap)

    for idx, cl in enumerate(np.unique(y_iris)):
        ax.scatter(x=X_iris[y_iris == cl, 0],  
                   y=X_iris[y_iris == cl, 1],
                   alpha=0.8,  
                   c=custom_cmap(idx),
                   marker=iris['target_names'][cl],
                   label=iris['target_names'][cl]) 

    ax.set_xlabel('Petal Length')
    ax.set_ylabel('Petal Width')
    ax.legend()
    ax.set_title('Decision Boundary')

    st.pyplot(fig)

# Allow prediction on user input    
st.subheader('Make Prediction')
pl = st.number_input('Petal Length', min_value=0.0, max_value=7.0, value=1.0)
pw = st.number_input('Petal Width', min_value=0.0, max_value=3.0, value=0.5)

if st.button('Predict'):
    prediction = clf.predict([[pl, pw]])
    probs = clf.predict_proba([[pl, pw]]).round(2)
            
    st.write("Prediction:", iris['target_names'][prediction])
    st.write("Probability:",probs)