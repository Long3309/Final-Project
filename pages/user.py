import streamlit as st
import pandas as pd
import plotly.express as px

import plotly.graph_objects as go
import plotly.figure_factory as ff
st.set_page_config(layout="wide")
st.header("CS313 - Final Project App")
 

# SoMH = st.slider("Chọn tổng số môn học bạn đã học", min_value = 1, max_value = 200,
#                  step = 1, value = 10)
# MaMH_lst = []
# score_lst = []
# for i in range(0,SoMH):
#     st.markdown("Nhập mã môn học")
#     MaMH = st.text_input(label = f"{i}",label_visibility="collapsed")
#     score = st.number_input(label = f"score {i}", label_visibility="collapsed", step=1.0, max_value=10.0, min_value=0.0)
#     MaMH_lst.append(MaMH)
#     score_lst.append(score)

uploaded_file = st.file_uploader("NHẬP FILE ĐIỂM DƯỚI DẠNG EXCEL HOẶC CSV")
if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
    except:
        df = pd.read_excel(uploaded_file)
    columns = df.columns
    select = st.multiselect("", options = columns, default = columns[0])
    button = st.button("Tìm môn học")
    if button:
        df[select]

# Tổng quan theo Khoa SV
tongquan_khoasv = pd.read_pickle("tongquan_khoasv.pkl")
loai_MH =  st.selectbox("CHỌN LOẠI MÔN HỌC", options=tongquan_khoasv["Loại MH"].unique())
khoaSV = st.selectbox("CHỌN KHOA SINH VIÊN", options=tongquan_khoasv["KhoaSV"].unique())
namhoc = st.number_input("CHỌN NĂM HỌC", min_value=2006, max_value=2022, step = 1)
tongquan_khoasv_selected = tongquan_khoasv.loc[(tongquan_khoasv["Loại MH"] == loai_MH) & (tongquan_khoasv["KhoaSV"] == khoaSV)
                                                & (tongquan_khoasv["NamHoc"] == namhoc)]
# tongquan_khoasv_selected.columns = ["MaMH", "count"]
fig = px.histogram(tongquan_khoasv_selected,
                   x = "MaMH",
                   text_auto=True,
                   title= f"Số lượng sinh viên `{khoaSV}` học các môn `{loai_MH}`")
fig.update_traces(textposition = "outside")
fig.update_layout(barmode='stack', xaxis={'categoryorder':'total descending'})
st.plotly_chart(fig, use_container_width=True)
