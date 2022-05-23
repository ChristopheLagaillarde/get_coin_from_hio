from selenium.common.exceptions import NoSuchElementException


def check_if_element_exist_with_id(id_of_element, driver):
    try:
        driver.find_element_by_id(f'"{id_of_element}"')
    except NoSuchElementException:
        return False
    return True