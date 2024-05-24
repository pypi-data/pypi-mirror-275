import sys
import json

from testwizard.commands_core import CommandBase
from testwizard.commands_core.OkErrorCodeAndMessageResult import OkErrorCodeAndMessageResult


class GoToUrl(CommandBase):
    def __init__(self, testObject):
        CommandBase.__init__(self, testObject, "Selenium.GoToUrl")

    def execute(self, url):
        requestObj = [url]

        result = self.executeCommand(requestObj)

        return OkErrorCodeAndMessageResult(result, "GoToUrl was successful", "GoToUrl failed")
