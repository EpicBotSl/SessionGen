import heroku3
from config import *

herokuclient = heroku3.from_key(HEROKU_API_KEY)


class HerokuHelper:
    def __init__(self, appName, apiKey):
        self.API_KEY = apiKey
        self.APP_NAME = appName
        self.herokuclient = self.getherokuclient()
        self.app = self.herokuclient.apps()[self.APP_NAME]

    def getherokuclient(self):
        return heroku3.from_key(self.API_KEY)

    def getAccount(self):
        return self.herokuclient.account()

    def getLog(self):
        return self.app.get_log()

    def addEnvVar(self, key, value):
        self.app.config()[key] = value

    def restart(self):
        return self.app.restart()
