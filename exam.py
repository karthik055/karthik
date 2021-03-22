import streamlit as st
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
import numpy as np
st.text_input('User Name:')
file = st.file_uploader("select file:",type=['csv'])
k = st.button('submit')
if k == True:
    df = pd.read_csv(file)
    st.write(df)
st.markdown("output 1")
st.write(df.head())


st.markdown("output 2")
fig = plt.figure()
y = fig.add_subplot(1,1,1)
y.scatter(df['petal.length'],df['sepal.length'])
y.set_xlabel("petal.length")
y.set_ylabel("sepal.length")
st.write(fig)
