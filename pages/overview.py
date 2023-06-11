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
danhmucMH = pd.read_csv("danhmucMH.csv")
tomtatMH = pd.read_csv("data_script.csv")
tomtatMH.drop(["STT"],axis = 1,inplace=True)
tongquan = pd.read_pickle("tongquan.pkl")

# Lấy thông tin mã môn học
MaMH = diemThi["MaMH"].unique()
st.markdown("""
            # TÍNH NĂNG NHẬP MÃ MÔN HỌC
            Người dùng chọn môn học muốn biết thông tin điểm thi theo từng năm, hệ thống sẽ trả về dữ liệu điểm thi của
            môn học được lựa chọn và các thông tin liên quan đến môn học ở bên dưới.
            """, unsafe_allow_html=True)
MaMH_Selected = st.selectbox("CHỌN MÃ MÔN HỌC", options=MaMH)
# Các dataframe lấy MaMH là mã môn học được chọn
df_diemThiMH = diemThi.loc[diemThi["MaMH"] == MaMH_Selected]
df_danhmucMH = danhmucMH.loc[danhmucMH["MaMH"] == MaMH_Selected]
df_tomtatMH = tomtatMH.loc[tomtatMH["Mã MH"] == MaMH_Selected]

# Biểu diễn điểm thi của các môn học đã được chọn
tenmonhoc = df_danhmucMH["Tên MH (Tiếng Việt)"].values[0]
fig = px.histogram(df_diemThiMH, x = "Diem_HP",
                   color="NamHoc",
                   title= f"Thông tin điểm thi qua từng năm của môn học `{tenmonhoc}`")
st.plotly_chart(fig,use_container_width=True)

# Hiển thị các data thông tin về môn học được lựa chọn
st.markdown("### Thông tin về môn học được lựa chọn")
st.dataframe(df_danhmucMH)
st.markdown("### Mô tả về môn học được lựa chọn")
st.dataframe(df_tomtatMH, use_container_width=True)

# Chọn sinh viên để lấy ra điểm thi của sinh viên đó
st.markdown("""
            # TÍNH NĂNG NHẬP MSSV
            Người dùng có thể chọn SV muốn biết thông tin, hệ thống sẽ trả về thông tin điểm thi của sinh viên đó,
            đồng thời phân tích số lượng môn học mà sinh viên đó đã đăng ký, từ đó đưa ra dự đoán khoa mà sinh viên đó đang trực thuộc
            """, unsafe_allow_html=True)
MSSV = diemThi["MSSV"].unique()
SV = st.selectbox("CHỌN MÃ SỐ SINH VIÊN", options=MSSV)
diemThi_SV = diemThi.loc[diemThi["MSSV"] == SV]
col1, col2 = st.columns(2)
with col1:
    fig = px.bar(diemThi_SV, x = "MaMH", y = "Diem_HP",
                    color="NamHoc",
                    title= "Thông tin điểm thi của sinh viên")
    st.plotly_chart(fig,use_container_width=True, theme=None)
with col2:
    fig = px.histogram(tongquan.loc[tongquan["MSSV"] == SV], x = "Đơn vị quản lý chuyên môn",
                    color="Đơn vị quản lý chuyên môn",
                    title= "Thông tin điểm thi của sinh viên")
    st.plotly_chart(fig,use_container_width=True, theme=None)
