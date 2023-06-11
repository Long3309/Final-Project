import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.figure_factory as ff
st.set_page_config(layout="wide", initial_sidebar_state = "collapsed")
st.header("CS313 - Final Project App")
@st.cache_data()
def load_data():
    # Load datasets từ local file
    st.header("Điểm thi")
    diemThi = pd.read_pickle("diemThi.pkl")
    st.dataframe(diemThi, use_container_width=True)

    st.header("Danh mục môn học")
    danhmucMH = pd.read_csv("danhmucMH.csv")
    # danhmucMH.drop(["Unnamed: 0"], axis=1, inplace=True)
    st.dataframe(danhmucMH, use_container_width=True)

    st.header("Tóm tắt môn học")
    tomtatMH = pd.read_csv("data_script.csv")
    tomtatMH.drop(["STT"],axis = 1,inplace=True)
    st.dataframe(tomtatMH, use_container_width=True)
    
    st.header("Các môn học thay thế")
    thaytheMH = pd.read_pickle("thaytheMH.pkl")
    st.dataframe(thaytheMH, use_container_width=True)
    
    return diemThi, danhmucMH, tomtatMH
    
def main():
    load_data()
if __name__ == '__main__':
    main()
    