from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 设置 WebDriver 选项
chrome_options = Options()
chrome_options.add_argument("--headless")  # 无头模式
chrome_options.add_argument("--disable-gpu")

# # 设置 ChromeDriver 路径
# webdriver_service = Service('/path/to/chromedriver')  # 请替换为你的 chromedriver 路径

# 初始化 WebDriver
driver = webdriver.Chrome()

try:
    # 打开 Daily Papers 页面
    driver.get("https://huggingface.co/papers")
    
    # 等待页面加载并找到 Spectra 研究的链接
    wait = WebDriverWait(driver, 10)
    # wait.until(EC.presence_of_element_located((By.CLASS_NAME, "paper-card")))

    # 获取所有论文卡片元素
    paper_cards = driver.find_elements(By.CSS_SELECTOR, "a")
    print(paper_cards)
    spectra_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Spectra: A Comprehensive Study of Ternary, Quantized, and FP16 Language Models")))
    
    # 点击 Spectra 研究的链接
    spectra_link.click()
    
    # 等待新页面加载
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1")))
    
    # 提取页面上的数据
    title = driver.find_element(By.CSS_SELECTOR, "h1").text
    authors = driver.find_element(By.CSS_SELECTOR, ".authors").text
    abstract = driver.find_element(By.CSS_SELECTOR, ".abstract").text
    
    print(f"Title: {title}")
    print(f"Authors: {authors}")
    print(f"Abstract: {abstract}")
    
finally:
    # 关闭 WebDriver
    driver.quit()