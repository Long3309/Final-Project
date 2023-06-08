import streamlit as st
import pandas as pd
import plotly.express as px

import plotly.graph_objects as go
import plotly.figure_factory as ff
st.set_page_config(layout="wide")
st.header("CS313 - Final Project App")
# @st.cache_data()
# Load datasets từ local file
diemThi = pd.read_pickle("diemThi.pkl")
danhmucMH = pd.read_csv("data.csv")
danhmucMH.drop(["Unnamed: 0", "Số TT"], axis=1, inplace=True)
tomtatMH = pd.read_csv("data_script.csv")
tomtatMH.drop(["STT"],axis = 1,inplace=True)
# Lấy thông tin mã môn học
MaMH = diemThi["MaMH"].unique()
MaMH_Selected = st.selectbox("CHỌN MÃ MÔN HỌC", options=MaMH)
# Các dataframe lấy MaMH là mã môn học được chọn
df_diemThiMH = diemThi.loc[diemThi["MaMH"] == MaMH_Selected]
df_danhmucMH = danhmucMH.loc[danhmucMH["Mã MH"] == MaMH_Selected]
df_tomtatMH = tomtatMH.loc[tomtatMH["Mã MH"] == MaMH_Selected]

# Biểu diễn điểm thi của các môn học đã được chọn
tenmonhoc = df_danhmucMH["Tên MH (Tiếng Việt)"].values[0]
fig = px.histogram(df_diemThiMH, x = "Diem_HP",
                   color="NamHoc",
                   title= f"Thông tin điểm thi qua từng năm của môn học `{tenmonhoc}`")
st.plotly_chart(fig,use_container_width=True)

# Hiển thị các data thông tin về môn học được lựa chọn
st.dataframe(df_danhmucMH)
st.dataframe(df_tomtatMH, use_container_width=True)