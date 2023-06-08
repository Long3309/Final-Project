import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
# url = 'https://daa.uit.edu.vn/danh-muc-mon-hoc-dai-hoc'
url = "https://daa.uit.edu.vn/content/bang-tom-tat-mon-hoc"
# response = requests.get(url)
response =browser.get(url)
# soup = BeautifulSoup(response.content, 'html.parser')
# table = browser.find_element(By.XPATH, '//*[@id="block-system-main"]/div/table[2]')
table = browser.find_element(By.XPATH, '//*[@id="node-8847"]/div/div/div/div/table')
# table = soup.find('table')  # Xác định bảng HTML
data = []
for row in table.find_elements(By.TAG_NAME, 'tr'):  # Duyệt qua từng dòng của bảng
    row_data = []
    for cell in row.find_elements(By.TAG_NAME,'td'):  # Duyệt qua từng ô dữ liệu của dòng
        row_data.append(cell.text)  # Trích xuất dữ liệu từ ô
    data.append(row_data)  # Thêm dữ liệu của dòng vào danh sách
df = pd.DataFrame(data)  # Tạo DataFrame từ danh sách dữ liệu
print(df)  # In DataFrame
df.to_csv('data_script.csv', index=False)  # Lưu DataFrame thành file CSV
