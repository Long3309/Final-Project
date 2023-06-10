import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
st.set_page_config(layout="wide")
st.header("CS313 - Final Project App")

tongquan = pd.read_pickle("tongquan.pkl")
fig = px.histogram(tongquan, x = "Diem_HP", text_auto=True, nbins = 20,
                   title= "Thông tin điểm thi sinh viên")
fig.update_traces(textposition = "outside")
st.plotly_chart(fig, use_container_width=True)