# Programme : get_coin_from_hio
# Description : This method go get the coin
# Date : 23/05/2022
# Author : Christophe Lagaillarde
# Version : 1.0

from selenium_tools.id_exist import id_exist
from selenium import webdriver
from time import sleep
from Credential import Credential


def get_coin_from_hio(driver: webdriver) -> None:
    driver.get("https://hogwarts.io/viewforum.php?f=52")
    while not (id_exist("username", driver) and id_exist("password", driver) and id_exist("login", driver)):
        sleep(1)
    my_login = Credential()
    driver.find_element_by_id("username").send_keys(my_login.get_username())
    driver.find_element_by_id('password').send_keys(my_login.get_password())
    driver.find_element_by_name('login').click()
    del my_login
    sleep(20)
    driver.execute_script("document.getElementsByClassName(\"money money--sickles\")[1].click();")
    driver.close()