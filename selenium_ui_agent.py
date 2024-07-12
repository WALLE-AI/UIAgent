from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from PIL import Image
from io import BytesIO
import requests

# 设置Chrome选项
options = Options()
options.add_argument('--headless')  # 无头模式
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')

# 启动WebDriver
driver = webdriver.Chrome()

try:
    # 打开Google
    driver.get("https://www.google.com")

    # 找到搜索框，输入关键词并搜索
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("医学临床指南")
    search_box.send_keys(Keys.RETURN)

    # 等待搜索结果加载
    time.sleep(2)

    # 点击第一个搜索结果
    first_result = driver.find_element(By.CSS_SELECTOR, 'h3')
    first_result.click()

    # 等待页面加载
    time.sleep(2)

    # 截取整个页面的截图
    screenshot = driver.get_screenshot_as_png()
    screenshot_image = Image.open(BytesIO(screenshot))
    screenshot_image.save("screenshot.png")

    # 提取页面所有文字信息
    page_text = driver.find_element(By.TAG_NAME, "body").text
    with open("page_text.txt", "w", encoding="utf-8") as text_file:
        text_file.write(page_text)

    # 提取页面所有图片信息
    images = driver.find_elements(By.TAG_NAME, "img")
    for index, img in enumerate(images):
        src = img.get_attribute('src')
        img_data = requests.get(src).content
        with open(f"image_{index}.png", 'wb') as img_file:
            img_file.write(img_data)

finally:
    # 关闭WebDriver
    driver.quit()