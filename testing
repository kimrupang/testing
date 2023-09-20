from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys



url = 'https://illuminarean.com/'





def start(url):
    global driver

    options = webdriver.ChromeOptions()
    #options.add_argument('headless')
    #options.add_argument('window-size=1920x4000')
    #options.add_argument('--start-maximized')
    #options.add_argument('--start-fullscreen')
    #options.add_argument("disable-gpu")
    options.add_argument("lang=ko_KR")
    options.add_experimental_option("detach", True)
    #service = ChromeService(executable_path=ChromeDriverManager(driver_version="114.0.5735.90").install())
    service = ChromeService(executable_path=ChromeDriverManager().install())

    try:
        driver = webdriver.Chrome(service=service, options=options)
    except:
        post_message("WebDriver 불량\nChome, WebDriver 버전을 확인해 주세요.")

    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(5)
    time.sleep(1)
