from selenium import webdriver
import pytest
from ClassHabr import Habr

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(3)
    yield driver
    # driver.close()


def TripAroundHabr(driver):
    actions = Habr(driver)
    actions.navigate_to_page('https://habr.com/ru/companies/otus/articles/596071/')
    actions.authorize()
    actions.authorize()
    actions.main_page()
    # Название статьи
    actions.article_search("AI in education")


    # First attemp to automate captcha

    # solver = TwoCaptcha("there_must_be_a_token")
    # response = solver.recaptcha(sitekey="there_must_be_a_token", url=captcha_page_url)
    # code = response['code']
    # captcha = driver.find_element(By.ID, 'g-recaptcha-response')
    # driver.execute_script(f'arguments[0].value="{code}";', captcha)
    # enter = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/fieldset/div[1]/button')
    # enter.click()
    # logo = driver.find_element(By.LINK_TEXT, 'Хабр')
    # logo.click()
    # check = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[1]/div/h1')
    # assert check.text == 'Моя лента'
