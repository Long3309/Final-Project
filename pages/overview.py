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
st.dataframe(df_danhmucMH)
st.dataframe(df_tomtatMH, use_container_width=True)

# Chọn sinh viên để lấy ra điểm thi của sinh viên đó
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
# Phân tích số lượng các mã môn học
# diemThi['MaMH_tiento'] = diemThi['MaMH'].str.extract(r'([A-Za-z]+)', expand=False)
# diemThi['MaMH_hauto'] = diemThi['MaMH'].str.extract(r'(\d+)', expand=False)
# diemThi.groupby("MaMH_tiento").size().reset_index()
MaMH_tt = pd.read_pickle("MaMH_tt.pkl")
fig = px.bar(MaMH_tt, x = "MaMH_tiento", y = "SoLuong",
                   color="MaMH_tiento",
                   title= f"Thông tin các mã môn học")
fig.update_layout(barmode='stack', xaxis={'categoryorder':'total descending'})
st.plotly_chart(fig,use_container_width=True)

# Danh mục môn học
# thongtinMH = danhmucMH[["MaMH",'Đơn vị quản lý chuyên môn', 'Loại MH']]
# tongquan = diemThi.merge(thongtinMH, on = "MaMH")
fig = px.histogram(tongquan, x = "Đơn vị quản lý chuyên môn",
                   color='Đơn vị quản lý chuyên môn',
                   title= f"Thông tin các đơn vị quản lý chuyên môn")
st.plotly_chart(fig,use_container_width=True)
# fig = px.histogram(tongquan, x = "MaMH",
#                    color='Đơn vị quản lý chuyên môn',
#                    title= f"Thông tin các đơn vị quản lý chuyên môn")
# st.plotly_chart(fig,use_container_width=True)
