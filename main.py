from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

opts = Options()
opts.set_headless()

assert opts.headless

browser = Firefox(options=opts)
browser.get('https://duckduckgo.com')
