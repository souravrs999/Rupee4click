import time
import requests
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys

opts = Options()
# opts.add_argument("--headless")
# opts.add_argument("--no-sandbox")
# opts.add_argument("--disable-dev-shm-usage")

browser = Firefox(options=opts)

major_url = "https://rupee4click.com"
browser.get(major_url)


def login():

    register = browser.find_element_by_xpath(
        '//*[@id="navbarResponsive"]/ul/li[2]/a'
    ).click()
    login_link = browser.find_element_by_xpath(
        "/html/body/div[1]/div/div[4]/p/a"
    ).click()
    email = browser.find_element_by_xpath('//*[@id="email"]').send_keys(
        " your email within these quotes "
    )
    password = browser.find_element_by_xpath('//*[@id="password"]').send_keys(
        " your password within these quotes "
    )
    sign_in_btn = browser.find_element_by_xpath('//*[@id="login"]/form/button').click()


def data_entry_job():

    dnj = browser.find_element_by_xpath('//*[@id="navbarNav"]/ul/li[6]/a').click()

    while True:

        text = browser.find_element_by_xpath(
            '//*[@id="blockquote"]/div/blockquote/p'
        ).text
        txt_field = browser.find_element_by_xpath(
            '//*[@id="loader"]/div/div[1]/form/div/textarea'
        ).send_keys(text)
        time.sleep(0.5)
        submit_btn = browser.find_element_by_xpath(
            '//*[@id="loader"]/div/div[1]/form/input'
        ).click()
        time.sleep(0.5)


if __name__ == "__main__":

    # login()
    # data_entry_job()

# browser.close()
# quit()
