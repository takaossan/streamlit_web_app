import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# データ分析関連(表)
df = pd.read_csv('./data/平均気温.csv',index_col='月')
st.dataframe(df)
st.table(df)

# データ分析関連(折れ線)
df = pd.read_csv('./data/平均気温.csv',index_col='月')
st.line_chart(df)
st.bar_chart(df['2021年'])

# matplotlib
fig, ax = plt.subplots()
ax.plot(df.index, df['2021年'])
ax.set_title('matplotlib graph')
st.pyplot(fig)