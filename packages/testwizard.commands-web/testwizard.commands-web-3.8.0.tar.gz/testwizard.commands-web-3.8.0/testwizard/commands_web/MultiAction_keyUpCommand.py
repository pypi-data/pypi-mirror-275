import sys
import json

from testwizard.commands_core import CommandBase
from testwizard.commands_core.OkErrorCodeAndMessageResult import OkErrorCodeAndMessageResult


class MultiAction_keyUp(CommandBase):
    def __init__(self, testObject):
        CommandBase.__init__(self, testObject, "Selenium.MultiAction_KeyUp")

    def execute(self, key, selector):
        requestObj = [key]
        if selector is not None:
            requestObj = [selector, key]

        result = self.executeCommand(requestObj)

        return OkErrorCodeAndMessageResult(result, "MultiAction_keyUp was successful", "MultiAction_keyUp failed")
