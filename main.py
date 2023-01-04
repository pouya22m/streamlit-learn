import streamlit as st
import pandas as pd

header = st.container()
data = st.container()

with header:
	st.title("ASO")
	st.text("text text")

with data:
	st.title("Data")
	df = pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/b39d5655-ecc6-4651-8cce-af053d87fec5/data/latest')
	st.write(df.head())

	st.subheader("chart title")
	timeframe_dist = pd.DataFrame(df['TIMEFRAME'].value_counts())
	st.bar_chart(timeframe_dist)

	st.slider("something range", min_value=10, max_value=100, value=20, step=10)