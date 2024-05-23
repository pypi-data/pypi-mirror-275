import sys
import json

from testwizard.commands_core import CommandBase
from testwizard.commands_core.OkErrorCodeAndMessageResult import OkErrorCodeAndMessageResult


class ScrollBy(CommandBase):
    def __init__(self, testObject):
        CommandBase.__init__(self, testObject, "Selenium.ScrollBy")

    def execute(self, x, y):
        requestObj = [x, y]

        result = self.executeCommand(requestObj)

        return OkErrorCodeAndMessageResult(result, "ScrollBy was successful", "ScrollBy failed")
