import sys
import json

from testwizard.commands_core import CommandBase
from testwizard.commands_core.OkErrorCodeAndMessageResult import OkErrorCodeAndMessageResult


class SwitchToParentFrameCommand(CommandBase):
    def __init__(self, testObject):
        CommandBase.__init__(self, testObject, "Selenium.SwitchToParentFrame")

    def execute(self):
        requestObj = []

        result = self.executeCommand(requestObj)

        return OkErrorCodeAndMessageResult(result, "SwitchToParentFrame was successful", "SwitchToParentFrame failed")
