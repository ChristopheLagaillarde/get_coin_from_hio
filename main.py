# Programme : GetMoneyFromHio
# Description : This program excecute get_coin_from_hio
# Date : 23/05/2022
# Author : Christophe Lagaillarde
# Version : 1.0

from selenium_tools.while_making_automation_headless import while_making_automation_headless
from get_coin_from_hio import get_coin_from_hio


def main():
    get_coin_from_hio(while_making_automation_headless())


if __name__ == "__main__":
    main()