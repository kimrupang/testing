from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys



url = 'https://illuminarean.com/'



def win_handles():
    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(1)


def scan_errors():
    driver.get_screenshot_as_file('error.png')


def clicks_xpath(address, texts):
    timecheck = 0
    while True:
        try:
            driver.find_element(By.XPATH, address).click()
            time.sleep(1)
            break
        except Exception:
            timecheck = timecheck + 1
            time.sleep(3)
            if timecheck == rest_time:
                scan_errors()
                post_message(texts + "\n클릭이 불가능 합니다.")
                file_update('error.png')
                break
    if timecheck == rest_time:
        driver.quit()
        sys.exit()


def click_id(address, texts):
    timecheck = 0
    while True:
        try:
            driver.find_element(By.ID, address).click()
            time.sleep(1)
            break
        except Exception:
            timecheck += 1
            time.sleep(3)
            if timecheck == rest_time:
                scan_errors()
                post_message(texts + "\n클릭이 불가능 합니다.")
                file_update('error.png')
                break
    if timecheck == rest_time:
        driver.quit()
        sys.exit()


def inputkey(address, key, texts):
    timecheck = 0

    while True:
        try:
            driver.find_element(By.XPATH, address).send_keys(key)
            time.sleep(1)
            break
        except Exception:
            timecheck += 1
            time.sleep(5)
            if timecheck == rest_time:
                scan_errors()
                post_message(texts + "입력이 불가능합니다.")
                file_update('error.png')
                break
    if timecheck == rest_time:
        driver.quit()
        sys.exit()


def inputkey_id(address, key, texts):
    timecheck = 0
    while True:
        try:
            driver.find_element(By.ID, address).send_keys(key)
            time.sleep(1)
            break
        except Exception:
            timecheck += 1
            time.sleep(5)
            if timecheck == rest_time:
                scan_errors()
                post_message(texts + "입력이 불가능합니다.")
                file_update('error.png')
                break
    if timecheck == rest_time:
        driver.quit()
        sys.exit()




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
    service = ChromeService(executable_path=ChromeDriverManager().install())

    try:
        driver = webdriver.Chrome(service=service, options=options)
    except:
        post_message("WebDriver 불량\nChome, WebDriver 버전을 확인해 주세요.")

    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(5)
    time.sleep(1)
