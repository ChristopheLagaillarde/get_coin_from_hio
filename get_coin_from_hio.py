from selenium_tools.check_if_element_exist_with_id import check_if_element_exist_with_id
from time import sleep
from Credential import Credential


def get_coin_from_hio(driver):
    driver.get("https://hogwarts.io/viewforum.php?f=52")
    while check_if_element_exist_with_id("username", driver)\
            and check_if_element_exist_with_id("password", driver)\
            and check_if_element_exist_with_id("login", driver):
        sleep(1)
    my_login = Credential()
    driver.find_element_by_id("username").send_keys(my_login.get_username())
    driver.find_element_by_id('password').send_keys(my_login.get_password())
    driver.find_element_by_name('login').click()
    del my_login
    driver.execute_script("document.getElementsByClassName(\"money money--sickles\")[1].click();")
    driver.close()