# Programme : name_exist
# Description : This function check if the element with specified name exist
# Date : 28/05/2022
# Author : Christophe Lagaillarde
# Version : 1.0

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import InvalidSelectorException

from selenium import webdriver


def name_exist(name_of_element: str, driver: webdriver) -> bool:
    try:
        driver.find_element_by_id(f'"{name_of_element}"')
    except NoSuchElementException:
        return False

    except InvalidSelectorException:
        return False

    return True