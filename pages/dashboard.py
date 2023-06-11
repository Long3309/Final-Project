import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
st.set_page_config(layout="wide")
st.header("CS313 - Final Project App")

tongquan = pd.read_pickle("tongquan.pkl")
fig = px.histogram(tongquan, x = "Diem_HP", text_auto=True, nbins = 50,
                   title= "Thông tin điểm thi sinh viên")
fig.update_traces(textposition = "outside")
st.plotly_chart(fig, use_container_width=True)

# Chọn năm học muốn biết thông tin
namhoc = tongquan["NamHoc"].unique()
namchon = st.selectbox("CHỌN NĂM HỌC MUỐN BIẾT THÔNG TIN", options=sorted(namhoc))
fig = px.histogram(tongquan.loc[tongquan["NamHoc"] == namchon],
                   x = "Diem_HP", text_auto=True, nbins = 50,
                   title= "Thông tin điểm thi sinh viên")
fig.update_traces(textposition = "outside")
st.plotly_chart(fig, use_container_width=True)

# Các môn học có tỉ lệ rớt nhiều nhất
ds_tilerot = pd.read_csv("ds_tilerot.csv")
threshold = st.number_input("CHỌN THRESHOLD SỐ LƯỢNG ĐĂNG KÝ", min_value=500,max_value=10000, step=500, value=1000)
fig = px.bar(ds_tilerot[ds_tilerot["Tổng số lượng"] > threshold].sort_values(["Tỉ lệ trượt"], ascending = False).head(10),
             x = "MaMH", y = "Tỉ lệ trượt",
             color="Tỉ lệ trượt", text_auto=True,
             hover_data=["Số lượng rớt","Tổng số lượng"],
             title= f"Top 10 môn có tỉ lệ trượt cao nhất (Số lượt đăng ký > {threshold})")
fig.update_traces(textposition = "outside")
st.plotly_chart(fig, use_container_width=True)

# Chia môn học theo loại MH
# tongquan_loaiMH = tongquan[["MaMH", "Loại MH"]]
tongquan_loaiMH = pd.read_csv("soluong_MH.csv")
# tongquan_loaiMH.groupby(["MaMH"]).count().reset_index("count")
loaiMH = st.selectbox("CHỌN LOẠI MÔN HỌC", options=tongquan_loaiMH["Loại MH"].unique())
fig = px.bar(tongquan_loaiMH.loc[tongquan_loaiMH["Loại MH"]== loaiMH],
             x = "MaMH", y = "Tổng số lượng",
             color = "Tổng số lượng",
             title = f"Thông tin môn học thuộc Loại `{loaiMH}`")
st.plotly_chart(fig, use_container_width=True)

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
