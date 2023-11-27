import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.title("Superstore data")
df = pd.read_excel("sample_-_superstore.xls")
# pip install xlrd
st.write(df.head())

region = st.selectbox("Target region", ["East", "West", "South", "Central"])
df_region = df[df["Region"]==region]
st.write(region)

fig, ax = plt.subplots()
ax = plt.scatter(df_region["Sales"], df_region["Profit"])
st.pyplot(fig)