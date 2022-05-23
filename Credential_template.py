# Programme : Credential_template
# Description : This class is the template of the Crendential class
# Date : 23/05/2022
# Author : Christophe Lagaillarde
# Version : 1.0

class Credential:

    def __init__(self):
        self.username = ''
        self.password = ''

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password