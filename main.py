from selenium import webdriver
from Credential import Credential
from time import sleep


def while_making_automation_headless():
    options = webdriver.EdgeOptions()
    options.headless = True
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument("--disable-extensions")
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    options.add_argument("--start-maximized")
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    driver = webdriver.Edge(executable_path="msedgedriver.exe", options=options)
    return driver


def check_if_element_exist_with_id(id_of_element, driver):
    try:
        driver.find_element_by_id(f'"{id_of_element}"')
    except Exception:
        return False
    return True


def get_coin_from_hio(driver):
    driver.get("https://hogwarts.io/viewforum.php?f=52")
    my_login = Credential()
    while check_if_element_exist_with_id("username", driver)\
            and check_if_element_exist_with_id("password", driver)\
            and check_if_element_exist_with_id("login", driver):
        sleep(1)

    driver.find_element_by_id("username").send_keys(my_login.get_username)
    driver.find_element_by_id('password').send_keys(my_login.get_password)
    driver.find_element_by_name('login').click()
    del my_login
    sleep(10)
    driver.execute_script("document.getElementsByClassName(\"money money--sickles\")[1].click();")
    driver.close()


def main():
    get_coin_from_hio(while_making_automation_headless())


if __name__ == "__main__":
    main()