import time

import requests
from loguru import logger
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os

from tqdm import tqdm

from webdriver.config import SEARCG_URL_DICT
from webdriver.selenium_driver import SeleniumDrvier


DOWNLOAD_PDF_DIR = "pdf_download"


class ChormeWebAgent():
    def __init__(self):
        self.desc = "Chorme Web Agent"
        self.driver =SeleniumDrvier.get_driver()

    def __str__(self):
        return self.desc

    def get_chorme_search_web(self,user_query):
        '''

        :param user_query:
        :return:
        '''
        self.driver.get(SEARCG_URL_DICT["Chorme"])
        search_box = self.driver.find_element(By.NAME, "q")
        search_box.send_keys(user_query)
        search_box.send_keys(Keys.RETURN)
        time.sleep(2)
        ##下载搜索页面中pdf文件
        self.download_web_similarity_pdf_file()

    def list_pdf_files_in_directory(self,directory_path):
        try:
            # 获取目录中的所有文件和子目录
            entries = os.listdir(directory_path)

            # 过滤并只保留 PDF 文件
            pdf_files = [entry for entry in entries if
                         entry.lower().endswith('.pdf') and os.path.isfile(os.path.join(directory_path, entry))]
            return pdf_files
        except Exception as e:
            print(f"An error occurred: {e}")
            return []
    def download_web_similarity_pdf_file(self):
        if not os.path.exists(DOWNLOAD_PDF_DIR):
            os.makedirs(DOWNLOAD_PDF_DIR)
        pdf_links = []
        search_results = self.driver.find_elements(By.XPATH, '//a')

        for result in search_results:
            href = result.get_attribute('href')
            if href and href.endswith('.pdf'):
                pdf_links.append(href)
        pdf_files_local = self.list_pdf_files_in_directory(DOWNLOAD_PDF_DIR)
        for pdf_link in tqdm(pdf_links):
            pdf_name_id = pdf_link.split("/")[-1]
            if pdf_name_id not in pdf_files_local:
                logger.info(f"download pdf name {pdf_name_id}")
                # pdf_url = base_url + pdf_name_id
                pdf_response = requests.get(pdf_link)
                ##延迟两秒
                time.sleep(1)
                # 获取PDF文件名
                pdf_name = os.path.join(DOWNLOAD_PDF_DIR, pdf_name_id)
                # 保存PDF文件
                with open(pdf_name, 'wb') as pdf_file:
                    logger.info(f"downloading pdf {pdf_name_id}")
                    pdf_file.write(pdf_response.content)
            else:
                logger.info(f"pdf name is local exist {pdf_name_id}")


def test_chorme_selenuim_search(query):
    agent = ChormeWebAgent()
    agent.get_chorme_search_web(query)