import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
url = 'https://daa.uit.edu.vn/danh-muc-mon-hoc-dai-hoc'
# url = "https://daa.uit.edu.vn/content/bang-tom-tat-mon-hoc"
# response = requests.get(url)
browser.get(url)
table = browser.find_element(By.XPATH, '//*[@id="block-system-main"]/div/table[2]')
# table = browser.find_element(By.XPATH, '//*[@id="node-8847"]/div/div/div/div/table')
data = []
for row in table.find_elements(By.TAG_NAME, 'tr'):  # Duyệt qua từng dòng của bảng
    row_data = []
    for cell in row.find_elements(By.TAG_NAME,'td'):  # Duyệt q ua từng ô dữ liệu của dòng
            row_data.append(cell.text)  # Trích xuất dữ liệu từ ô
    data.append(row_data)  # Thêm dữ liệu của dòng vào danh sách
df = pd.DataFrame(data)  # Tạo DataFrame từ danh sách dữ liệu
print(df)  # In DataFrame
df.to_csv('data_test.csv', index=False)  # Lưu DataFrame thành file CSV

imgs = browser.find_elements(By.XPATH, "//img[@typeof = 'foaf:Image']")
lst_check = []
for img in imgs:
    img = img.get_attribute("src")
    if img == "https://daa.uit.edu.vn/sites/daa/files/uploads/checked.png":
        print("True")
        lst_check.append("True")
    else:
        print("False")
        lst_check.append("False")
with open("check.txt", "w") as f:
    f.writelines('\n'.join(lst_check))
