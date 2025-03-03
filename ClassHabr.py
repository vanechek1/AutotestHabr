from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pytest
from twocaptcha import TwoCaptcha
import time
from config import user_name, password

class Habr:

    def __init__(self, driver):
        self.driver = driver

    def navigate_to_page(self, page_url):
        self.driver.get(page_url)

    def authorize(self):
        button_entrance = self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/a[2]/button')
        button_entrance.click()

        email_input = self.driver.find_element(By.XPATH, '//*[@id="ident-form"]/div[1]/input')
        email_input.send_keys(user_name)
        password_input = self.driver.find_element(By.XPATH, '//*[@id="ident-form"]/div[2]/input')
        password_input.send_keys(password)

        # Поиск капчи и вход во фрейм
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH, '//*[@id="ident-form"]/div[3]/div/div/div/iframe'))

        captcha = self.driver.find_element(By.XPATH, '//*[@id="recaptcha-anchor"]/div[1]')
        captcha.click()
        try:
            element = WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'span[aria-checked="true"]')))

            # Выход из фрейма и нажатие на кнопку "Вход"
            self.driver.switch_to.default_content()
            enter = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/fieldset/div[1]/button')
            enter.click()
        except:
            print('Element not found')
            self.driver.quit()

    def main_page(self):
        logo = self.driver.find_element(By.LINK_TEXT, 'Хабр')
        logo.click()

    def article_search(self, article_name):
        # Открыть строку поиска
        try:
            svg_find = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-test-id="search-button"]')))
            svg_find.click()
        except:
            print('No such element to click')

        search = self.driver.find_element(By.CSS_SELECTOR, 'input[class="tm-search__input tm-input-text-decorated__input"]')
        search.send_keys(f'{article_name}\n')

        for i in range(2, 10):
            try:
                webpage = WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, '//span[contains(text(),"GoROBO")]')))
                webpage.click()
                break
            except:
                nextpage = self.driver.find_element(By.XPATH,
                                               f'//a[@class="tm-pagination__page" and contains(text(),"{i}")]')
                nextpage.click()
